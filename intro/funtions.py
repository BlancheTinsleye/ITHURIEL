import json

# function is creating a block of code and executes
# the code if the function is called

def add(num1, num2):
    # return num1 + num2
    print(num1 + num2)

def multiply(num1, num2):
    return num1 * num2

def iterate():
    items = ["pen", "paper", "eraser"]
    for item in items:
        print(item)
    # return None

def choose_min(num1, num2):
    return min(num1, num2)



# sum = add(4, 12)

# print(choose_min(2, 5))

# items = ["pen", "paper", "eraser"]
# print(iterate(items))
# iterate()
def add_element():
    # pass
    fruits = ["apple", "mango", "banana", "grape", "orange"]

    fruits.append("pineapple")
    print(fruits)

def get_products():
    with open("stocks.json", "r") as file:
        data = json.load(file)

    return data["products"]

def show_prices():
    products = get_products()

    print(products["products"])


    # products["max"] = 2
    # for key,val in products.items():
    #     print(f"product: {key} | price {val}")
    # print("\n") #new line
    # products["lollipop"] = 15

    # for key,val in products.items():
    #     print(f"product: {key} | price {val}")
    
def store():
    open = True
    products = get_products()

    while open:
        user_input = input("INPUT: ")
        user_input = user_input.lower()

        if user_input == "bye":
            break

        if user_input in products:
            print(f"Price of {user_input}: {products[user_input]}")
        else:
            print("No stock")

        print("\n")

    

store()
# show_prices()
# add_element()

