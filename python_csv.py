import csv

f1 = open("transactions.csv", "r", encoding="utf-8", newline="")

reader = csv.reader(f1)

total_of_category = 0

for row in reader:
    if(row[5] == 'Fast Food' and row[1] == "Wendy's"):
        print(row)
        total_of_category += float(row[3])

print("The total of the category is: " + str(total_of_category))

f1.close()
