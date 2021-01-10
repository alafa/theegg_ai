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
                if i == 0:
                    title = row[0]
                    
                if i == 1:
                    title_note = row[0]
                    
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
                
    return {"data": df, "title": title, "title_note": title_note}
    
    
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
    
    
def load_csvs():
    
    csv_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
    
    data = []
    for csv_id in csv_list:
        d = load_csv(csv_id)
        d["data"] = group_by_region(d["data"])
        data.append(d)
        
    return data
 

CSVS_DATA = load_csvs()
print("Pandas dataframes available in CSVS_DATA[]['data']")

