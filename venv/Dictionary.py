import random

eng_to_spa = {
    "hello": "Hola", "yes": "si",
    "dictionary": "diccionario", "one": "uno", "two": "dos",
    "no": "no"

}
# to delete something in the dic
#del(eng_to_spa["Hello"])
if "hello" in eng_to_spa:
    print("I know to say hello in spanish")
else:
    print("I do not know how to say hello in spanish")

print(list(eng_to_spa.values()))
print(list(eng_to_spa.keys()))
print(f"Word of the day: ", random.choice(list(eng_to_spa.values())))

random_word = random.choice(list(eng_to_spa.keys()))
answer = input(f"How do you say {random_word} in Spanish? ")
if answer == eng_to_spa[random_word]:
    print("Well done")
    