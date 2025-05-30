print( "ejemplos de condicionales")
def recomendar_producto(edad, historial_compras, es_premium, presupuesto):
    # Productos de ejemplo
    productos = {
        "juguetes": 20,
        "videojuegos": 60,
        "ropa": 40,
        "vino": 70,
        "libros": 30,
        "accesorios premium": 100
    }

    # Reglas condicionales
    if edad < 13:
        recomendacion = "juguetes" if productos["juguetes"] <= presupuesto else "libros"
    elif 13 <= edad < 18:
        if "videojuegos" not in historial_compras and presupuesto >= productos["videojuegos"]:
            recomendacion = "videojuegos"
        else:
            recomendacion = "ropa" if productos["ropa"] <= presupuesto else "libros"
    elif edad >= 18:
        if es_premium and presupuesto >= productos["accesorios premium"]:
            recomendacion = "accesorios premium"
        elif "vino" not in historial_compras and edad >= 21 and presupuesto >= productos["vino"]:
            recomendacion = "vino"
        else:
            recomendacion = "libros"

    return f"Producto recomendado: {recomendacion.capitalize()}"