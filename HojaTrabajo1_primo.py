print("Ingrese un numero")
x = int(input())

contador = 0
for i in range(x):

    if x%(i+1) == 0:
        contador += 1

if contador<= 2:
    print("Es primo")
else:
    print("No es primo")

print("Creditos Ramiro Telles")
print("CUI:30572502030301")
print("Carnet: 202010044")
