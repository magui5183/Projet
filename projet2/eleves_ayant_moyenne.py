#pour ce projet nous avons decider d utiliser pandas
#Pandas est une librairie Python spécialisée dans l’analyse des données
##Première étape : il faut charger la librairie Pandas
import pandas as pd
#charger les donnes aui se trouvent dans eleves.xlsx
#donne est le nom de l'objet de type data frame créé
donne=pd.read_excel('eleves.xlsx')
print(donne)
#extraire les eleves ayant une moyenne c-a-d une moyenne superieure ou egale a 10
eleves_ayant_moyenne=donne[donne['Moyenne'] >= 10 ]
writer = pd.ExcelWriter('eleve_ayant_moyenne.xlsx', engine='xlsxwriter')
# Enregistre dans la feuille sheet1 et non indexe
eleves_ayant_moyenne.to_excel(writer, 'Sheet1',index = False)
## enregistre le fichier excel .
writer.save()


