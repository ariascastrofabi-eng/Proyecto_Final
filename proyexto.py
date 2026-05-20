print("BIENVENIDO AL MUNDO GAMING")
usuario=input("Ingresa el nombre de usuario: ").strip()
contraseña=input("Ingresa la contraseña correcta: ").strip()
intentos=3
i = 1 
while contraseña.strip() != "Fabian19" and usuario.strip() != "FabianArias" and i < intentos:
    print("CONTRASEÑA INCORRECTA")
    usuario=input("Ingresa el nombre de usuario: ").strip()
    contraseña=input("Ingresa el nombre de usuario: ").strip()
    i+=1

if contraseña == "Fabian19" and usuario == "FabianArias":
    while True:
        print("INGRESA UN NUMERO PARA ENTRES A ESA FUNCION(1-4): ")
        print(f"\n1.INVENTARIO DE LOS PRODUCTOS: ")
        print(f"2.VENTAS DE LOS PRODUCTOS: ")
        print(f"3.INGRESA QUE PRODUCTO ")

        opcion=input("INGRESA UN NUMERO: ")

        if opcion == 1:
            print("listo")
else:
    print("bloqueado por 3 intentos")