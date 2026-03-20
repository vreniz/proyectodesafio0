#Order Manager

This program is designed to register and manage orders, clients, and sales reports.  
It uses dictionaries to store information, and organizes the code into modules.  
Navigation is handled through a menu, where you can select the desired action.

##Features

1.Client Registration
   -Register clients using their ID, first name, last name, and email.  
   -Once registered successfully, the program confirms the entry.

2.Product Registration**  
   -Register products with the following details: product_ID, product_name, and unit_price.  
   -Information is stored in tuples for easy access.

3.Order Creation  
   -Create orders using previously registered clients and products.  
   -Add the product quantity to calculate the total price (unit_price × quantity).  

4.View Orders  
   -Use the view_order function to consult registered orders.  
   -If the requested information is not found in the dictionaries, the program shows a “No order registered” message.  
   -Otherwise, it lists all registered orders.

5.Daily Income Calculation
   -The program calculates daily income using the calculate_income function.  
   -It sums the total of all registered orders.

6.Sales Report  
   -Generates a complete report including:  
    -Total registered orders  
    -Client orders  
    -Quantity of items sold  
    -Reports are clearly labeled with titles using comments (`#`) in the code.
