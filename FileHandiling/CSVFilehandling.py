import csv
with open("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#writing to the csv file

with open("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//writecsv.csv", 'w',newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow([1,"Rahul",85])
    writer.writerow([2,"Ankita",90])

#appedding  the data to csv file
with open("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//data.csv", 'a',newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3,"Kiran",88])



