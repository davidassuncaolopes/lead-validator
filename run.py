from pathlib import Path

import pandas as pd

from app.cleaner import limpar_base
from app.email_validator import validar_email


def processar_base(arquivo_entrada: str, arquivo_saida: str) -> None:
    """Limpa uma base de leads, valida e-mails e salva o resultado."""
    leads = pd.read_csv(arquivo_entrada)
    leads_limpos = limpar_base(leads)

    if "email" in leads_limpos.columns:
        leads_limpos["email_valido"] = leads_limpos["email"].apply(
            validar_email
        )

    caminho_saida = Path(arquivo_saida)
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    leads_limpos.to_csv(caminho_saida, index=False)

    print(f"Arquivo processado: {Path(arquivo_entrada).name}")
    print(f"Registros originais: {len(leads)}")
    print(f"Registros após limpeza: {len(leads_limpos)}")

    if "email_valido" in leads_limpos.columns:
        validos = int(leads_limpos["email_valido"].sum())
        invalidos = len(leads_limpos) - validos
        print(f"E-mails com formato válido: {validos}")
        print(f"E-mails com formato inválido: {invalidos}")

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