class Entrega:
    __fechaa= ''
    __identificador= ''
    __detalle= ''
    __monto= ''
    def __init__(self,fec='',iden='',det='',mon=''):
        self.__fechaa = fec
        self.__identificador = iden
        self.__detalle = det
        self.__monto = mon
    def __str__(self):
        return 'FECHA: {}, IDENTIFICADOR: {}, DETALLE: {}, MONTO: {}'.format(self.__fechaa,self.__identificador,self.__detalle,self.__monto)
    def getIdentificador(self):
        return self.__identificador
    def getMonto(self):
        return self.__monto

