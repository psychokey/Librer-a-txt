def agregarlib():
    archivo=open("Libros.txt","a")
    book=input("Escriba el nombre del libro que desea agregar: ")
    archivo.write(book+"\n")
    archivo.close()

def verificarlibs():
    with open("Libros.txt","r") as File:
        informacion=File.read()
        libro=input("Escriba el nombre del libro que desea buscar: ")
        if libro in informacion:
            print("El libro",libro,"sí se encuentra en nuestra librería")
        else:
            print("El libro",libro,"no se encuentra en nuestra librería")
        
def visualizarlibs():
    archivo=open("Libros.txt","r")
    contenido=archivo.read()
    archivo.close()
    print("\n"+contenido)

def eliminarlibs():
    archivo=open("Libros.txt","w")
    archivo.write("")
    archivo.close()

power="SI"
while power=="SI":
    print("\n——————————————————————————————————————")
    print("Bienvenidos a la librería La Económica")
    print("——————————————————————————————————————")
    print("Este programa le permitirá:")
    print("1.Añadir un libro")
    print("2.Buscar un libro")
    print("3.Visualizar lista completa de libros")
    print("4.Borrar toda la información")
    opc=int(input("Seleccione una opción: "))
    if opc==1:
        agregarlib()
        print("¿Desea realizar otra operación? SI/NO")
        resp=input()
        power=resp.upper()
    if opc==2:
        verificarlibs()
        print("¿Desea realizar otra operación? SI/NO")
        resp=input()
        power=resp.upper()
    if opc==3:
        visualizarlibs()
        print("¿Desea realizar otra operación? SI/NO")
        resp=input()
        power=resp.upper()
    if opc==4:
        eliminarlibs()
        print("¿Desea realizar otra operación? SI/NO")
        resp=input()
        power=resp.upper()
    if opc<1 or opc>4:
        print("\nOpción no válida")
