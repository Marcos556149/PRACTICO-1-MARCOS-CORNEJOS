import csv
from ClaseRecepcion import Recepcion
from ClaseManejadorEntrega import ManejadorEntrega
class ManejadorRecepcion:
    __listaRecepcion= []
    def __init__(self):
        self.__listaRecepcion= []
    def leerArchivoRecepcion(self):
        archivo1= open('recepcion.csv')
        reader= csv.reader(archivo1,delimiter=';')
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                idd= fila[0]
                fe= fila[1]
                tip= fila[2]
                mar= fila[3]
                pro= fila[4]
                obs= fila[5]
                recepcion1= Recepcion(idd,fe,tip,mar,pro,obs)
                self.__listaRecepcion.append(recepcion1)
        archivo1.close()
    def Listar(self,Entregas):
        self.__listaRecepcion.sort()
        print("LISTA DE PRODUCTOS RECIBIDOS QUE AUN NO HAN SIDO REPARADOS")
        for i, Recepcion in enumerate(self.__listaRecepcion):
            identif= Recepcion.getID()
            if Entregas.BuscarID1(identif) == -1:
                print (self.__listaRecepcion[i])
    def MontoTotal(self,Entregas,marcaa):
        total= 0
        for j, Recepcion in enumerate(self.__listaRecepcion):
            if marcaa == Recepcion.getMarca():
                identificad= Recepcion.getID()
                indicee= Entregas.BuscarID1(identificad)
                if indicee != -1:
                    total += Entregas.obtenerMonto(indicee)
        print("El monto total de las reparaciones realizadas en productos de la marca {} es: {}".format(marcaa,total))







