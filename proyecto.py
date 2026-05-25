print("BIENVENIDO AL MUNDO GAMING")
print("="*60)
usuario_registrado=""
contraseña_registrado=""
while True:
    print("="*60)
    print(f"\n1.CREAR CUENTA")
    print(f"2.INICIA SESION")

    opcion1=input("INGRESA UN NUMERO:").strip()
    if opcion1 == "1":
        print("CREA UNA CUENTA")
        print("="*60)
        usuario_registrado=input("INGRESA UN USUARIO NUEVA: ").strip()
        contraseña_registrado=input("INGRESA UNA CONTRASEÑA NUEVA: ").strip()
        print("CREADO CON EXITO")
    elif opcion1 == "2":
        if usuario_registrado == "" or contraseña_registrado == "":
            print("="*60)
            print("no hay registrado en el sistema")
            continue
        print("INICIA SESION")
        intentos=3
        i = 1
        usuario=input("INGRESA EL NOMBRE DE USUARIO: ")
        contraseña=input("INGRESA LA CONTRASEÑA: ")
        while (contraseña.strip() != contraseña_registrado or usuario.strip() != usuario_registrado) and i < intentos:
            print("="*60)
            usuario=input("Ingresa el nombre de usuario: ").strip()
            contraseña=input("Ingresa la contraseña correcta: ").strip()
            i+=1
        if contraseña == contraseña_registrado and usuario == usuario_registrado:
            print("ACCESO CONCEDIDO ")
            print("="*60)
            while True:
                print("="*60)
                print("INGRESA UN NUMERO PARA USAR LA FUNCION(1-4): ")
                print(f"\n                  1.INVENTARIO DE LOS PRODUCTOS: ")#esto es para ver los productos del inventario
                print(f"                  2.VENTAS DE LOS PRODUCTOS: ")#esto es para la venta de un producto
                print(f"                  3.INGRESA QUE PRODUCTO ")#esto es para adquirir un producto
                print(f"                  4.EDICION DE TEXTO DE LOS PRODUCTOS")#solo para pner el replace y slicing en mis productos
                print("="*60)

                opcion=input("INGRESA UN NUMERO(1, 2, 3, 4) O ESCRIBA SALIR: ").strip().upper()

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
                    print("Saliendo del sistema......")
                    break
                else:
                    print("solo los numeros 1,2,3,4 o salir")
        
        else:print("BLOQUEADO POR INTENTOS")
        break
    else:
        print("Opcion invalida solo 1 y 2")