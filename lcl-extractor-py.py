# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:43:52 2023

@author: Max-Bld
"""

#%% 1. IMPORT

import tabula as tb
import pandas as pd
import os

#%% 2. SCRAPE

#List of each file path


base_path=input("Path directory containing the bank statements:\n")

if base_path=='':
    base_path = "C:\\"
else :
    pass

file_list=[]

for path in os.listdir(base_path):
    if os.path.isfile(os.path.join(base_path, path)) and ((path.startswith("COMPTEDEDEPTS_"))):
        file_list.append(base_path+path)
        

#List of lists of dfs

all_names=[]
all_data=[]
for f in file_list:
    data=tb.read_pdf(f, multiple_tables=True, pages='all')
    data.pop(-1) #the last tabular in the pdf is useless
    name=f[-16:-8]
    all_names.append(name) #not used
    all_data.append(data)

#%%List of dfs

data_flat=[]
for sublist in all_data:
    for df in sublist:
        data_flat.append(df)
        
#%% 3. RIGHT HEADER

#New header with first row with exception 3(found in all)

for n in range(0, len(data_flat)):
    if any(data_flat[n].columns.str.contains('DATE'))==True:
       pass
    else :
        new_header=data_flat[n].iloc[0]
        data_flat[n]=data_flat[n][1:]
        data_flat[n].columns=new_header
 
    
#%% Handling exception 1 (found in 2021):

for n in range(0, len(data_flat)):
    if all(data_flat[n].columns.str.contains('ECRITURES'))==False:
        pass
    else:
        new_header=data_flat[n].iloc[0]
        data_flat[n]=data_flat[n][1:]
        data_flat[n].columns=new_header
        
#%% 4. RIGHT COLUMNS

#Handling exception 2 (found in 2020):

for n in range(0, len(data_flat)):
    if data_flat[n].columns[0]==('DATEK6EXTP25 LIBELLE'):
        data_flat[n].rename(columns={data_flat[n].columns[0]:'DATE LIBELLE'}, inplace=True)
    else:
        pass
        
#Rename Dfs col 'date' to 'date libelle'

for n in range(0, len(data_flat)):
    if data_flat[n].columns.any() == 'DATE':
        data_flat[n].rename(columns={'DATE':'DATE LIBELLE'}, inplace=True)
    else:
        pass
        
#Drop useless dfs off the list

data_dropped_0=[]

for n in range(0, len(data_flat)):
    if (len(data_flat[n].columns)>=4):
        data_dropped_0.append(data_flat[n])
    else:
        pass
        
#Drop useless unnamed columns

for n in range(0, len(data_dropped_0)):
    data_dropped_0[n]=data_dropped_0[n][['DATE LIBELLE', 'VALEUR', 'DEBIT', 'CREDIT']]

#Rename remaining columns

data_renamed=data_dropped_0

for n in range(0, len(data_renamed)):
    data_renamed[n].rename(columns=
                           {data_renamed[n].columns[0]:"objet", 
                            data_renamed[n].columns[1]:"date",
                            data_renamed[n].columns[2]:"debit",
                            data_renamed[n].columns[3]:"credit"},
                           inplace=True)
    
#%% 5. CONCATENATE

data_concat=pd.concat(data_dropped_0)

#%% 6. STANDARDIZATION

#%%% 6.1. CONVERT 'debit' AND 'credit' TO FLOAT64



data_rows_solde=data_concat

#standardize

data_rows_solde['debit']=data_rows_solde['debit'].str.replace(',', '.')
data_rows_solde['credit']=data_rows_solde['credit'].str.replace(',', '.')
data_rows_solde['debit']=data_rows_solde['debit'].str.replace(' ', '')
data_rows_solde['credit']=data_rows_solde['credit'].str.replace(' ', '')
  
#Convert to float

data_rows_solde['debit']=pd.to_numeric(data_rows_solde['debit'], errors='coerce')
data_rows_solde['credit']=pd.to_numeric(data_rows_solde['credit'], errors='coerce')

#%%% 6.2. STANDARDIZE 'objet'

#Delete numeric characters in 'objet'

data_rows_objet=data_rows_solde
data_rows_objet['objet']=data_rows_objet['objet'].str.replace("\d+", "")
data_rows_objet['objet']=data_rows_objet['objet'].str.replace("/", "")
data_rows_objet['objet']=data_rows_objet['objet'].str.replace(".", "")
data_rows_objet['objet']=data_rows_objet['objet'].str.replace(":", "")
data_rows_objet['objet']=data_rows_objet['objet'].str.replace("\n", "")

#Upper case objet

data_rows_objet['objet']=data_rows_objet['objet'].str.lower()

#%%% 6.3. CONVERT 'date' TO DATETIME64

#Replace . by /

data_time=data_rows_objet
data_time['date']=data_time['date'].str.replace('.','/')

#Convert to datetime

data_time['date']=pd.to_datetime(data_time['date'], format='%d/%m/%y', errors='coerce')

#%% 7. FILL None VALUES

data_filled=data_time

#Replace NaN by 0 in debit and credit cols

data_filled['debit']=data_filled['debit'].fillna(0)
data_filled['credit']=data_filled['credit'].fillna(0)

#%Replace NaT with the previous upper value

data_filled['date']=data_filled['date'].fillna(method='ffill')
data_filled['objet']=data_filled['objet'].fillna(method='ffill')

#%% 8. DELETE ROWS

#Delete rows containing 'solde' or 'totaux' in ['objet'] col

data_delete=data_filled
data_delete=data_delete[data_delete['objet'].str.contains("SOLDE")==False]

#Delete rows with both positive and negative

data_rows_pos_neg=data_delete[~((data_delete['debit'] > 0) & 
                      (data_delete['credit'] > 0))]

#Delete rows with redundant info

mask = (data_rows_pos_neg['objet'].str.len() == 5)
data_rows_last=data_rows_pos_neg.loc[~mask]

#%% 9. EXPORT

#Reset index

data_index=data_rows_last.reset_index(drop=True)

print(data_index.info())
print("Process Finished.")

#Export

data_index.to_csv(base_path + "comptes_full.csv")

#%% COMMENTS

#exception 1:
#exception 2: 
#exception 3: first line contains already "DATE" and columns name do not need to be changed
