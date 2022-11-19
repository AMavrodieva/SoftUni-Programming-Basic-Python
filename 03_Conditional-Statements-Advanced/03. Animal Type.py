kind_of_animal = input()
if kind_of_animal == "dog":
    print("mammal")
elif kind_of_animal == "crocodile" or kind_of_animal == "tortoise" \
        or kind_of_animal == "snake":
    print("reptile")
else:
    print("unknown")
