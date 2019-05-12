#pour ce projet nous avons decider d utiliser pandas
import pandas as pd
#charger les donnes aui se trouvent dans eleves.xlsx
donne=pd.read_excel('eleves.xlsx')
print(donne)
eleves_ayant_plus20ans=donne[donne['Age'] > 20 ]
print(eleves_ayant_plus20ans)
writer = pd.ExcelWriter('eleve_ayant_plus20ans.xlsx', engine='xlsxwriter')
eleves_ayant_plus20ans.to_excel(writer, 'Sheet1',index = False)
writer.save()


