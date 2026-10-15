from app.linkedin import gerar_busca_linkedin


def test_gerar_busca_linkedin():
    # Nome e empresa
    assert gerar_busca_linkedin(
        "Ana Costa", "Cloud Systems"
    ) == "https://www.google.com/search?q=Ana+Costa+Cloud+Systems+LinkedIn"

    # Apenas o nome
    assert gerar_busca_linkedin(
        "Ana Costa"
    ) == "https://www.google.com/search?q=Ana+Costa+LinkedIn"

    # Nome vazio
    assert gerar_busca_linkedin("") == ""

    # Nome ausente
    assert gerar_busca_linkedin(None) == ""

    print("Todos os testes de busca LinkedIn passaram!")


if __name__ == "__main__":
    test_gerar_busca_linkedin()
