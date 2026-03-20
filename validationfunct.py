# =========================================
# VALIDATION FUNCTIONS
# =========================================
# Este módulo se encarga de:
# - Validar entradas del usuario
# - Evitar datos incorrectos
# - Asegurar que el sistema reciba información válida

# FUNCTION: INPUT INTEGER
# =========================================
# Solicita un número entero válido (solo dígitos)
def input_int(prompt):
    while True:
        value = input(prompt).strip() # Lee entrada y elimina espacios
        if value.isdigit(): # Verifica que solo contenga números
            return int(value) # Convierte a entero
        print("Invalid input. Please enter a valid integer.")  # Mensaje de error si no es válido
        
        
 # FUNCTION: INPUT FLOAT
# =========================================
# Solicita un número decimal válido (precio)       
def input_float(prompt):
    while True:
        value = input(prompt).strip()

        # Replace comma with dot
        value = value.replace(",", ".") # Permite usar coma o punto como decimal

        
        if value.count(".") > 1: # Verifica que no haya más de un punto decimal
            print("Invalid format. Too many decimal points.")
            continue

        
        if value == "." or value == "": #  validar que no esté vacío o solo punto
            print("Invalid number.")
            continue

        #  validar que solo tenga números y punto
        valid = True
        for char in value:
            if not (char.isdigit() or char == "."):
                valid = False

        if not valid:
            print("Invalid input. Only numbers allowed.")
            continue

        
        number = float(value) # Convierte a número decimal

        
        if number <= 0:  # Verifica que sea positivo
            print("Value must be greater than 0.")
            continue

        return number # Retorna valor válido

# FUNCTION: INPUT STRING
# =========================================
# Solicita texto que no esté vacío
def input_string(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value  # Retorna texto válido
        print("This field cannot be empty.")

# FUNCTION: INPUT NAME
# =========================================
# Solicita nombres (solo letras y espacios)

def input_name(prompt):
    
    #Only allows letters and spaces
    
    while True:
        value = input(prompt).strip()

        if value.replace(" ", "").isalpha(): # Verifica que solo tenga letras (ignora espacios)
            return value.title() # Capitaliza (Ej: juan → Juan)
        else:
            print("Invalid name. Only letters are allowed.")

# FUNCTION: INPUT EMAIL
# =========================================
# Solicita un correo electrónico con formato básico válido
            
def input_email(prompt):
    while True:
        email = input(prompt).strip()

        
        if "@" in email and "." in email:  # Verifica que tenga '@' y '.'

            # dividir en dos partes
            parts = email.split("@") # Divide en usuario y dominio

            if len(parts) == 2: # Divide en usuario y dominio
                username, domain = parts

                # validar que no estén vacíos
                if username != "" and domain != "": # Verifica que ambas partes tengan contenido

                    # el dominio debe tener punto 
                    if "." in domain: # El dominio debe contener punto (ej: gmail.com)
                        return email

        print("Invalid email. Example: user@mail.com")
