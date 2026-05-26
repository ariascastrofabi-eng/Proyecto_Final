print("="*60)
print("BIENVENIDO AL MUNDO GAMING")
usuario_registrado=[]
contraseña_registrado=[]
while True:
    print("="*60)
    print(f"\n1.CREAR CUENTA")
    print(f"2.INICIA SESION")
    print(f"3.SALIR")
    print("="*60)

    opcion1=input("INGRESA UN NUMERO:").strip()
    if opcion1 == "1":
        print("="*60)
        print("CREA UNA CUENTA")
        print("="*60)
        usuario_nuevo=input("INGRESA UN USARIO NUEVO: ").strip()
        if usuario_nuevo in usuario_registrado:
            print("YA ESTA EN LA LISTA")
        elif usuario_nuevo == "":
            print("ERROR NO DEBE ESTAR VACIO")
        else:
            contraseña_nuevo=input("INGRESA LA CONTRASEÑA NUEVA: ").strip()
            usuario_registrado.append(usuario_nuevo)
            contraseña_registrado.append(contraseña_nuevo)
            print("="*60)
    elif opcion1 == "2":
        if len(usuario_registrado) == 0:
            print("no hay registrado en el sistema")
        else:
            print("="*60)
            print("INICIA SESION")
            print("="*60)
            intentos=3
            i = 1
            usuario=input("INGRESA EL NOMBRE DE USUARIO: ").strip()
            contraseña=input("INGRESA LA CONTRASEÑA: ").strip()
            pocision=0
            while i <= intentos:
                poci=0
                pocision=0
                while poci < len(usuario_registrado):
                    if usuario_registrado[poci]==usuario and contraseña_registrado [poci]==contraseña:
                        pocision=1
                        break
                    poci+=1
                
                if pocision == 1:
                    break
                
                if i < intentos:
                    print("="*60)
                    print(f"CONTRASEÑA O USUARIO INCORRECTO")
                    usuario=input("Ingresa el nombre de usuario: ").strip()
                    contraseña=input("Ingresa la contraseña correcta: ").strip()    
                i+=1
            if pocision== 1 :
                print("="*60)
                print("ACCESO CONCEDIDO ")
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
                    print("INGRESA UN NUMERO PARA USAR LA FUNCION(1-5): ")
                    print(f"\n                  1.INVENTARIO DE LOS PRODUCTOS: ")#esto es para ver los productos del inventario
                    print(f"                  2.VENTAS DE LOS PRODUCTOS: ")#esto es para la venta de un producto
                    print(f"                  3.INGRESA QUE PRODUCTO ")#esto es para adquirir un producto
                    print(f"                  4.VER LA CAJA DE AHORRO")#solo para pner el replace y slicing en mis productos
                    print(f"                  5.VOLVER AL INICIO")
                    print("="*60)

                    opcion=input("INGRESA UN NUMERO(1, 2, 3, 4 o 5) O ESCRIBA SALIR: ").strip().upper()

                    if opcion == "1":
                        print(f"EL PRODUCTO ES: {producto_1}|SU PRECIO DE VENTA ES: {precio_venta} bs | SU STOCK SON: {stock_1}")
                        print(f"EL PRODUCTO ES: {producto_2}|SU PRECIO DE VENTA ES: {precio_venta1} bs | SU STOCK SON: {stock_2}")
                    elif opcion == "2":

                        print("========ELIGA QUE PRODUCTOS DESEA VENDER======== ")
                        print(f"1.{producto_1}")
                        print(f"2.{producto_2}")

                        opcion2=input("INGRESA UN NUMERO: ").strip()
                        if opcion2 == "1":
                            if producto_1 == "Vacante":
                                print("=========ERROR NO HAY PRODUCTO REGISTRADO=======")
                            else:
                                cantidad=int(input("INGRESA LA CANTIDAD QUE DESEA VENDER: "))
                                if stock_1 >= cantidad and stock_1 > 0: 
                                    venta_total=precio_venta*cantidad
                                    caja+=venta_total
                                    stock_1-=cantidad
                                    print(f"'VENTA EXITOSA' EN LA CAJA ACTUALMENTE TENEMOS: {caja} BS Y DE STOCK DE ESTE PRODUCTO {producto_1} SON {stock_1} ")
                                else:
                                    print("=============NO HAY STOCK O NO ES SUFICIENTE=============")
                        elif opcion2 == "2":
                            if producto_2 == "Vacante":
                                print("===========ERROR NO HAY PRODUCTO REGISTRADO=======")
                            else:
                                cantidad=int(input("INGRESA LA CANTIDAD QUE DESEA VENDER: "))
                                if stock_2 >= cantidad and stock_2 > 0:
                                    venta_total1=precio_venta1*cantidad
                                    caja+=venta_total1
                                    stock_2-=cantidad

                                    print(f"EN LA CAJA ACTUALMENTE TENEMOS: {caja} BS Y DE STOCK DE ESTE PRODUCTO {producto_2} SON {stock_2} ")
                                else:
                                    print("=============NO HAY STOCK O NO ES SUFICIENTE=============")
                        else:
                            print("INGRESA SOLO LOS NUMEROS 1 O 2")
                    elif opcion == "3":
                        print("==========ELIJA EN QUE CAJA PARA GUARDAR MI PRODUCTO QUE VOY A ADQUIRIR=========== ")
                        
                        print(f"1.{producto_1}")
                        print(f"2.{producto_2}")

                        opcion3=input("INGRESA UN NUMERO: ")

                        if opcion3 == "1":
                            Producto_registrado=input("INGRESA EL NOMBRE DEL PRODUCTO QUE VA ADQUIRIR: ")
                            precio_adquirido=float(input("INGRESA EL PRECIO DE COMPRA DEl PRODUCTO: "))
                            precio_registrado=float(input("INGRESA EL PRECIO PARA VENDER EL PRODUCTO: "))
                            cantidad_pro=int(input("INGRESA LA CANTIDAD QUE QUIERE PARA LA TIENDA: "))

                            precio_total=cantidad_pro*precio_adquirido

                            if caja >= precio_total:
                                caja-=precio_total
                                print(f"NUESTRA CAJA AHORA TIENE AHORA {caja} BS")
                            else:
                                print("=======SALDO INSUFICIENTE=======")
                            if Producto_registrado == producto_1:
                                stock_1+=cantidad_pro
                                print(f"LA CANTIDAD DE MI PRODUCTO {producto_1} es ahora de {stock_1}")
                            else:
                                producto_1=Producto_registrado
                                precio_venta=precio_registrado
                                precio_compra=precio_adquirido
                                stock_1=cantidad_pro

                        elif opcion3 == "2":
                            Producto_registrado1=input("INGRESA EL NOMBRE DEL PRODUCTO QUE VA ADQUIRIR: ")
                            precio_adquirido1=float(input("INGRESA EL PRECIO DE COMPRA DEl PRODUCTO: "))
                            precio_registrado1=float(input("INGRESA EL PRECIO PARA VENDER EL PRODUCTO: "))
                            cantidad_pro1=int(input("INGRESA LA CANTIDAD QUE QUIERE PARA LA TIENDA: "))
                            precio_total1=cantidad_pro1*precio_adquirido1
                            
                            if caja >= precio_total1:
                                caja-=precio_total1
                                print(f"EN LA CAJA AHORA TENEMOS {caja}")
                            else:
                                print("=====SALDO INSUFICIENTE==========")
                            if Producto_registrado1 == producto_2:
                                stock_2+=cantidad_pro1
                            else:
                              producto_2=Producto_registrado1
                              precio_compra1=precio_adquirido1
                              precio_venta1=precio_registrado1
                              stock_2=cantidad_pro1
                        else:
                            print("INGRES SOLO LOS NUMEROS 1 O 2")
                        input("INGRESA ENTER PARA VOLVER AL MENU")
                    elif opcion == "4":
                        print(f"LA CAJA DE AHORRO QUE TENGO ES {caja} BS")
                        input("INGRESA ENTER PARA VOLVER AL MENU")
                    elif opcion == "5":
                        print("VOLVIENDO A MENU DE INICIO")
                        break
                    elif opcion == "SALIR":
                        print("\nSALIENDO DEL SISTEMAS......")
                        break
                    else:
                        print("SOLO LOS NUMERO 1,2,3,4 O 5 O SALIR")
                
                if opcion == "SALIR":
                    break
                continue
            else:print("BLOQUEADO POR INTENTOS")
            break
    elif opcion1 == "3":
        break
    else:
        print("OPCION VALIDA 1,2 Y 3")