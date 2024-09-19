def shopping_list():
   print("Welcome to the Shopping List Program!")
   items = {}  # Dictionary to store items and their prices
   while True:
       # Ask for item name
       item_name = input("Enter the name of the item (or type 'done' to finish): ")
       if item_name.lower() == 'done':
           break
       # Ask for item price and ensure it's a valid number
       try:
           item_price = float(input(f"Enter the price of '{item_name}': "))
       except ValueError:
           print("Invalid price. Please enter a number.")
           continue
       # Store the item and its price in the dictionary
       items[item_name] = item_price
   # Print the shopping list
   print("\nShopping List:")
   for item, price in items.items():
       print(f"{item}: ${price:.2f}")
   # Calculate and print the total cost
   total_price = sum(items.values())
   print(f"\nTotal Price: ${total_price:.2f}")
# Run the shopping list function
shopping_list()