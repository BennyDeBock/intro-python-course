"""
Assigning variables

We create a few variables and print them in a sentence
"""
country = "Belgium"
city = "Ghent"
postcode = 9000
address = "Klein Turkije 8"

print("The comic sans is located in ", country, " in the municipality of ", city, ". The address is ", address)


"""
Checking datatypes

Sometimes we can't be sure about the datatype we're working with. Hence it's handy to figure this out with some code
"""
a = "15"
b = 9

c = a + str(b)
d = int(a) - b

print(c, ". Type is ", type(c))
print(d, ". Type is ", type(d))
