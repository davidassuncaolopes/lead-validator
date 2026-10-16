import pandas as pd

from run import processar_base


def test_processar_base(tmp_path):
    # Cria uma base fictícia de entrada
    arquivo_entrada = tmp_path / "leads_teste.csv"
    arquivo_saida = tmp_path / "resultado" / "leads_processados.csv"

    leads = pd.DataFrame(
        {
            "nome": ["Ana Costa", "Ana Costa", "Pedro Souza"],
            "email": [
                "ana@example.com",
                "ana@example.com",
                "pedro.souza@",
            ],
            "empresa": [
                "Cloud Systems",
                "Cloud Systems",
                "Web Company",
            ],
            "cargo": [
                "Analista",
                "Analista",
                "Designer",
            ],
        }
    )

    leads.to_csv(arquivo_entrada, index=False)

    # Executa o fluxo completo
    processar_base(str(arquivo_entrada), str(arquivo_saida))

    # Confirma que o arquivo foi criado
    assert arquivo_saida.exists()

    resultado = pd.read_csv(arquivo_saida)

    # Confirma a limpeza de duplicatas
    assert len(resultado) == 2

    # Confirma a validação dos e-mails
    assert "email_valido" in resultado.columns
    assert resultado["email_valido"].tolist() == [True, False]

    # Confirma a geração das buscas
    assert "busca_linkedin" in resultado.columns
    assert resultado["busca_linkedin"].str.startswith(
        "https://www.google.com/search?q="
    ).all()

    print("Teste de integração concluído com sucesso!")