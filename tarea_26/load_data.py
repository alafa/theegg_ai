# Imports
import csv
import json
import pandas as pd
from datetime import datetime

# Leer fichero
def data_load_csv(file_details):
    
    filepath = f"{file_details['directory']}/{file_details['filename']}"
    header_row = file_details['header_row']

    print(f"Cargando: {file_details['name']} ({filepath})")
    with open(f'./data/{filepath}', newline = '') as f:
        reader = csv.reader(f, delimiter =';', quoting = csv.QUOTE_NONE)
        for i, row in enumerate(reader):

            if i < header_row:
                continue

            if i == header_row:
                header = row
                
                if file_details['directory'] == "datos-asistenciales":
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
                        
                        try:
                            row_dict[header[j]] = int(value)
                            
                        # Si es decimal entrará aqui
                        except:
                            row_dict[header[j]] = float(value.replace(",", "."))

                df = df.append(row_dict, ignore_index=True)
                
    return df
    

def get_columns_new_names(columns):
    column_name_conversions = {}
    for col in df.columns:

        new_col_came = col.lower()
        new_col_came = new_col_came.split("/ ")[-1]
        new_col_came = new_col_came.split(":")[0]

        if "incidencia acumulada 14 días" in col.lower():
            new_col_came = f"{new_col_came}_incidencia_acum_14d"

        column_name_conversions[col] = new_col_came
    return column_name_conversions
    
    
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
        
        df_new["total_calculado"] = df_new["guipuzcoa"] + df_new["vizcaya"] + df_new["alava"] 
    
    return df_new
    
    
def assistential_data_load_csvs():
    
    csv_list = ["01", "04"]
    
    data = []
    for csv_id in csv_list:
        d = assistential_data_load_csv(csv_id)
        d["data"] = group_by_region(d["data"])
        data.append(d)
        
    return data
 
 

FILES = [
    {
        'name': 'ingresos_en_planta',
        'directory': "datos-asistenciales",
        'filename': "01.csv",
        'header_row': 2,
        'need_to_group_hospitals_by_region': True
    },
    {
        'name': 'ingresos_en_UCI',
        'directory': "datos-asistenciales",
        'filename': "04.csv",
        'header_row': 2,
        'need_to_group_hospitals_by_region': True
    },
    {
        'name': 'positive_cases_by_region',
        'directory': "situacion-epidemiologica",
        'filename': "02.csv",
        'header_row': 1,
        'need_to_group_hospitals_by_region': False
    },
    {
        'name': 'positive_cases_by_gender_and_age',
        'directory': "situacion-epidemiologica",
        'filename': "09.csv",
        'header_row': 1,
        'need_to_group_hospitals_by_region': False
    },
    {
        'name': 'deaths',
        'directory': "situacion-epidemiologica",
        'filename': "08.csv",
        'header_row': 2,
        'need_to_group_hospitals_by_region': False
    }
]

DATA = {}

for file_to_read in FILES:

    df = data_load_csv(file_to_read)
    
    if file_to_read['need_to_group_hospitals_by_region']:
        df = group_by_region(df)
    
    # Ajustar los nombres de las columnas 
    df = df.rename(columns=get_columns_new_names(df.columns))
    
    # Eliminar la columna vacia (si la hay)
    if '' in list(df.columns):
        df = df.drop([''], axis=1)
    DATA[file_to_read['name']] = df
    
print(f"Data available in DATA object")

