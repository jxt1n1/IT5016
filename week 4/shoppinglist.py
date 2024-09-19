"""
Shopping list to cal...
author: jatin
"""
 
def get_shoppinglist():
    shopping_list = [] #it is a list that stores values
    total_price = 0
    while True:
        item = input("Enter the name of the item(or type 'done' to finish):")
        if item.lower() == 'done':
            break
        try:
            price = float(input(f"Enter the price of '{item}':"))
            shopping_list.append((item,price))
            total_price += price
        except ValueError:
            print("invalid input. please enter a numeric value for price")
 
        return shopping_list,total_price
 
def main():
    print("welcome to theshopping list program")
    shopping_list, total_price = get_shoppinglist()
 
    if not shopping_list:
        print("no items were entered")
    else:
        print("\nshopping list")
        for item, price in shopping_list:
            print(f"(item),$(price:.2f")
        print(f"\ntotal price: $(total_price:.2f")
 
main()