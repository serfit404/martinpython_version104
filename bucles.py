print ("ejemplos de bucles")
inventario = {
    "frutas": {"manzana": 10, "plátano": 5},
    "verduras": {"zanahoria": 7, "papa": 20}
}

for categoria, items in inventario.items():
    print(f"Categoría: {categoria}")
    for producto, cantidad in items.items():
        print(f"  {producto}: {cantidad}")