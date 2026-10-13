from validate_email import validate_email


def validar_email(email: str) -> bool:
    """Verifica se o endereço de e-mail tem formato válido."""
    if not isinstance(email, str) or not email.strip():
        return False

    resultado = validate_email(email.strip())
    return bool(resultado)