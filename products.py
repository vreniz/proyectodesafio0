#PRODUCT MANAGEMENT MODULE
# Este módulo se encarga de:
# - Registrar productos
# - Mostrar la lista de productos



# FUNCTION: REGISTER PRODUCT
# Esta función agrega un nuevo producto al sistema
def register_product(products_dict, product_id, name, price):
    if product_id in products_dict:
        return  "Product already exists" # Verifica si el producto ya existe (evita duplicados)

    products_dict[product_id] = (name, price)  # Guarda el producto como una tupla (nombre, precio)     # Ejemplo: ( "Laptop", 2000 )
    return  "Product registered successfully"    # Ejemplo: ( "Laptop", 2000 )

# FUNCTION: VIEW PRODUCTS
# =========================================
# Esta función muestra todos los productos registrados

def view_products(products_dict):
    if not products_dict:
        return "No products registered" # Si no hay productos, retorna mensaje

    result = "\n--- PRODUCT LIST ---\n"  # Encabezado del listado

    for product_id in products_dict:  # Recorre todos los productos en el diccionario
        product = products_dict[product_id]   # Obtiene el producto (tupla: nombre, precio)   # product[0] → nombre ; # product[1] → precio
        result += f"ID: {product_id} | Name: {product[0]} | Price: $ {product[1]}\n" # Agrega la información al resultado

    return result # Agrega la información al resultado