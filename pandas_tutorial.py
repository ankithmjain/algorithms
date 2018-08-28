import pandas as pd
import numpy as np
file_to_load = "Resources/purchase_data.csv"
purchase_data = pd.read_csv(file_to_load, names=["SN","ID","Age","Gender", "Item ID", "Item Name","Price"],
                            sep=',', encoding='utf8')

df = pd.DataFrame()
#print(purchase_data)
#,"Age","Gender","Item ID","Item Name"
Total = purchase_data['Price'].sum()

print("Total is ", Total)


#names = ['Bob','Jessica','Mary','John','Mel']
#births = [968, 155, 77, 578, 973]
#BabyDataSet = list(zip(names, births))

#df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

#df.to_csv('Resources/births1880.csv')