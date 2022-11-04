import csv

with open("adress.csv", "w+") as csvfile:
    myfile= csv.writer(csvfile)
    myfile.writerow(["firstname","lastname","klass"])
    firstname = input("pls write down your firstname")
    lastname = input("pls write down your lastname")
    klass = input("pls write down your klass")
    myfile.writerow([firstname, lastname, klass,])

with open("adress.csv", "r") as csvfile:
    myfile1= csv.reader(csvfile)
    for  row in myfile1:
        print(row)

