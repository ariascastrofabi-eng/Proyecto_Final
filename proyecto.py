print("="*60)
print("BIENVENIDO AL MUNDO GAMING")
usuario_registrado=[]
contraseña_registrado=[]
producto_1="Vacante"
stock_1=0
precio_compra=0.0
precio_venta=0.0

producto_2="Vacante"
stock_2=0
precio_compra1=0.0
precio_venta1=0.0

caja=10000
while True:
    print("="*60)
    print(f"\n1.CREAR CUENTA")
    print(f"2.INICIA SESION")
    print(f"3.SALIR")
    print("="*60)

    opcion1=input("INGRESA UN NUMERO: ").strip().upper()
    if opcion1 == "1": #PARA CREARME UNA CUENTA
        print("="*60)
        print("CREA UNA CUENTA")
        print("="*60)
        usuario_nuevo=input("INGRESA UN USUARIO NUEVO: ").strip()
        if usuario_nuevo in usuario_registrado:
            print("YA ESTA EN LA LISTA") #si el usuario esta poniendo un usuario igual a otro entonces le sale un aviso igual
        elif usuario_nuevo == "":
            print("ERROR NO DEBE ESTAR VACIO") #esto es si en el usuario deja sin nada para pasar a crear una cuenta no le deja
        else:
            contraseña_nuevo=input("INGRESA LA CONTRASEÑA NUEVA: ").strip()
            usuario_registrado.append(usuario_nuevo)
            contraseña_registrado.append(contraseña_nuevo) #con esa funcion añade la contraseña y el usuario en la lista para que acceda el usuario
            print("="*60)
            print("CREADO CON EXITO")
            print("="*60)
    elif opcion1 == "2": #PARA INICIAR SESION
        if len(usuario_registrado) == 0:
            print("NO HAY REGISTRADO EN EL SISTEMA")
        else:
            print("="*60)
            print("INICIA SESION")
            print("="*60)
            intentos=3
            i = 1
            usuario=input("INGRESA EL NOMBRE DE USUARIO: ").strip()
            contraseña=input("INGRESA LA CONTRASEÑA: ").strip()
            pocision=0
            while i <= intentos: #esto para el conteo con el intentos con el if de intentos en el bucle controlan esa funcion
                poci=0
                pocision=0
                while poci < len(usuario_registrado): #esto es para ver si hay mas usuarios o no
                    if usuario_registrado[poci]==usuario and contraseña_registrado [poci]==contraseña: #esto es para ver en la posicion al mismo tiempo si el usuario y contraseña estan en la misma posicion para que no se entre con otras contraseñas o otros usuarios de la lista
                        pocision=1
                        break
                    poci+=1
                
                if pocision == 1:
                    break
                
                if i < intentos:
                    print("="*60)
                    print(f"CONTRASEÑA O USUARIO INCORRECTO")
                    usuario=input("INGRESA EL NOMBRE DE USUARIO: ").strip()
                    contraseña=input("INGRESA LA CONTRASEÑA: ").strip()    
                i+=1
            if pocision== 1 :
                print("="*60)
                print("ACCESO CONCEDIDO ")
                while True:
                    print("="*60)
                    print("INGRESA UN NUMERO PARA USAR LA FUNCION(1-5): ")
                    print(f"\n                  1.INVENTARIO DE LOS PRODUCTOS: ")#esto es para ver los productos del inventario
                    print(f"                  2.VENTAS DE LOS PRODUCTOS: ")#esto es para la venta de un producto
                    print(f"                  3.INGRESA QUE PRODUCTO ")#esto es para adquirir un producto en el inventario 1 o 2
                    print(f"                  4.VER LA CAJA DE AHORRO")#esta opcion es para ver la caja cuanto perdimos y cuanto ganamos al vender con su codigo del producto con las 3 palabras y para ver su stock como factura 
                    print(f"                  5.VOLVER AL INICIO") #para volver al inicio de sesion o crear cuenta
                    print("="*60)

                    opcion=input("INGRESA UN NUMERO(1, 2, 3, 4 o 5) O ESCRIBA SALIR: ").strip().upper()

                    if opcion == "1":
                        print(f"EL PRODUCTO ES: {producto_1}|SU PRECIO DE VENTA ES: {precio_venta} bs | SU STOCK SON: {stock_1}") #esto se ve el producto 1 que estoy adquiriendo
                        print(f"EL PRODUCTO ES: {producto_2}|SU PRECIO DE VENTA ES: {precio_venta1} bs | SU STOCK SON: {stock_2}")#esto se ve el producto 2 que estoy adquiriendo 
                    elif opcion == "2":

                        print("========ELIJA QUE PRODUCTOS DESEA VENDER======== ")
                        print(f"1.{producto_1} | stock: {stock_1}")
                        print(f"2.{producto_2} | stock: {stock_2}")

                        opcion2=input("INGRESA UN NUMERO: ").strip().upper()
                        if opcion2 == "1":
                            if producto_1 == "Vacante" or stock_1 == 0:
                                print("=========ERROR NO HAY PRODUCTO REGISTRADO O STOCK CERO=======")
                            else:
                                cantidad=int(input("INGRESA LA CANTIDAD QUE DESEA VENDER: ")) #esto es para cuantos vamos a vender del producto
                                if stock_1 >= cantidad and stock_1 > 0: 
                                    venta_total=precio_venta*cantidad #esto el total de la cantidad que estamos vendiendo con el precio para sumar en la caja
                                    caja+=venta_total
                                    stock_1-=cantidad #esto solo disminuye el stock con la cantidad adquirida
                                    print(f"'VENTA EXITOSA' EN LA CAJA ACTUALMENTE TENEMOS: {caja} BS Y DE STOCK DE ESTE PRODUCTO {producto_1} SON {stock_1} ")
                                else:
                                    print("=============NO HAY SUFICIENTE STOCK=============")
                        elif opcion2 == "2":
                            if producto_2 == "Vacante" or stock_2 == 0:
                                print("===========ERROR NO HAY PRODUCTO REGISTRADO O STOCK CERO=======")
                            else:
                                cantidad1=int(input("INGRESA LA CANTIDAD QUE DESEA VENDER: "))
                                if stock_2 >= cantidad1 and stock_2 > 0:
                                    venta_total1=precio_venta1*cantidad1 #esto el total de la cantidad que estamos vendiendo con el precio para sumar en la caja
                                    caja+=venta_total1
                                    stock_2-=cantidad1 #esto solo disminuye el stock con la cantidad adquirida

                                    print(f"EN LA CAJA ACTUALMENTE TENEMOS: {caja} BS Y DE STOCK DE ESTE PRODUCTO {producto_2} SON {stock_2} ")
                                else:
                                    print("=============NO HAY SUFICIENTE STOCK=============")
                        else:
                            print("INGRESA SOLO LOS NUMEROS 1 O 2")
                    elif opcion == "3":
                        print("==========ELIJA EN QUE CAJA PARA GUARDAR MI PRODUCTO QUE VOY A ADQUIRIR=========== ")
                        
                        print(f"1.{producto_1}")
                        print(f"2.{producto_2}")

                        opcion3=input("INGRESA UN NUMERO: ").strip().upper()

                        if opcion3 == "1":
                            Producto_registrado=input("INGRESA EL NOMBRE DEL PRODUCTO DE UNA COMPUTADORA QUE VA ADQUIRIR: ").strip().upper()
                            producto_limpio=Producto_registrado.replace(" ","_") #esto es para que la variables agarren bien el nombre del producto de la computadora relacionado
                            precio_adquirido=float(input("INGRESA EL PRECIO DE COMPRA DEl PRODUCTO(BS): "))
                            precio_registrado=float(input("INGRESA EL PRECIO PARA VENDER EL PRODUCTO(BS): "))
                            cantidad_pro=int(input("INGRESA LA CANTIDAD QUE QUIERE PARA LA TIENDA: "))

                            precio_total=cantidad_pro*precio_adquirido #el total de cuanto voy a gastar para la compra del producto y disminuye la caja y si es igual entonces el producto se suma solo las cantidades

                            if caja >= precio_total:
                                if precio_adquirido >= precio_registrado:
                                    print("ESTARIAS PERDIENDO GANANCIAS ESTAS SEGURO DE ESO") #es una advertencia si el usuario esta poniendo en el precio adquirido mas que para vender o igual porque estaria perdiendo dinero
                                    print("SI O NO")
                                    opcion4=input("INGRESA UN SI O NO: ").strip().upper()
                                    if opcion4 != "SI":
                                        print("CANCELADO")
                                        continue #solo para continuar con lo que no es SI
                                caja-=precio_total
                                if producto_limpio == producto_1:
                                    stock_1+=cantidad_pro
                                    precio_venta=precio_registrado
                                    print(f"LA CANTIDAD DE MI PRODUCTO {producto_1} es ahora de {stock_1}")
                                else:
                                    producto_1=producto_limpio
                                    precio_venta=precio_registrado
                                    precio_compra=precio_adquirido
                                    stock_1=cantidad_pro
                                print(f"'COMPRADO CON EXITO' NUESTRA CAJA AHORA TIENE AHORA {caja} BS")
                            else:
                                print("=======SALDO INSUFICIENTE=======")


                        elif opcion3 == "2":
                            Producto_registrado1=input("INGRESA EL NOMBRE DEL PRODUCTO DE UNA COMPUTADORA QUE VA ADQUIRIR: ").strip().upper()
                            producto_limpio1=Producto_registrado1.replace(" ","_")
                            precio_adquirido1=float(input("INGRESA EL PRECIO DE COMPRA DEl PRODUCTO(BS): "))
                            precio_registrado1=float(input("INGRESA EL PRECIO PARA VENDER EL PRODUCTO(BS): "))
                            cantidad_pro1=int(input("INGRESA LA CANTIDAD QUE QUIERE PARA LA TIENDA: "))
                            precio_total1=cantidad_pro1*precio_adquirido1
                            
                            if caja >= precio_total1:
                                if precio_adquirido1 >= precio_registrado1:
                                    print("ESTARIAS PERDIENDO GANANCIAS ESTAS SEGURO DE ESO") #es una advertencia si el usuario esta poniendo en el precio adquirido mas que para vender o igual porque estaria perdiendo dinero
                                    print("INGRESA SI O NO")
                                    opcion5=input("INGRESA UN SI O NO: ").strip().upper() 
                                    if opcion5 != "SI":
                                        print("CANCELADO")
                                        continue #solo para continuar con lo que no es SI
                                caja-=precio_total1
                                if producto_limpio1 == producto_2:
                                
                                    stock_2+=cantidad_pro1
                                    precio_venta1=precio_registrado1
                                    print(f"LA CANTIDAD DE MI PRODUCTO {producto_2} es ahora de {stock_2}")
                                else:
                                    producto_2=producto_limpio1
                                    precio_compra1=precio_adquirido1
                                    precio_venta1=precio_registrado1
                                    stock_2=cantidad_pro1
                                print(f"'COMPRADO CON EXITO' EN LA CAJA AHORA TENEMOS {caja}")
                            else:
                                print("=====SALDO INSUFICIENTE==========")
                        else:
                            print("INGRESA SOLO LOS NUMEROS 1 O 2")
                        input("INGRESA ENTER PARA VOLVER AL MENU") #esto para volver al menu principal 
                    elif opcion == "4":
                                producto_areglado=producto_1.replace("_"," ")
                                producto_areglado1=producto_2.replace("_"," ") #solo para volverlo sin espacios
                                print(f"LOS PRODUCTOS COMERCIALES QUE VENDO ES:{producto_areglado} | {producto_areglado1} ") 
                                if producto_1 == "Vacante":
                                    print("NINGUN PRODUCTO EN EL 1")
                                    codigo_deproducto="-----"#esto si no hay producto 
                                else:
                                    codigo_deproducto=producto_1[0:4]
                                
                                if producto_2 == "Vacante":
                                    print("NINGUN PRODUCTO EN EL 2")
                                    codigo_deproducto1="-----"
                                else:
                                    codigo_deproducto1=producto_2[0:4]
                                print(f"EL CODIGO DE LOS PRODUCTOS: {codigo_deproducto} | {codigo_deproducto1}")

                                print(f"""      
                                ===========================================================
                                |                   RESUMEN FACTURA                        |
                                ===========================================================
                                |    EN LA CAJA TENEMOS                                    |
                                |    caja {caja} BS                                        |
                                |    CODIGO: {codigo_deproducto} | STOCK: {stock_1}                                |
                                |    CODIGO1: {codigo_deproducto1} | STOCK: {stock_2}                              |
                                ===========================================================""")
                                input("INGRESA ENTER PARA VOLVER AL MENU")
                    elif opcion == "5":
                        print("VOLVIENDO A MENU DE INICIO") #solo para volver al menu de inicio
                        break
                    elif opcion == "SALIR":
                        print("\nSALIENDO DEL SISTEMAS......") #salir del sistema siempre
                        break
                    else:
                        print("SOLO LOS NUMERO 1,2,3,4 O 5 O SALIR")
                
                if opcion == "SALIR":
                    break
                continue #esto ayuda al 5 a volver al menu de inicio
            else:print("BLOQUEADO POR INTENTOS")
            break
    elif opcion1 == "3": # ESTO ES PARA CERRAR EL SISTEMA
        break
    else:
        print("OPCION VALIDA 1,2 Y 3")