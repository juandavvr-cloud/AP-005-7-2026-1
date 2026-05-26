while True:
    a = input("Por favor ingrese un valor")
    aInt = int(a)
    mod = aInt%2
    
    if(mod == 0):
        print("a es un par")
    else:
        print("a No es un Par, es Impar")
        continuar = input("Por favor indique si desea continuar. (S/N):")
    if continuar != "s":
        print("Programa finalizado")
        break