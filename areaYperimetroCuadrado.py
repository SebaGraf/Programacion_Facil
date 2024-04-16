def areaCuadrado(lado):
    a = lado ** 2
    l = lado * 4
    return a,l

a = 0
l = 0
print("PROGRAMA PARA CALCULAR AREA DE UN CUADRADO")
print("-------------------------------------------")

lado = float(input("Ingrese lado del cuadrdo: "))
a,l = areaCuadrado(lado)
print(f"EL AREA DEL CUADRADO DE LADO {lado} ES: ,{a} Y SU PERIMETRO ES: {l}")

