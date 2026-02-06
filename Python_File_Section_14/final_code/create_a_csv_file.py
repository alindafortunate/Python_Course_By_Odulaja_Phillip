import csv

data = [
    ["Product", "Category", "Quantity"],
    ["Mango", "Fruit", "10"],
    ["Phone", "Electronics", "12"],
    ["Dress", "Clothes", "1"],
]
with open("data_file2.csv", "w") as data_file:
    csv.writer(data_file).writerows(data)


# reading the file contents
with open('data_file2.csv', 'r') as data_file:
    csv.reader(data_file)
    for row in csv.reader(data_file):
        print(row)