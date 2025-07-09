const fs = require('fs');
const path = require('path');

const dirs = ['.serverless', 'artifacts'];

dirs.forEach((dir) => {
  const fullPath = path.join(__dirname, '..', dir);
  if (fs.existsSync(fullPath)) {
    fs.rmSync(fullPath, { recursive: true, force: true });
    console.log(`✅ Removido: ${dir}`);
  } else {
    console.log(`ℹ️ Diretório não encontrado: ${dir}`);
  }
});