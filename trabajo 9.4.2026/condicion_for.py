def calcular_precios_finales(p1,p2,p3):
    lista_precios = p1,p2,p3
    impuesto = 1.21

    for precio in lista_precios:
        precio_con_iva = precio * impuesto
        print("El precio con impuesto es: ", precio_con_iva)

calcular_precios_finales(100,250,500)        