#CLIENT MANAGEMENT MODULE
# Este módulo se encarga de:
# - Registrar clientes
# - Mostrar la lista de clientes
def register_client(clients_dict, client_id, first_name, last_name, email):
    
    if client_id in clients_dict: # Verifica si el cliente ya existe (evita duplicados)
        return "Client already exists"
        
    clients_dict[client_id] = { # Se guarda el cliente en el diccionario usando su ID como clave
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    # Retorna mensaje de éxito
    return "Client registered successfully"

# FUNCION VER CLIENTES
# Esta función muestra todos los clientes registrados
def view_clients(clients_dict):
    # Si no hay clientes registrados, retorna mensaje
    if not clients_dict:
        return "No clients registered"
    # Encabezado del listado
    result = "\n--- CLIENT LIST ---\n" # Recorre todos los clientes en el diccionario
   
    for client_id in clients_dict:      # Recorre todos los clientes en el diccionario
       
        client = clients_dict[client_id]
       
        full_name = client["first_name"] + " " + client["last_name"] # Construye el nombre completo
        # Agrega la información del cliente al resultado
        result += f"ID: {client_id} | Name: {full_name} | Email: {client['email']}\n"

    return result # Retorna el listado completo como texto