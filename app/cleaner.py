import pandas as pd


def limpar_base(leads: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa e padroniza uma base de leads sem alterar o DataFrame original.
    """
    leads_limpos = leads.copy()

    # Padroniza os nomes das colunas
    leads_limpos.columns = (
        leads_limpos.columns
        .str.strip()
        .str.lower()
    )

    # Remove espaços extras dos campos de texto
    for coluna in leads_limpos.select_dtypes(include=["object"]).columns:
        leads_limpos[coluna] = leads_limpos[coluna].str.strip()

    # Padroniza os e-mails em letras minúsculas
    if "email" in leads_limpos.columns:
        leads_limpos["email"] = leads_limpos["email"].str.lower()

    # Converte campos vazios em valores ausentes
    leads_limpos = leads_limpos.replace(r"^\s*$", pd.NA, regex=True)

    # Remove duplicatas usando o e-mail como critério
    if "email" in leads_limpos.columns:
        leads_limpos["email"] = leads_limpos["email"].replace("", pd.NA)

        leads_com_email = leads_limpos[
            leads_limpos["email"].notna()
        ].drop_duplicates(subset=["email"], keep="first")

        leads_sem_email = leads_limpos[
            leads_limpos["email"].isna()
        ]

        leads_limpos = pd.concat(
            [leads_com_email, leads_sem_email],
            ignore_index=True
        )

    return leads_limpos