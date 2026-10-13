from pathlib import Path

import pandas as pd

from app.cleaner import limpar_base


def processar_base(arquivo_entrada: str, arquivo_saida: str) -> None:
    """Limpa uma base de leads e salva o resultado separadamente."""
    leads = pd.read_csv(arquivo_entrada)
    leads_limpos = limpar_base(leads)

    caminho_saida = Path(arquivo_saida)
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    leads_limpos.to_csv(caminho_saida, index=False)

    print(f"Arquivo processado: {Path(arquivo_entrada).name}")
    print(f"Registros originais: {len(leads)}")
    print(f"Registros após limpeza: {len(leads_limpos)}")
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