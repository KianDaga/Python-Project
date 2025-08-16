from prettytable import from_csv
with open("pokemonlist.csv") as fp:
    table = from_csv(fp)
table.align = "l"
print(table.get_string(sortby="Pokemon Name"))