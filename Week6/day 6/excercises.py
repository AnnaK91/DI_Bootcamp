# 1.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
keys_dictionary = dict(zip(keys, values))

# 3

#  "brand": "Ford",

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": "men, women, children, home",
    "international_competitors": "Gap, H&M, Benetton",
    "number_stores": 7000,
    "major_color": "France -> blue, Spain -> red, US -> pink, green"
}

brand["number_stores"] = 2

print("The customers of Zara are:", brand["type_of_clothes"])

brand["country_creation"] = "Spain"

# 5

if "international competitors" in brands:
    brand["store:"] = "Desigual"

    # It doesnt work, so I am gessing this is not the solution...

    del brand["creation_date"]

    



