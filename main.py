from ClaseManejadorRecepcion import ManejadorRecepcion
from ClaseManejadorEntrega import ManejadorEntrega
if __name__=='__main__':
    Recepciones= ManejadorRecepcion()
    Recepciones.leerArchivoRecepcion()
    Entregas= ManejadorEntrega()
    Entregas.leerArchivoEntrega()
    Recepciones.Listar(Entregas)
    marcaa= input('Ingresar Marca: ')
    Recepciones.MontoTotal(Entregas,marcaa)



