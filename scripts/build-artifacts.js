const fs = require('fs-extra');
const path = require('path');
const { execSync } = require('child_process');
const archiver = require('archiver');

const buildFunction = async (name) => {
  const srcDir = path.resolve('src', name);
  const commonDir = path.resolve('src', 'common');
  const requirementsFile = path.join(srcDir, 'requirements.txt');
  
  // Cada função tem seu próprio diretório temporário isolado
  const buildDir = path.resolve(`temp_build_${name}`);
  const outputZip = path.resolve('artifacts', `serverless_function_${name}.zip`);

  console.log(`\n🔧 Empacotando função: ${name}`);

  try {
    // Limpa e cria a pasta dedicada para esta função específica
    await fs.remove(buildDir);
    await fs.ensureDir(path.join(buildDir, 'src'));

    console.log('📦 Instalando dependências...');
    execSync(`pip install -r ${requirementsFile} -t ${buildDir}`, { stdio: 'inherit' });

    console.log('📁 Copiando código fonte...');
    await fs.copy(srcDir, path.join(buildDir, 'src', name));
    
    // Verifica se o diretório common existe antes de copiar
    if (await fs.pathExists(commonDir)) {
      await fs.copy(commonDir, path.join(buildDir, 'src', 'common'));
    } else {
      // console.error('⚠️  Diretório common não encontrado')
      throw new Error('Diretório common não encontrado');
    }

    console.log('🗜️ Compactando para ZIP...');
    await fs.ensureDir('artifacts');
    
    const output = fs.createWriteStream(outputZip);
    const archive = archiver('zip', { zlib: { level: 9 } });

    // Promise para aguardar o fim do processo de compactação
    const zipPromise = new Promise((resolve, reject) => {
      output.on('close', resolve);
      output.on('error', reject);
      archive.on('error', reject);
    });

    archive.pipe(output);
    archive.directory(buildDir + '/', false);
    await archive.finalize();
    await zipPromise;

    console.log(`✅ Função '${name}' empacotada em: ${outputZip}`);

  } catch (error) {
    console.error(`❌ Erro ao empacotar função '${name}':`, error);
    throw error;
    
  } finally {
    // Garante que o diretório temporário seja sempre removido
    if (await fs.pathExists(buildDir)) {
      await fs.remove(buildDir);
      console.log(`🧹 Diretório temporário '${buildDir}' removido.`);
    }
  }
};

// Função para build individual
const buildSingle = async (functionName) => {
  try {
    console.log(`🚀 Iniciando build da função: ${functionName}`);
    await buildFunction(functionName);
    console.log(`🎉 Build da função '${functionName}' finalizado com sucesso!`);
  } catch (err) {
    process.exit(1);
  }
};

// Função para build de todas as funções (independentemente)
const buildAll = async () => {
  const functions = ['registrar', 'relatorio'];
  
  console.log('🚀 Iniciando build de todas as funções...');
  
  for (const functionName of functions) {
    try {
      await buildFunction(functionName);
    } catch (err) {
      process.exit(1);
    }
  }
  
  console.log('\n🎉 Build de todas as funções finalizado com sucesso!');
};

// Verifica argumentos da linha de comando
const main = async () => {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    // Sem argumentos: build todas as funções
    await buildAll();

  } else if (args.length === 1) {
    // Com argumento: build função específica
    const functionName = args[0];
    if (['registrar', 'relatorio'].includes(functionName)) {
      await buildSingle(functionName);
    } else {
      console.error('❌ Função inválida. Use: registrar ou relatorio');
      console.log('💡 Uso: node build-artifacts.js [registrar|relatorio]');
      process.exit(1);
    }
  } else {
    console.error('❌ Muitos argumentos fornecidos.');
    console.log('💡 Uso: node build-artifacts.js [registrar|relatorio]');
    process.exit(1);
  }
};

// Exporta funções para uso programático
module.exports = {
  buildFunction,
  buildSingle,
  buildAll
};

// Executa apenas se chamado diretamente
if (require.main === module) {
  main().catch(err => {
    console.error('❌ Erro fatal:', err);
    process.exit(1);
  });
}