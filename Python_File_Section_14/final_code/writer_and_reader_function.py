# Working with CSV files
import csv

data = [
    ["Name", "Age", "Location"],
    ["Alinda", "28", "Rukungiri"],
    ["Fortunate", "27", "Kibaale"],
    ["Ali", "29", "Kagadi"],
]

# # using the writer function on csv files
# with open("data.csv", "w") as data_file:
#     writer = csv.writer(data_file)
#     writer.writerows(data)
#     writer.writerow(["Annet", "24", "Hoima"])

# Using the reader function on csv files
with open("data.csv", "r") as data_file:
    reader = csv.reader(data_file)
    for row in reader:
        print(row)
