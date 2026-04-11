def evaluar(nombre, materia, nota):
    if nota >= 90:
        print(nombre, "sacó una nota sobresaliente en", materia)
    elif nota >= 60:
        print(nombre, "aprobó la materia de", materia)
    else:
        print(nombre, "no logró pasar", materia)

evaluar("Ana", "Matemáticas", 95)
evaluar("Luis", "Historia", 70)
evaluar("Jose", "Química", 45)