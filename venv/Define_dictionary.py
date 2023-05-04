# empty dictionaery
d={}

d = dict() # same thing

d = {1: "one", 2: "two"}
# The vaues are the numbers and the keys las palabras
print(d)

#english to spanish dictionary
eng_to_spa={
    "hello": "Hola", "yes": "si",
    "dictionary": "diccionario", "one": "uno", "two": "dos",
    "no": "no"

}
print(eng_to_spa, len(eng_to_spa))
print(f"two in spanish is {eng_to_spa ['two']}")
eng_to_spa["three"]= "tres" #this is how to add new keys
eng_to_spa["two"] = "Dos" #this is how you change a value

print("let me teach yo Spanish")
# i is all the keys
for i in eng_to_spa:
    print(f"{i} is {eng_to_spa[i]}")