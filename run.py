from pathlib import Path

import pandas as pd

from app.cleaner import limpar_base
from app.email_validator import validar_email
from app.linkedin import gerar_busca_linkedin


def processar_base(arquivo_entrada: str, arquivo_saida: str) -> None:
    """Limpa leads, valida e-mails e gera buscas por perfis no LinkedIn."""
    leads = pd.read_csv(arquivo_entrada)
    leads_limpos = limpar_base(leads)

    # Valida o formato dos e-mails
    if "email" in leads_limpos.columns:
        leads_limpos["email_valido"] = leads_limpos["email"].apply(
            validar_email
        )

    # Gera links de busca por nome e empresa
    if "nome" in leads_limpos.columns:
        leads_limpos["busca_linkedin"] = leads_limpos.apply(
            lambda linha: gerar_busca_linkedin(
                linha.get("nome"),
                linha.get("empresa", ""),
            ),
            axis=1,
        )

    # Salva o resultado
    caminho_saida = Path(arquivo_saida)
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)
    leads_limpos.to_csv(caminho_saida, index=False)

    # Exibe o resumo do processamento
    print(f"Arquivo processado: {Path(arquivo_entrada).name}")
    print(f"Registros originais: {len(leads)}")
    print(f"Registros após limpeza: {len(leads_limpos)}")

    if "email_valido" in leads_limpos.columns:
        validos = int(leads_limpos["email_valido"].sum())
        invalidos = len(leads_limpos) - validos
        print(f"E-mails com formato válido: {validos}")
        print(f"E-mails com formato inválido: {invalidos}")

    if "busca_linkedin" in leads_limpos.columns:
        buscas_geradas = int(
            leads_limpos["busca_linkedin"].ne("").sum()
        )
        print(f"Buscas de LinkedIn geradas: {buscas_geradas}")

    print(f"Resultado salvo em: {caminho_saida}")
    print("-" * 40)


if __name__ == "__main__":
    processar_base(
        "data/leads.csv",
        "output/leads_limpos.csv",
    )

    processar_base(
        "data/leads_teste_reais.csv",
        "output/leads_teste_reais_limpos.csv",
    )
