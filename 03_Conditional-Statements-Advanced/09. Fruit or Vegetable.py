product_name = input()
fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetable = ["tomato", "cucumber", "pepper", "carrot"]
if product_name in fruits:
    print("fruit")
elif product_name in vegetable:
    print("vegetable")
else:
    print("unknown")
