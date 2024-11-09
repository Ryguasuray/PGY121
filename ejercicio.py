def calculariva(precio):
    precio = precio * 0.19
    return precio
def calculoDesc(precio,descuento):
    total = (precio - (precio * (descuento/100)))
    print("el total a pagar con un descuento del" ,descuento, "%" es: $ ,total")
op = 3 
while op != 4:
    print("menu")
    print ("*"*10)
    print ("1. calcular iva")
    print ("2. descuento")
print("3. calcular imc")
print("4. salir")
op = int(input("ingresar opcion: (1-4): "))
#ejemplo de bucle en el cacillero se me abrio un bucle infinito, voy a utilizar el mando while en el codigo
contador = 0
while contador <10:
    #condicion de salida
    print (contador)
    contador +=1
    #bucle estructurado 

if op ==1:
    presio = int (input ("ingrese precio del producto:"))
    precio = calculariva("precio")
    print ("el precio con iva es :$",precio)
    if op ==2:
        precio = int(input("ingrese precio del producto:"))
        descuento = int(input("ingrese el % de descuento (o-100):"))
        calculoDesc(precio,descuento)
