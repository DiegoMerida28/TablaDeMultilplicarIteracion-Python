numero = int(input("Ingresa un n�mero para generar la tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
