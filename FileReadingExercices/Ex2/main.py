def print_countries_and_capitals(filename):
    with open(filename, "r") as file:
        line = file.readline()
        while line:
            country, capital = line.strip().split(", ")
            line = file.readline()
            print(f"The Capital of {country} is {capital}")
            
            #Specify the path to the file with countries and capitals
filename = 'countries_and_capitals.txt'

# Call the function with the filename
print_countries_and_capitals(filename)
