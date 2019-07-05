import pandas as pd
from sqlalchemy import create_engine

# READING A FILE
catalonia = pd.read_csv("catalonia_pol.csv")

# CREATING A DATA FRAME AND CHANGING NAMES
municipalities = catalonia[["mun_id", "municipalities", "re_id"]]
municipalities = municipalities.rename(columns={"re_id":"prov_id"})
municipalities.to_csv("mun_id_table.csv")

# NAME OF THE ALL PARTIES
parties = ["PP", "PSOE", "PODEMOS-IU-EQUO", "Cs", "ECP", "PODEMOS-COMPROMÍS-EUPV", "ERC-CATSÍ", "CDC", "PODEMOS-EN MAREA-ANOVA-EU", "EAJ-PNV", "EH Bildu", "CCa-PNC", "PACMA", "RECORTES CERO-GRUPO VERDE", "UPyD", "VOX", "BNG-NÓS", "PCPE", "GBAI", "EB", "FE de las JONS", "SI", "SOMVAL", "CCD", "SAIn", "PH", "CENTRO MODERADO", "P-LIB", "CCD-CI", "UPL", "PCOE", "AND", "JXC", "PFyV", "CILUS", "PxC", "MAS", "IZAR", "UNIDAD_DEL_PUEBLO", "PREPAL", "Ln", "REPO", "INDEPENDIENTES-FIA", "ENTABAN", "IMC", "PUEDE", "FE", "ALCD", "FME", "HRTS-Ln","UDT"]

# DROPING COLUMNS WITH PARTY NAMES
catalonia = catalonia.drop((parties), axis="columns")
catalonia = catalonia.drop([catalonia.columns[1]],axis="columns")
catalonia = catalonia.rename(columns = {"re_id":"prov_id"})
catalonia = catalonia.drop(["provinces"], axis="columns")

# DROPING COLUMNS OF THE PARTIES THAT DID NOT JOIN THE ELECTIONS
for i in range(len(parties)):
    if sum(catalonia[parties[i]+"_per"]) == 0:
        catalonia = catalonia.drop([parties[i]+"_per"], axis="columns")

# READING FILES
spain = pd.read_csv("final_spanish_regions.csv")
cat_mod = pd.read_csv("modified_cat_1.csv")

# CREATING DATAFRAME CALLED regin_ages
region_ages = spain.loc[:,['RegionName','Age_20-24_Ptge', 'Age_25-29_Ptge', 'Age_30-34_Ptge', 'Age_35-39_Ptge',
       'Age_40-44_Ptge', 'Age_45-49_Ptge', 'Age_50-54_Ptge', 'Age_55-59_Ptge',
       'Age_60-64_Ptge', 'Age_65-69_Ptge', 'Age_70-74_Ptge', 'Age_75-79_Ptge',
       'Age_80-84_Ptge', 'Age_85-89_Ptge', 'Age_90-94_Ptge', 'Age_95-99_Ptge']]

# RENAME SOME COLUMNS
region_ages = region_ages.rename(columns={"RegionName":"municipalities"})

# READING A FILE AND DROPING UNNECESSARY COLUMNS
result = pd.read_csv("query_result.csv")
result = result.drop(["cade","code"], axis="columns")

# SUMMING UP THE PERCENTAGES ACCORDING TO AGES
result["Age_20-34"] = result["Age_20-24_Ptge"] + result["Age_25-29_Ptge"] +result["Age_30-34_Ptge"]
result["Age_35-49"] = result["Age_35-39_Ptge"] + result["Age_40-44_Ptge"] +result["Age_45-49_Ptge"]
result["Age_50-64"] = result["Age_50-54_Ptge"] + result["Age_55-59_Ptge"] +result["Age_60-64_Ptge"]
result["Age_65-79"] = result["Age_65-69_Ptge"] + result["Age_70-74_Ptge"] +result["Age_75-79_Ptge"]

# LIST OF COLUMNS NEEDS TO BE DELETED
delete_years = ['abs_rate','code.1', 'Age_20-24_Ptge', 'Age_25-29_Ptge', 'Age_30-34_Ptge', 'Age_35-39_Ptge',
       'Age_40-44_Ptge', 'Age_45-49_Ptge', 'Age_50-54_Ptge', 'Age_55-59_Ptge',
       'Age_60-64_Ptge', 'Age_65-69_Ptge', 'Age_70-74_Ptge', 'Age_75-79_Ptge',
       'Age_80-84_Ptge', 'Age_85-89_Ptge', 'Age_90-94_Ptge', 'Age_95-99_Ptge']

# DROPING COLUMNS
result = result.drop((delete_years), axis="columns")

# UPLOADING FILES TO DATABASE
driver = 'mysql+pymysql:'
user = 'root'
password = 'ironhack'
ip = '35.241.205.10'
database = 'population_project'

connection_string = f'{driver}//{user}:{password}@{ip}/{database}'
engine = create_engine(connection_string)

result.to_sql("MUN_POL_AGE", engine)
municipalities.to_sql("MUN_ID_TABLE",engine)


# SOME EDITTING FIXING THE INDEX
municipalities["muni_id"] = list(range(1,948))
municipalities = municipalities.drop(["mun_id"], axis="columns")
municipalities = municipalities[["muni_id", "municipalities", "prov_id"]]
print(municipalities.columns)

municipalities.to_sql("MUN_ID_TABLE_1",engine)

mun_pol = pd.read_csv("mun_pol_age.csv")
mun_pol["muni_id"] = list(range(1,948))
mun_pol = mun_pol.drop(["mun_id"], axis="columns")

new_order = ['index', 'muni_id', 'municipalities', 'prov_id', 'poblacion', 'v_census',
       't_votes', 'votes_rate', 'PP_per', 'PSOE_per', 'Cs_per', 'ECP_per',
       'ERC-CATSÍ_per', 'CDC_per', 'PACMA_per',
       'RECORTES CERO-GRUPO VERDE_per', 'VOX_per', 'PCPE_per', 'PxC_per',
       'Age_20-34', 'Age_35-49', 'Age_50-64', 'Age_65-79']


mun_pol = mun_pol[new_order]
mun_pol = mun_pol.drop(["index"], axis="columns")

connection_string = f'{driver}//{user}:{password}@{ip}/{database}'
engine = create_engine(connection_string)

mun_pol.to_sql("MUN_POL_AGE_2",engine)