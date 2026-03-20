# =========================================
# IMPORTS (Importación de módulos)
# =========================================
# Traemos funciones de otros archivos para mantener el código organizado (modularidad)
from clients import register_client, view_clients
from products import register_product, view_products
from orders import create_order, view_orders, calculate_income
from reports import generate_report
from validationfunct import input_int, input_float,input_string,input_name,input_email

# =========================================
# IN-MEMORY DATABASE (Almacenamiento en memoria)
# =========================================
# Diccionarios donde se almacenan los datos durante la ejecución del programa

clients = {}   # Guarda clientes
products = {}  # Guarda productos
orders = {}    # Guarda pedidos

# =========================================
# VALIDATION FUNCTIONS
# =========================================
"""
def input_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Invalid input. Please enter a valid integer.")
        
def input_float(prompt):
    while True:
        value = input(prompt).strip()

        # Replace comma with dot
        value = value.replace(",", ".")

        # ❌ validar que no haya más de un punto
        if value.count(".") > 1:
            print("Invalid format. Too many decimal points.")
            continue

        # ❌ validar que no esté vacío o solo punto
        if value == "." or value == "":
            print("Invalid number.")
            continue

        # ❌ validar que solo tenga números y punto
        valid = True
        for char in value:
            if not (char.isdigit() or char == "."):
                valid = False

        if not valid:
            print("Invalid input. Only numbers allowed.")
            continue

        # convertir a float
        number = float(value)

        # ❌ validar positivo
        if number <= 0:
            print("Value must be greater than 0.")
            continue

        return number

def input_string(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("This field cannot be empty.")


def input_name(prompt):
    
    #Only allows letters and spaces
    
    while True:
        value = input(prompt).strip()

        if value.replace(" ", "").isalpha():
            return value.title()
        else:
            print("Invalid name. Only letters are allowed.")
"""

# =========================================
# CONTINUE FUNCTION (Control de flujo)
# =========================================
# Esta función pregunta al usuario si desea volver al menú o salir del programa

def ask_to_continue():
    while True:
        answer = input("\nReturn to menu? (yes/no): ").strip().lower()

        if answer == "yes":
            return True
        elif answer == "no":
            print("Goodbye!")
            return False
        else:
            print("Invalid option. Please type 'yes' or 'no'.")


# =========================================
# MENU (Interfaz principal)
# =========================================
# Controla toda la interacción con el usuario

def menu():
    running = True # Variable de control del ciclo principal

    while running:
         # Mostrar menú de opciones
        print("\n===== MENU =====")
        print("1. Register Client")
        print("2. Register Product")
        print("3. Create Order")
        print("4. View Orders")
        print("5. Calculate Income")
        print("6. Generate Report")
        print("7. View Clients")
        print("8. View Products")
        print("9. Exit")
        
        # Leer opción del usuario
        option = input("Select an option: ").strip()

        # 
        # =========================================
        # OPTION 1: REGISTER CLIENT
        # =========================================
        if option == "1":
            client_id = input_int("Client ID: ")
            first_name = input_name("First Name: ")
            last_name = input_name("Last Name: ")
            email = input_email("Email: ")

             # Se registra el cliente
            msg = register_client(clients, client_id, first_name, last_name, email)
            print(msg)
            # Se pregunta si desea continuar
            running = ask_to_continue()

        # 
        # =========================================
        # OPTION 2: REGISTER PRODUCT
        # =========================================
        elif option == "2":
            product_id = input_int("Product ID: ")
            name = input_string("Name: ")
            price = input_float("Price: $ ")

            
            msg = register_product(products, product_id, name, price)
            print(msg)

            running = ask_to_continue()

        # 
        # =========================================
        # OPTION 3: CREATE ORDER
        # =========================================
        elif option == "3":
            order_id = input_int("Order ID: ")
            client_id = input_int("Client ID: ")
            product_id = input_int("Product ID: ")
            quantity = input_int("Quantity: ")

            # Se crea el pedido validando existencia de cliente y producto
            msg = create_order(
                orders, order_id, client_id, product_id, quantity, clients, products
            )
            print(msg)

            running = ask_to_continue()

        # VIEW ORDERS
        elif option == "4":
            print(view_orders(orders, clients, products))
            running = ask_to_continue()

        # CALCULATE INCOME
        elif option == "5":
            print(f"Total Income: {calculate_income(orders)}")
            running = ask_to_continue()

        # GENERATE REPORT
        elif option == "6":
            print(generate_report(orders, clients, products))
            running = ask_to_continue()

        # VIEW CLIENTS
        elif option == "7":
            print(view_clients(clients))
            running = ask_to_continue()

        # VIEW PRODUCTS
        elif option == "8":
            print(view_products(products))
            running = ask_to_continue()

        # EXIT
        elif option == "9":
            print("Goodbye!")
            running = False # Finaliza el programa

        else:
            print("Invalid option")


# =========================================
# MAIN (Punto de entrada del programa)
# =========================================
# Esta condición asegura que el programa se ejecute solo si este archivo es el principal
if __name__ == "__main__":
    menu()