#make a list called things with these three strings as elements: 'mozzarella', 'cinderella','salmonella'
things = ['mozzarella', 'cinderella', 'salmonella']
#capitalize the element in things that refers to a person, then print
things[1] = things[1].capitalize()
print(things)
#make the cheesy element of things all uppercase and print list
things[0]= things[0].upper()
print(things)
#delete the disease element and print list
things.remove('salmonella')
print(things)