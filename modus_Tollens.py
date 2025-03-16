def modus_tollens(p, q):
    """
    Si P implica Q (P → Q) y Q es falso, entonces P es falso.
    """
    if not q:
        return not p
    return "No se puede inferir P"

# Ejemplo:
p = True  # "Si llueve"
q = False  # "La calle NO está mojada"

resultado = modus_tollens(p, q)
print(resultado)  # Salida: False (No ha llovido)
