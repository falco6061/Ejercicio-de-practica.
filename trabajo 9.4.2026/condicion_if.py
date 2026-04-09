def controlar_clima(t1,t2,t3):
    promedio = (t1 * t2 * t3) / 3
    print("La temperatura promedio es: ", promedio)

    if promedio > 30:
        print("Hace mucho calor")

    if promedio < 10:
        print("Hace mucho frio")    

controlar_clima(35, 32, 40)


