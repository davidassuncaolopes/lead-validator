from app.email_validator import validar_email


def test_validar_email():
    # Formato válido
    assert validar_email("ana@example.com") is True

    # Formato inválido
    assert validar_email("pedro.souza@") is False

    # Campo vazio
    assert validar_email("") is False

    # Apenas espaços
    assert validar_email("   ") is False

    # Espaços externos
    assert validar_email(" ana@example.com ") is True

    print("Todos os testes de validação de e-mail passaram!")


if __name__ == "__main__":
    test_validar_email()