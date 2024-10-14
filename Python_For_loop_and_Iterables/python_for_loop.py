# Remembering for loops.

fruits = ["apple", "orange", "banana"]

# for i in fruits:
#     a = fruits[-1]
# print(a)

countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi", "South Sudan"]

for country in countries:
    if country.startswith("S"):
        print(country)

developers = {"Alinda", "Brian", "Sandra", "Adamouh", "Ham"}
# for dev in developers:
#     print(f"{dev} is {len(dev)} characters long")

currencies = ("Euro", "UGX", "KSH", "TSH", "dollar")
for currency in currencies:
    if currency.isupper():
        print(currency)


email = "alindafortunate5@gmail.com"
for email in email:
    splitted_email = email.split("@")
    # print(splitted_email, end="")
