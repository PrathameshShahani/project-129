import csv

dataset_1=[]
dataset_2=[]

with open("bright_stars.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        dataset_1.append(i)

with open("converted.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        dataset_2.append(i)

headers_1=dataset_1[0]
headers_2=dataset_2[0]

star_data1=dataset_1[1:]
star_data2=dataset_2[1:]

headers=headers_1+headers_2
star_data=[]

for index,data_row in enumerate(star_data1):
    star_data.append(star_data1[index]+star_data2[index])

with open("total_stars.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)