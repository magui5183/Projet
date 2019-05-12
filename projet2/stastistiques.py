# -*- coding: utf-8 -*-
#pour ce projet nous aavons decider d utiliser pandas
import pandas as pd
import numpy as np
#charger les donnes aui se trouvent dans eleves.xlsx
donne=pd.read_excel('eleves.xlsx')
print(donne)
#calculer explicitement la moyenne de la classe
moyenne_ecole=donne['Moyenne'].mean()

 #comptage des valeurs
donne['Sexe'].value_counts()
#extraire le nombre de fille
femelle=donne['Sexe'].value_counts()[0]
#extraire le nombre de garcons
male=donne['Sexe'].value_counts()[1]
#calculer la totale
total=femelle+male
#pourcentage fille
pourcentageFemelle=(femelle/total)*100
#pourcentage garcon
pourcentageMale=(male/total)*100

#extraire eleve ayant plus grande  moyenne
grandeMoyenne=donne[donne['Moyenne']== donne['Moyenne'].max()]
# extraire la region de l eleve seulement
grandeMoyenneRegion=grandeMoyenne['Region']
region = np.array(grandeMoyenneRegion) 
region=region[0]

# Create a Pandas dataframe from the data.
donne = pd.DataFrame({
                      'Moyenne': [moyenne_ecole],
                      'Pourcentage fille': [pourcentageFemelle],
                      'Pourcentage garcon': [pourcentageMale],
                      'Region':[region]
                      
                     })

# Creer un Pandas Excel writer utilisant XlsxWriter as the engine.
writer = pd.ExcelWriter('statistique.xlsx', engine='xlsxwriter')

# Convertir  dataframe to an XlsxWriter Excel object.
donne.to_excel(writer, sheet_name='Sheet1',index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

