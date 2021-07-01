import csv
from ClaseEntrega import Entrega
class ManejadorEntrega:
    __listaEntrega= []
    def __init__(self):
        self.__listaEntrega= []
    def leerArchivoEntrega(self):
        archivo2= open('entrega.csv')
        reader= csv.reader(archivo2,delimiter=';')
        bandera1= True
        for fila in reader:
            if bandera1:
                bandera1= not bandera1
            else:
                fec= fila[0]
                iden= fila[1]
                det= fila[2]
                mon= int(fila[3])
                entrega1= Entrega(fec,iden,det,mon)
                self.__listaEntrega.append(entrega1)
        archivo2.close()
    def BuscarID1(self,identif):
        indice= -1
        longitudLista= len(self.__listaEntrega)
        i= 0
        while (indice == -1)and(i < longitudLista):
            if identif == self.__listaEntrega[i].getIdentificador():
                indice= i
            i += 1
        return indice
    def obtenerMonto(self,indice1):
        return self.__listaEntrega[indice1].getMonto()




