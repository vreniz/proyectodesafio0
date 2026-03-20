# =========================================
# VALIDATION FUNCTIONS
# =========================================

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
    """
    Only allows letters and spaces
    """
    while True:
        value = input(prompt).strip()

        if value.replace(" ", "").isalpha():
            return value.title()
        else:
            print("Invalid name. Only letters are allowed.")
            
def input_email(prompt):
    while True:
        email = input(prompt).strip()

        # Debe tener @ y .
        if "@" in email and "." in email:

            # dividir en dos partes
            parts = email.split("@")

            if len(parts) == 2:
                username, domain = parts

                # validar que no estén vacíos
                if username != "" and domain != "":

                    # el dominio debe tener punto
                    if "." in domain:
                        return email

        print("Invalid email. Example: user@mail.com")
