def calcular_promedio(alumno, materia, notas):
    total = 0
    
    for nota in notas:
        total = total + nota
    
    promedio = total / 3
    print("El promedio de", alumno, "en", materia, "es:", promedio)

calcular_promedio("Ana", "Matemáticas", [8, 10, 9])