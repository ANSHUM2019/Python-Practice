print("""
This
is 
multiline""")

Escape Characters
\  :Allows to creare a new line in multiline string
\\ :Inclusion of back slash in a string
\n :Creating a line break
\t :Creates a tab or an indendation
\' :single quotes
\" :Double quotes

superpowers = ['flight', 'Cool Cape', '20/20 Vision']
print(superpowers)
print(*superpowers) # Concatenates the List content
print(superpowers[0])
superpowers.append()
superpowers.pop([index]) #pop out the value and Deletes it form the source
superpowers.insert(1, 'Taco Meat')
del superpowers[1]
superpowers.remove('flight')
superpowers.reverse()
superpowers.copy() # Returns all the element of the List
superpowers.index('flight') # Returns the index of the element
superpowers.clear()
superpowers.count(<Value>)
superpowers[1].count('o')
superpowers[1].count('o',1,2)# Sustring, start, Last index


