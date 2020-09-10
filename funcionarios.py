def menu ():
    op=0
    

    while  op != 5:
        print ("Menu")
        print ("1.- Registrar funcionarios")
        print ("2.- listado de los funcionarios")
        print ("3.- Buscar funcionario")
        print ("4.- Eliminar funcionario")
        print ("5.- Salir")
        op = input("Digite una opcion:")

        if op == '1':
            Registrar()
        elif op == '2':
            imprimir()
        elif op == '3':
            Buscar()
        elif op == '4':
            Eliminar()
        elif op == '5':
            Salir()


def Registrar():
    
    funcionarios={}
    continua= "s"
    while continua=="s":
        nombre=input("Ingrese el nombre del funcionario:")
        identificacion=int(input("Ingrese el id del funcionario:"))
        cargo=input("Ingrese el cargo del funcionario:")
        salario=int(input("Ingrese el salario del funcionario:"))
        funcionarios= nombre,identificacion,cargo,salario
        continua=input("quiere seguir insertando datos:[s/n]")
    
    return funcionarios


def imprimir():
    print("Listado de todos los funcionarios")
    for nombre in funcionarios:
        print(nombre,funcionarios)


def Buscar():
    print("Buscar")
    ident = int(input("Ingrese el id del funcionario a buscar:"))
    for identificacion in funcionarios:
        if identificacion == ident:
          print(identificacion, funcionarios)




def Eliminar():
    print("Eliminar")
    ident = int(input("Ingrese el id del funcionario a eliminar:"))
    for identificacion in funcionarios:
        if identificacion == ident:
            del [funcionarios]
            print(funcionarios)
    


def Salir():
    print ("Gracias por utlizar el programa")



menu()
funcionarios=Registrar()
imprimir()
Buscar()
Eliminar()
Salir()