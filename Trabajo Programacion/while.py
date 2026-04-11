def sumar_repetido(valor, veces, etiqueta):
    contador = 0
    resultado = 0
    
    while contador < veces:
        resultado = resultado + valor
        contador = contador + 1
    
    print(etiqueta, resultado)

sumar_repetido(5, 3, "Total:")