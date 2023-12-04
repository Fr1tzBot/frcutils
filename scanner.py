DATABASE = "./database.csv"
#database format:
#Barcode, Stock Level, Image, Name, Category, Description, Quantity, Container

def checkItem(code: str) -> bool:
    #check if item barcode is in database
    with open(DATABASE) as f:
        for line in f:
            if code in line:
                return True
            
def addItem(code: str, name: str, category: str, description: str, quantity: int, container: str):
    #add item to database
    with open(DATABASE, "a") as f:
        f.write(f"{code}, , , {name}, {category}, {description}, {quantity}, {container}\n")
    

while True:
    code = input()
    #remaining code will only run when a code is scanned
    if code == "exit" or type(code) != str or code is None or code == "": #filter out invalid inputs
        break

    if checkItem(code):
        print("Item found!")
        #get item info from database
        with open(DATABASE) as f:
            for line in f:
                if code in line:
                    item = line.split(", ")
                    name = item[3]
                    category = item[4]
                    description = item[5]
                    quantity = item[6]
                    container = item[7]
                    print(f"Name: {name}")
                    print(f"Category: {category}")
                    print(f"Description: {description}")
                    print(f"Quantity: {quantity}")
                    print(f"Container: {container}")
                    break
    else:
        print("Item not found in database")
        name = input("Enter name: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        quantity = int(input("Enter quantity: "))
        container = input("Enter container: ")
        #add item to database
        addItem(code, name, category, description, quantity, container)
        print("Item added to database")