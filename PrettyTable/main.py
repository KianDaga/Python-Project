from prettytable import PrettyTable 
table = PrettyTable()
table.field_names = [ '#', 'Pokemon Name', 'Type']
table.add_row([ '001', 'Bulbasaur', 'Grass/Poison'])
table.add_row([ '002', 'Ivysaur', 'Grass/Posison'])
table.add_row([ '003', 'Venusaur', 'Grass/Posison'])
table.add_row([ '004', 'Charmander', 'Fire'])
table.add_row([ '005', 'Charmeleon', 'Fire'])
table.add_row([ '006', 'Charizard', 'Fire/Flying'])
table.add_row([ '007', 'Squirtle', 'Water'])
table.add_row([ '008', 'Wartotle', 'Water'])
table.add_row([ '009', 'Blastpoise', 'Water'])
table.add_row([ '002', 'Caterpie', 'Bug'])
print(table)
with open('test.csv', 'w', newline='') as f_output:
    f_output.write(table.get_csv_string())