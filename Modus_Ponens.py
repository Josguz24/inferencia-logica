def modus_ponens(p, q):
    """
    Si P implica Q (P → Q) y P es verdadero, entonces Q es verdadero.
    """
    if p:
        return q
    return "No se puede inferir Q"

# Ejemplo:
p = True   # "Si estudias"
q = "Aprobarás el examen"

resultado = modus_ponens(p, q)
print(resultado)  # Salida: "Aprobarás el examen"
