from urllib.parse import quote_plus


def gerar_busca_linkedin(nome: str, empresa: str = "") -> str:
    """Gera uma busca pública por um perfil no LinkedIn."""
    nome = nome.strip() if isinstance(nome, str) else ""
    empresa = empresa.strip() if isinstance(empresa, str) else ""

    if not nome:
        return ""

    partes = [nome, empresa, "LinkedIn"]
    consulta = " ".join(parte for parte in partes if parte)
    consulta_codificada = quote_plus(consulta)

    return f"https://www.google.com/search?q={consulta_codificada}"