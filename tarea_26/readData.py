# Imports
import csv
import json
import pandas as pd
from datetime import datetime

# Leer fichero
def load_csv(filename):
    print(f"Cargando: {filename}.csv")
    with open(f'./data/{filename}.csv', newline = '') as f:
        reader = csv.reader(f, delimiter =';', quoting = csv.QUOTE_NONE)
        for i, row in enumerate(reader):

            if i < 2:
                # Imprimir la descripción de los datos
                print(f" - {row[0]}")
                continue

            if i == 2:
                header = row
                header[0] = "fecha"
                header[1] = "total"
                df = pd.DataFrame(columns = header)
                continue

            if row is not "":
                row_dict = {}
                for j, value in enumerate(row):
                    if j == 0:
                        # Transformar a formato fecha si es posible
                        try:
                            row_dict[header[j]] = datetime.strptime(value, '%Y/%m/%d')
                        except:
                            row_dict[header[j]] = value
                    elif value is not "":
                        row_dict[header[j]] = int(value)

                df = df.append(row_dict, ignore_index=True)
                
    return df
    
HOSPITALES = [
    {
        "geo": "guipuzcoa",
        "hospitales": ["03 Donosti", "06 Zumarraga", "07 Bidasoa", "08 Mendaro", "09 Alto Deba", "12 Eibar"]
    },
    {
        "geo": "vizcaya",
        "hospitales": ["02 Cruces", "04 Basurto", "05 Galdakao", "10 San Eloy", "11 Urduliz", "14 Sta Marina", "15 Gorliz", "BERMEO H.", "ZALDIBAR H.", "ZAMUDIO H."]
    },
    {
        "geo": "alaba",
        "hospitales": ["01 Araba", "13 Leza", "ÁLAVA PSIQUIÁTRICO H."]
    }

]
    
def group_by_region(df):

    df_new = pd.DataFrame()
    
    df_new["fecha"] = df["fecha"]
    df_new["total"] = df["total"]

    with open('hospitales.json', encoding="utf-8") as json_file:
        hospitales_por_territorio = json.load(json_file)
        
        for hospitales_territorio in hospitales_por_territorio:
        
            geo = hospitales_territorio["geo"]
            df_new[geo] = 0
            for hosp in hospitales_territorio["hospitales"]:
                
                if hosp in df.columns:
                    df_new[geo] += df[hosp].fillna(0)
                else:
                    print(f"--> WARNING: No data for hospital {hosp} ({geo})")
        
        df_new["total_calculado"] = df_new["guipuzcoa"] + df_new["vizcaya"] + df_new["alaba"] 
    
    return df_new
    
    
df_01 = group_by_region(load_csv("01"))
df_02 = group_by_region(load_csv("02"))
df_03 = group_by_region(load_csv("03"))
df_04 = group_by_region(load_csv("04"))
df_05 = group_by_region(load_csv("05"))
df_06 = group_by_region(load_csv("06"))
df_07 = group_by_region(load_csv("07"))
df_08 = group_by_region(load_csv("08"))
df_09 = group_by_region(load_csv("09"))


print("Pandas dataframes available: df_01, df_02, df_03, df_04, df_05, df_06, df_07, df_08, df_09")

