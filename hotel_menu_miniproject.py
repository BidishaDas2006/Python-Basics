menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80
}

print("Welcome to PYTHON restaurant!")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80") 


total_cost=0
item=input("Please enter the item you want to order: ")
if item in menu:
    total_cost+=menu[item]
    print(f"your item {item} has been added to your order.")

else:
    print("please selct a valid item from the menu.")   


another_item=input("Do you want to order another item? (yes/no): ")
if another_item=="yes":
    item2=input("Please enter the item you want to order: ")
    if item2 in menu:
        total_cost+=menu[item2]

    else:
        print("please selct a valid item from the menu.")
print("Your total cost is Rs ",total_cost)
print("Thank you for dining with us!")
