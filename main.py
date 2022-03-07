from calculadora import Calculadora

calculadora=Calculadora()

operacion=0
while True:
    print("""Menu:
    1.- Sumar
    2.- Restar
    3.- Multiplicar
    4.- Dividir
    5.- Potencia
    6.- Raiz
    0.- Salir
    """)
    operacion=int(input("Selecciona opcion: "))
    
    match operacion:
        case 1:
            n1=input("Ingresa tus numeros separados por comas: ").split(',')
            n1=[int(x) for x in n1]
            value = calculadora.suma(*n1)
            print(f"El resultado es: {value}")
        case 2:
            n1=int(input("Ingresa primer valor: "))
            n2=int(input("Ingresa segundo valor: "))
            value = calculadora.resta(n1,n2)
            print(f"El valor de la resta es: {value}")
        case 3:
            n1=input("Ingresa tus numeros separados por comas: ").split(',')
            n1=[int(x) for x in n1]
            
            value = calculadora.multiplicacion(*n1)
            print(f"El resultado es: {value}")
        case 4:
            n1=int(input("Ingresa primer valor: "))
            n2=int(input("Ingresa segundo valor: "))
            try:
                value = calculadora.division(n1,n2)
                print(f"El valor de la divison es: {value}")
            except ZeroDivisionError:
                print("No se puede dividir entre 0")
        case 5:
            n1=int(input("Ingresa primer valor: "))
            n2=int(input("Ingresa segundo valor: "))
            value = calculadora.potencia(n1,n2)
            print(f"El resultado es: {value}")
        case 6:
            n1=int(input("Ingresa el numero: "))
            value = calculadora.raizcuadrada(n1)
            print(f"El resultado es: {value}")

    if operacion == 0:
        break