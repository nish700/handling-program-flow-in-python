# --------------
#  Read the data of the format .yaml type
import json


# using with open command to read the file

with open(path) as stream:
    nobel_dict = json.load(stream)

#  Women who got the first Nobel Prize?

for dict in nobel_dict:
    if dict['Sex'] == 'Female':
        print("First Nobel prize to a women went to :", dict['Full Name'])
        break;

#  How many have come from india?
birth_country = 0
org_country = 0
india_list = []

for dict in nobel_dict:
    if dict['Organization Country'] == "India":
        org_country += 1
    if dict['Birth Country'] == 'India':
        birth_country += 1
        india_list.append(dict)

print('India produced :', birth_country)

#  Calculate category wise number of prizes for the people who came from India?
ind_category_list = []
ind_category_dist = {}

for dict in india_list:
    if dict['Category'] not in ind_category_list:
        ind_category_list.append(dict['Category'])
        ind_category_dist['Category'] = 1
    else:
        ind_category_dist['Category'] += 1

print('category wise for india',ind_category_dist)

#   Which country has produced the highest number of Nobel winners for category `Chemistry`?
import operator

country_list =[]
chem_dict = {}

for dict in nobel_dict:
    if dict['Category'] == 'Chemistry':
        if dict['Birth Country'] not in country_list: 
            country_list.append(dict['Birth Country'])
            chem_dict[dict['Birth Country']] = 1
        else:
            chem_dict[dict['Birth Country']] += 1

print('highest number of nobel winners for chemistry ', max(chem_dict.items(), key=operator.itemgetter(1)))


#  Which Organization won the most nobel prizes in the category "Physics" and "Chemistry" ?
org_physics = []
org_chemistry = []
org_phy_dict = {}
org_che_dict = {}

for dict in nobel_dict:
    if dict['Category'] == 'Physics':
        if dict['Organization Name'] not in org_physics:
            org_physics.append(dict['Organization Name'])
            org_phy_dict[dict['Organization Name']] = 1
        else:
            org_phy_dict[dict['Organization Name']] += 1
    
    if dict['Category'] == 'Chemistry':
        if dict['Organization Name'] not in org_chemistry:
            org_chemistry.append(dict['Organization Name'])
            org_che_dict[dict['Organization Name']] = 1
        else:
            org_che_dict[dict['Organization Name']] += 1

print('Organization with most numbers in physics ', max(org_phy_dict.items(), key=operator.itemgetter(1)))
print('Organization with most numbers in chemistry ', max(org_che_dict.items(), key = operator.itemgetter(1)))

#  What was the Motivation for awarding the Nobel Prize for Marie Curie, nÃ©e Sklodowska?
for dict in nobel_dict:
    if dict['Full Name'] == 'Marie Curie, née Sklodowska':
        print(dict['Motivation'])

#  In which category people got Noble Prize in the year 1994?

for dict in nobel_dict:
    if dict['Year'] == 1994:
        print(dict['Category'], "-" , dict['Full Name'])


