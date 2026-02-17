# try:
#     with open(r"zsample_file.txt", 'r') as file:
#         file.read()
# except : # Learn't a trick that if you don't know the exact error to catch better put nothing like this.
#     print("File doesn't exist")


try:
    with open(r"zsample_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    with open(r"sample.txt", "w") as new_file:
        new_file.write("I am new text here -> updated now.")
