# ORDER MANAGEMENT MODULE
# =========================================
# Este módulo se encarga de:
# - Crear pedidos
# - Mostrar pedidos
# - Calcular ingresos

# FUNCTION: CREATE ORDER
# =========================================
# Esta función crea un nuevo pedido en el sistema
def create_order(orders_dict, order_id, client_id, product_id, quantity, clients_dict, products_dict):
    if order_id in orders_dict: # Verifica si el pedido ya existe (evita duplicados)
        return  "Order already exists" # Verifica si el pedido ya existe (evita duplicados)

    if client_id not in clients_dict:  # Verifica que el cliente exista
        return  "Client does not exist"

    if product_id not in products_dict:  # Verifica que el producto exista
        return  "Product does not exist"

     # Obtiene el precio del producto
     # products_dict[product_id] → (name, price)
     # [1] → precio
    unit_price = products_dict[product_id][1]
    total = unit_price * quantity  # Calcula el total del pedido

    orders_dict[order_id] = { # Guarda el pedido en el diccionario
        "client": client_id, # ID del cliente
        "product": product_id,# ID del producto
        "quantity": quantity, # ID del cliente
        "total": total #Total a pagar 
    }

    return  "Order created successfully" # retorna mensaje de exito

# FUNCTION: VIEW ORDERS
# =========================================
# Esta función muestra todos los pedidos registrados
def view_orders(orders_dict, clients_dict, products_dict):
    if not orders_dict:  # Si no hay pedidos, retorna mensaje
        return "No orders registered" 

    result = "\n--- ORDER LIST ---\n"   # Encabezado del listado

    for order_id in orders_dict: # Recorre todos los pedidos
        order = orders_dict[order_id] # Obtiene el pedido

        client = clients_dict[order["client"]]# Obtiene información del cliente
        client_name = client["first_name"] + " " + client["last_name"]   #   # Obtiene información del cliente
        product_name = products_dict[order["product"]][0]   # Obtiene el nombre del producto

        result += ( # Obtiene el nombre del producto
            f"Order ID: {order_id} | "
            f"Client: {client_name} | "
            f"Product: {product_name} | "
            f"Qty: {order['quantity']} | "
            f"Total: {order['total']}\n"
        )

    return result   # Retorna el listado completo

# FUNCTION: CALCULATE INCOME
# =========================================
# Esta función calcula el total de ingresos generados

def calculate_income(orders_dict):
    total_income = 0    # Inicializa el total en 0
    
    for order_id in orders_dict: # Recorre todos los pedidos
        total_income += orders_dict[order_id]["total"] # Suma el total de cada pedido

    return total_income # Retorna el ingreso total