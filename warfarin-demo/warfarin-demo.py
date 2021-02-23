import os
import json
from pandas.core.frame import DataFrame

drugs_ddi_path = '/data/DrugData/Drugs/data/'
warfarin_path = drugs_ddi_path + 'Warfarin/Warfarin_inter.json'

ddi_list = []
ddi_list_check = []
drug_list = []

with open(warfarin_path,'r') as load_f:
     warfarin_dict = json.load(load_f)

inter_list = warfarin_dict['Drug Interactions']['inter_list']
for i in inter_list:
     drug_list.append(i[1])
     ddi_list.append(['warfarin', i[1], i[0]])
     
g = os.walk(drugs_ddi_path)  
for path,dir_list,file_list in g:  
     for dir_name in dir_list:
          if(dir_name.lower() in drug_list):
               drug_ddi_file = os.path.join(path, dir_name) + '/' + dir_name + '_inter.json'
               try:
                    with open(drug_ddi_file,'r') as load_drug:
                         drug_dict = json.load(load_drug)        
                         for i in drug_dict['Drug Interactions']['inter_list']:
                              if(i[1] in drug_list):
                                   new_list = [dir_name.lower(), i[1]]
                                   new_list.sort()
                                   
                                   if(new_list in ddi_list_check):
                                        continue
                                   else:
                                        ddi_list_check.append(new_list)
                                        ddi_list.append([dir_name.lower(), i[1], i[0]])    
                                   
               except FileNotFoundError:
                    pass

data = DataFrame(ddi_list)
data.to_csv("warfarin_ddi.csv")