import pandas as pd

from app.cleaner import limpar_base


def test_limpar_base():
    dados = pd.DataFrame({
        " Nome ": [" Ana ", "Ana duplicada", "Bruno", "Carla"],
        " Email ": [
            "ANA@EXAMPLE.COM",
            "ana@example.com",
            None,
            "  carla@example.com  ",
        ],
        " Empresa ": [" Empresa A ", "Empresa B", "Empresa C", "Empresa D"],
    })

    original = dados.copy(deep=True)

    resultado = limpar_base(dados)

    # 1. Colunas padronizadas
    assert list(resultado.columns) == ["nome", "email", "empresa"]

    # 2. E-mails em minúsculas e sem espaços externos
    assert resultado.loc[0, "email"] == "ana@example.com"
    assert "carla@example.com" in resultado["email"].tolist()

    # 3. Duplicata removida, contato sem e-mail preservado
    assert len(resultado) == 3
    assert resultado["email"].isna().sum() == 1

    # 4. DataFrame original não alterado
    pd.testing.assert_frame_equal(dados, original)

    print("Todos os casos-limite passaram!")


if __name__ == "__main__":
    test_limpar_base()