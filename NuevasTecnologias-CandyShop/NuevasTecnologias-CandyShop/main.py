from numpy import empty
from pandas import notnull
import analisis
import carga
import limpieza
import merge


limpiezaRealizada = False
cargaRealizada = False
mergeoRealizado = False

while True:
    print("1. Cargar DataFrame. \n" \
    "2. Para limpieza \n" \
    "3. Para merge \n" \
    "4. Para analisis \n" \
    "5. Para Salir \n" \
    )

    opcion = input("Selecciona la opción de tu interes: \n")
    match opcion:
        case "1":
            print('Proceso de Carga clientes en ejecución \n')
            df_cliente_carga = carga.carga_clientes()
            print('Proceso de Carga clientes, finalizado correctamente\n')

            print('Proceso de Carga compras en ejecución \n')
            df_compra_carga = carga.carga_compras()
            print('Proceso de Carga compras, finalizado correctamente\n')
            cargaRealizada = True
        
        case "2": 
            if cargaRealizada==False:
                print("Se debe cargar datos previamente \n")
            else:
                print('Proceso de Limpieza clientes, en ejecución...')
                df_clientes_limpio = limpieza.limpiar_clientes(df_cliente_carga)
                print('Proceso de limpieza Clientes, finalizado correctamente, resultado guardado en la ruta de processed')
        
                print('Proceso de Limpieza compras, en ejecución...')
                df_compras_limpio = limpieza.limpieza_compras(df_compra_carga)
                print('Proceso de limpieza compras, finalizado correctamente, resultado guardado en la ruta de processed')
                limpiezaRealizada=True
        
        case "3":
            if cargaRealizada==False:
                print("Debes realizar la carga y limpieza primero \n")
            elif limpiezaRealizada==False:
                print("Debes realizar la carga y limpieza primero \n")
            else:
                print("Proceso de merge iniciado")
                df_clientes_compras = merge.merge()
                print("Proceso de merge finalizado correctamente")
                mergeoRealizado=True
        case "4":
            if mergeoRealizado==False:
                print("Debes realizar el merge primero \n")
            else:
                print('Proceso de analisis, en ejecución...')
                analisis.analisis(df_clientes_compras)
                print('Proceso de analisis, Finalizado \n')
       
        case "5":
            print('Chaolin Pinguin \n')
            break;
        case _:
            print("y eso quien te dijo que era una opcion \n")