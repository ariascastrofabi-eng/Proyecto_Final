print("BIENVENIDO AL MUNDO GAMING")
usuario=input("Ingresa el nombre de usuario: ").strip()
contraseña=input("Ingresa la contraseña correcta: ").strip()
intentos=3
i = 1 
while (contraseña.strip() != "Fabian19" or usuario.strip() != "FabianArias") and i < intentos:
    print("CONTRASEÑA INCORRECTA")
    usuario=input("Ingresa el nombre de usuario: ").strip()
    contraseña=input("Ingresa la contraseña correcta: ").strip()
    i+=1

if contraseña == "Fabian19" and usuario == "FabianArias":
    print("ACCESO CONCEDIDO ")
    while True:
        print("INGRESA UN NUMERO PARA USAR LA FUNCION(1-4): ")
        print(f"\n 1.INVENTARIO DE LOS PRODUCTOS: ")
        print(f" 2.VENTAS DE LOS PRODUCTOS: ")
        print(f" 3.INGRESA QUE PRODUCTO ")
        print(f"4.EDICION DE TEXTO DE LOS PRODUCTOS")

        opcion=input("INGRESA UN NUMERO: ").strip().upper()

        if opcion == "1":
            print("listo")
            input("INGRESA ENTER PARA VOLVER AL MENU")
        elif opcion == "2":
            print("No listo")
            input("INGRESA ENTER PARA VOLVER AL MENU")
        elif opcion == "3":
            print("XD")
            input("INGRESA ENTER PARA VOLVER AL MENU")
        elif opcion == "4":
            print("HOLA")
            input("INGRESA ENTER PARA VOLVER AL MENU")
        elif opcion == "SALIR":
            break
        else:
            print("INGRESA LOS NUMEROS DEL 1 AL 4 O SALIR")
else:
    print("bloqueado por 3 intentos")