

import pandas

data=pandas.read_csv("day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231023.csv")


gray=len(data[data["Primary Fur Color"]
=="Gray"])
black=len(data[data["Primary Fur Color"]
=="Black"])
cinnamon=len(data[data["Primary Fur Color"]
=="Cinnamon"])


data_dict={
    "Fur Color":["Gray","Black","Cinnamon"],
    "Count":[gray,black,cinnamon]
}

print(data_dict)

data = pandas.DataFrame(data_dict)
data.to_csv("new_color1.csv", index=False)

#to list
# temp_list= data["Temp"].to_list()

#max temp row
# max_temp=data.temp.max()
# print(data[data.temp == max_temp]) 

# monday = data[data.day=="Monday"]

# print((monday.temp * 9/5) + 32 )

# dict_data={
#     "Name":["Salsabeel","Ibrahim","Alhad","Ehfat"]
#     ,"Phone":[823423424,5549854,54462665,123244487]
# }

# data = pandas.DataFrame(dict_data)
# data.to_csv("new_contact.csv", index=False)

#by using csv
# import csv
# with open("day 25/temp.csv",newline='') as file:
#     data=csv.reader(file)
#     temp_list=[]
#     next(data)
#     for row in data:
#         temp=int(row[1])
#         temp_list.append(temp)
# print(temp_list)