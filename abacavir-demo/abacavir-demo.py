import os
import json
from pandas.core.frame import DataFrame

drugs_ddi_path = '/data/DrugData/Drugs/data/'
warfarin_path = drugs_ddi_path + 'Abacavir/Abacavir_inter.json'

ddi_list = []
ddi_list_check = []
drug_list = []

with open(warfarin_path,'r') as load_f:
    warfarin_dict = json.load(load_f)

inter_list = warfarin_dict['Drug Interactions']['inter_list']
for i in inter_list:
    drug_list.append(i[1])
    ddi_list.append(['abacavir', i[1], i[0]])

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
data.to_csv("abacavir_ddi.csv")

drug_dict = {}
drug_dict['abacavir'] = 0
for i in range(0,len(drug_list)):
    drug_dict[drug_list[i]] = i

new_drug_list = []
new_drug_list.append('abacavir')
for i in drug_list:
    new_drug_list.append(i)
pd1_list = []
pd2_list = []
for i in ddi_list:
    pd1_list.append([drug_dict[i[0]], drug_dict[i[1]], i[2]])
label_list = []
label_list.append(1)
for i in drug_list:
    label_list.append(0)
for i in range(0,len(new_drug_list)):
    pd2_list.append([new_drug_list[i], label_list[i], label_list[i]])

pd1 = DataFrame(pd1_list)
pd2 = DataFrame(pd2_list)
pd1.to_csv("abacavir_pd1.csv")
pd2.to_csv("abacavir_pd2.csv")