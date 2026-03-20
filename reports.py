from orders import calculate_income # Importa función para calcular ingresos
# REPORT MODULE
# =========================================
# Este módulo se encarga de:
# - Generar un reporte final del sistema
# - Mostrar estadísticas de pedidos
# - Agrupar pedidos por cliente
# - Mostrar productos vendidos

# FUNCTION: GENERATE REPORT
# =========================================
# Genera un resumen completo del sistema
def generate_report(orders_dict, clients_dict, products_dict):
    total_orders = len(orders_dict)  # Total de pedidos registrados
    total_income = calculate_income(orders_dict)  # Total de ingresos (usa función externa)

    total_income_str = f"${total_income:,.2f}" # Formatea el dinero (ej: $9,600.00)

    report = "\n=== FINAL REPORT ===\n" # Encabezado del reporte
    report += f"Total Orders: {total_orders}\n"
    report += f"Total Income: {total_income_str}\n"

    # ORDERS GROUPED BY CLIENT
    # =========================================
    # Muestra los pedidos organizados por cliente
    report += "\n--- Orders by Client ---\n"

    for client_id in clients_dict:  # Recorre todos los clientes
        client = clients_dict[client_id]
        full_name = client["first_name"] + " " + client["last_name"]
        
        # COUNT ORDERS PER CLIENT
        # =====================================
        
        count = 0  # count orders
        for order_id in orders_dict: # Recorre todos los pedidos
            if orders_dict[order_id]["client"] == client_id: # Si el pedido pertenece a ese cliente
                count += 1

        order_text = "order" if count == 1 else "orders" #Manejo de singular/plural

        report += f"\n[Client ID: {client_id}] {full_name}: {count} {order_text}\n" # Muestra resumen del cliente

        # show each order (detail)
        # =========================================
        has_orders = False # para saber si tiene pedidos

        for order_id in orders_dict: # Recorre nuevamente los pedidos
            order = orders_dict[order_id]

            if order["client"] == client_id: # Si el pedido pertenece al cliente
                has_orders = True

                product_name = products_dict[order["product"]][0] # Obtiene el nombre del producto

                report += (  # Agrega el detalle del pedido
                    f"   - Order ID: {order_id} | "
                    f"Product: {product_name} | "
                    f"Qty: {order['quantity']} | "
                    f"Total: ${order['total']}\n"
                )

        if not has_orders:  # Si el cliente no tiene pedidos
            report += "   (No orders)\n"

    
    # Products sold
    # =========================================
    # Muestra cuántas unidades se vendieron por producto
    report += "\n--- Products Sold ---\n"

    for product_id in products_dict: # Recorre todos los productos
        product_name = products_dict[product_id][0].title()  # Obtiene nombre del producto
        total_qty = 0  # Obtiene nombre del producto

        for order_id in orders_dict: # Recorre pedidos
            if orders_dict[order_id]["product"] == product_id: # Si el pedido contiene ese producto
                total_qty += orders_dict[order_id]["quantity"]

        unit_text = "unit" if total_qty == 1 else "units" # Manejo singular/plural

        report += f"[Product ID: {product_id}] {product_name}: {total_qty} {unit_text}\n" # Agrega al reporte
