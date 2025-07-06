from user_agents import parse


def is_bot_user_agent(user_agent: str | None) -> bool:
    """Função pura que determina se um user agent é de um bot"""
    if _is_empty_user_agent(user_agent):
        return True

    bot_checks = [_contains_bot_keyword, _is_parsed_bot]
    return any(check(user_agent) for check in bot_checks)


def _is_empty_user_agent(user_agent: str | None) -> bool:
    """Verifica se user agent está vazio ou None"""
    return not user_agent


def _contains_bot_keyword(user_agent: str) -> bool:
    """Verifica se user agent contém palavra 'bot'"""
    return 'bot' in user_agent.lower()


def _is_parsed_bot(user_agent: str) -> bool:
    """Verifica se user agent é identificado como bot pelo parser"""
    return parse(user_agent).is_bot
