class Recepcion:
    __id= ''
    __fecha= ''
    __tipo= ''
    __marca= ''
    __problema= ''
    __observaciones= ''
    def __init__(self,idd='',fe='',tip='',mar='',pro='',obs=''):
        self.__id = idd
        self.__fecha = fe
        self.__tipo = tip
        self.__marca = mar
        self.__problema = pro
        self.__observaciones = obs
    def __str__(self):
        return 'ID: {}, FECHA: {}, TIPO: {}, MARCA: {}, PROBLEMA: {}, OBSERVACIONES: {}'.format(self.__id,self.__fecha,self.__tipo,self.__marca,self.__problema,self.__observaciones)
    def getID(self):
        return self.__id
    def getMarca(self):
        return self.__marca
    def __gt__(self,otro):
        return self.__marca > otro.getMarca()
