"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd
    import re
    import os

    def format_date(str_date):
        d = re.search(r'(^\d+)\/(\d+)\/(\d+)', str_date, re.IGNORECASE)
        day = d.group(1)
        month = d.group(2)
        year = d.group(3)
        if len(day)>2:
            date = year + '/' + month + '/' + day
            return date
        else:
            date = day + '/' + month + '/' + year
            return date

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")
    df = df[df.columns[1:]]
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    for i in df.columns:
        try:
            df[i]= df[i].str.lower()
        except:
            pass
    if "lã­nea_credito" in df.columns:
        df.rename(columns={"lã­nea_credito": "línea_credito"}, inplace=True)

    df.idea_negocio = df.idea_negocio.map(lambda x: re.sub("-|_", " ", str(x)))
    df.idea_negocio = df.idea_negocio.str.strip()
    df.monto_del_credito = df.monto_del_credito.map(lambda x: re.sub("\$|,", "", str(x)))
    df["línea_credito"] = df["línea_credito"].map(lambda x: re.sub("-|_", " ", str(x)))
    df["línea_credito"] = df["línea_credito"].str.strip()
    df.barrio = df.barrio.map(lambda x: re.sub("-| ", "_", str(x)))
    df.fecha_de_beneficio = df.fecha_de_beneficio.map(format_date)
    df.monto_del_credito = df.monto_del_credito.map(lambda x : float(x))

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.tipo_de_emprendimiento.unique()

    df.sexo.value_counts().to_list()
    df.tipo_de_emprendimiento.value_counts().to_list()
    df.idea_negocio.value_counts().to_list()
    df.barrio.value_counts().to_list()
    df.estrato.value_counts().to_list()
    df.comuna_ciudadano.value_counts().to_list()
    df.fecha_de_beneficio.value_counts().to_list()
    df.monto_del_credito.value_counts().to_list()
    df.línea_credito.value_counts().to_list()

    output_dir = "files/output/"
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv("files/output/solicitudes_de_credito.csv", index=False, header=True, sep=";")

    return df

pregunta_01()


