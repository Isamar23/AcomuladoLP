import os
import sys
sys.path.append(r"C:\Users\User\Desktop\LP ISAMAR") 
from dao import daoConnection
from models import clases as c

os.system('cls')
conex = daoConnection.Connection("localhost", "root", "", "bdregisters")
conex.connect()

#insertar Ciudad
def insertarCiudad():
    nombre = input("Nombre ciudad\n")
    ciudad = c.City(nombre, 1, any)
    daoCity = daoConnection.DaoCity(conex)
    daoCity.insert(ciudad)

def mostrarCiudad(): 
    daoCity=daoConnection.DaoCity(conex)
    cities = daoCity.get_all()
    for city in cities:
        print(city)
        
    #Eliminar Ciudad
def ElimiarCiudad():
    os.system('cls')
    mostrarCiudad()
    NameElimiar = input("escoja el id de la ciudad que quiere eliminar:")
    
    daoCity = daoConnection.DaoCity(conex)
    #eliminar
    daoCity.delete(NameElimiar)

def EditarCiudad():
    os.system('cls')
    mostrarCiudad()
    oldID = input("ID de la ciudad a editar: ")
    newName = input("Nuevo Nombre: ")
    newStatus = input("Nuevo Status: ")

    daoCity = daoConnection.DaoCity(conex)
    ciudad = c.City(newName, newStatus, oldID)
    #actualizar
    daoCity.update(ciudad)


def BuscarCiudad():
    os.system('cls')
    nameBuscar = input("escriba el nombre de la ciudad que quiere buscar:")
    
    daoCity = daoConnection.DaoCity(conex)
    #buscar
    cities = daoCity.get_by_id(nameBuscar)
    print(cities) 
    
        
        
    
      
def MenuCiudad():
    print("1. ingresar ciudad")
    print("2. Editar ciudad")
    print("3. Mostrar ciudad")
    print("4. Eliminar ciudad")
    print("5. buscar ciudad")
    print("6. salir")

def mainCiudad():
    opcion = 0
    while(opcion != 6):
        MenuCiudad()
        opcion = int(input("dime tu opcion\n" ))
        if (opcion == 1 ):
            insertarCiudad()
            os.system("pause")
        elif(opcion == 2):
            EditarCiudad()
            os.system("pause")
        elif(opcion == 3):
            mostrarCiudad()
            os.system("pause")    
        elif(opcion == 4):
            ElimiarCiudad()
            os.system("pause")
        elif(opcion == 5):
            BuscarCiudad()
            os.system("pause")
        
def InsertarTrabajo():
    os.system('cls')
    name = input("Nombre trabajo: ")
    trabajo = c.jobsj(name, 1, any)

    daoJobsj = daoConnection.Daojobsj(conex)
    #insertar
    daoJobsj.insert(trabajo)

def MostrarTrabajo():
    os.system('cls')
    daoJob = daoConnection.Daojobsj(conex)
    print("Trabajos de la base de datos: ")
    #mostrar
    jobs = daoJob.get_all()
    for job in jobs:
        print(job)

def ElimiarTrabajo():
    os.system('cls')
    MostrarTrabajo()
    NameElimiar = input("escoja el id del trabajo que quiere eliminar:")
        
    daoJobsj = daoConnection.Daojobsj(conex)
    #eliminar
    daoJobsj.delete(NameElimiar)

def EditarTrabajo():
    os.system('cls')
    MostrarTrabajo()
    oldId = int(input("ID del trabajo a editar: "))
    newName = input("Nuevo nombre: ")
    newStatus = input("Nuevo status: ")

    daoJob = daoConnection.DaoJob(conex)
    trabajo = c.Job(newName, newStatus, oldId)
    #actualizar
    daoJob.update(trabajo)

def BuscarTrabajo():
    os.system('cls')
    idBuscar = input("escriba el id del trabajo que quiere buscar:")
    
    daoJob = daoConnection.DaoJob(conex)
    #buscar e imprimir
    job = daoJob.get_by_id(idBuscar)
    print(job)

def MenuTrabajo():
    os.system('cls')
    print("MENU Trabajo")
    print("1.Ingresar trabajo")
    print("2.Mostrar trabajos")
    print("3.Eliminar trabajo")
    print("4.Editar trabajo")
    print("5.Buscar trabajo")
    print("6.Salir")
    print("-")

def mainTrabajo():
    opcion= 0
    while(opcion != 6):
        MenuTrabajo()
        opcion = int(input("Elige la opcion deseada:"))
        if (opcion == 1):
            InsertarTrabajo()
            os.system("pause")
        elif (opcion == 2):
            MostrarTrabajo()
            os.system("pause")
        elif (opcion == 3):
            ElimiarTrabajo()
            os.system("pause")
        elif (opcion == 4):
            EditarTrabajo()
            os.system("pause")    
        elif (opcion == 5):
            BuscarTrabajo()
            os.system("pause")    
            
            
            
 #INSERTAR EMPLOYEES
 
def insertarEmployees():
    os.system("cls")
    name_employee = input("Digite un nuevo empleado: ")
    os.system("cls")
    idciudad= mostrarCiudad()
    idciudad = int(input("Elige un id de Ciudad para el empleado: "))
    os.system("cls")
    idJob= MostrarTrabajo()
    idJob = int(input("Elige un id de trabajo para el empleado : "))
    salario = int(input("Ingrese Salario del empleado: "))
    empleado = c.Employee(name_employee,idciudad,idJob,salario,1,any)
    daoEmployee = daoConnection.DaoEmployee(conex)
    daoEmployee.insert(empleado)

#Mostrar EMPLOYEES
def mostrarEmpleado():
    daoEmployee = daoConnection.DaoEmployee(conex)
    Employee = daoEmployee.get_all()
    for employees in Employee:
        print(employees)

#Eliminar EMPLOYEE
def EliminarEmployee():
    os.system("cls")
    eliminarEmpleados= input("Digite el id del empleado que quieres eliminar: ")
    daoEmployee = daoConnection.DaoEmployee(conex)
    daoEmployee.delete(eliminarEmpleados)

#Buscar EMPLOYEE
def buscarEmployee():
    os.system("cls")
    id_employee_search = input("Escribe el id que quieras buscar: ")
    daoEmployee = daoConnection.DaoEmployee(conex)
    Employee = daoEmployee.get_by_id(id_employee_search)
    print(Employee)

#ediatar EMPLOYEES
def editarEmployee():
    os.system("cls")
    mostrarEmpleado()
    ieo = int(input("Ingresa id para actualizarlo: "))
    n_new_employee = input("Escribe nuevo empleado : ")
    os.system("cls")
    n_new_idCiudad = mostrarCiudad()
    n_new_idCiudad = input("Digite un nuevo id de la ciudad para el empleado : ")
    os.system("cls")
    n_new_idJob = MostrarTrabajo()
    n_new_idJob = input("Digite el nuevo id de trabajo para el empleado : ")
    os.system("cls")
    status_new = input("nuevo status : ")
    new_salario = int(input("Nuevo salario : "))
    daoEmployee = daoConnection.DaoEmployee(conex)
    employee = c.Employee(n_new_employee,n_new_idCiudad,n_new_idJob,status_new,new_salario,ieo)
    daoEmployee.update(employee)

#MENU EMPLOYEE
def menuEmpleado():
    print("1.Ingresar empleados")
    print("2.Mostrar empleados")
    print("3.Eliminar empleado")
    print("4.Editar empleado")
    print("5.Buscar")
    print("6.Salir")

def main_Employees():
    opcion_Employees = 0
    while(opcion_Employees != 6):
        menuEmpleado()
        opcion_Employees = int(input("Elige la opcion deseada"))
        if(opcion_Employees ==1):
            insertarEmployees()
            os.system("pause")
        if(opcion_Employees ==2):
            mostrarEmpleado()
            os.system("pause")
        if(opcion_Employees == 3):
            EliminarEmployee()
            os.system("pause")
        if(opcion_Employees == 4):
            editarEmployee()
            os.system("pause")
        if(opcion_Employees == 5):
            buscarEmployee()
            os.system("pause")
        
        
def MenuPrincipal():
    print("MENU PRINCIPAL")
    print("1.registro de ciudades")
    print("2.registro de trabajos")
    print("3.registro de empleados")
    print("4.salir")
    print("-")

def main():
    opcion= 0
    while(opcion != 4):
        os.system('cls')
        MenuPrincipal()
        opcion = int(input("Elige la opcion deseada:"))
        if (opcion == 1):
            mainCiudad()
            os.system("pause")
        elif (opcion == 2):
            mainTrabajo()
            os.system("pause")
        elif (opcion == 3):
            main_Employees()
            os.system("pause") 
        
main()




#instanciar modelo
#city1 = models.clases.City(0, "Managua", 1)
#city2 = models.clases.City(0, "León", 1)
#city3 = models.clases.City(0, "Granada", 1)
#city4 = models.clases.City(0, "Masaya", 1)
#city5 = models.clases.City(0, "Estelí", 1)
#city6 = models.clases.City(0, "Jinotepe", 1)


#instanciar dao
#daoCity = dao.DaoCity(conex)
#insertar
#daoCity.insert(city1)
#daoCity.insert(city2)
#daoCity.insert(city3)
#daoCity.insert(city4)
#daoCity.insert(city5)
#daoCity.insert(city6)


#consultar
#cities = daoCity.get_all()
#for city in cities:
   # print(city)
   
   
   


















