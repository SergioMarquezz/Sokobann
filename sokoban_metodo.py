#Mono = 0
#Camino = 1
#Paredes = 2
#Cajas = 3
#Meta = 4
#Caja-Meta = 5
#Cajas encimadas = 6

import os #Importacion de la libreria para limpliar la consola
import readchar #Importacion de libreria para leer caracteres

class Sokoban: #Clase general del programa

    #Variables globales
        
     fila_mono = 2 #posicion inicial del mono en la fila 
     columna_mono = 1 #Posicion inicial del mono en la columna
     espacio = 1 #Declaracion de una variable para almacenar un camino
     activar_jalar = False #Declaracion de una bandera
     activar_fuerza = False #Declarion de una bandera 
     metas = 0
     nivel = 0
         #Columnas
     mapa =  [] # Filas "Variable donde se almacenan los elementos de la matriz"
            
             
    #Metodos

     def __init__(self): #Metodo constructor
         pass
    
     def imprimir_mapa(self): #Metodo para imprimir mapa



        print "Nivel 1"
        print ""
        for f in range (len(self.mapa)): #Guarda la posicion de las filas

            fila = ''

            for c in  range (len(self.mapa)): #Guarda la posicion de las columnas

                fila = fila + ' ' + str (self.mapa[f][c]) #str (Covierte de numeros a letras)

            print fila

     def iniciar_juego(self):
     #def cargar_mapa(self): #Metodo para cargar el mapa

        file = open(str(self.nivel) + ('.txt'),'r') #Linea que abre un archivo... "file" (variable que almacena el archivo)...
        #"open" (comando para abrir un archivo)... "0" (nombre del archivo)... ".txt" (extencion del archivo)... "r" (archivo para leer)
    
        for line in file: 
                    
            fila = [] 
                        
            for c in line [:-1]:
                                                        
                fila.append(int(c))
 
            self.mapa.append(fila)

        


     #def imprimir_mapa(self): #Metodo para imprimir mapa



       # print "Nivel 1"
        #print ""
        #for f in range (len(self.mapa)): #Guarda la posicion de las filas

         #   fila = ''

          #  for c in  range (len(self.mapa)): #Guarda la posicion de las columnas

           #     fila = fila + ' ' + str (self.mapa[f][c]) #str (Covierte de numeros a letras)

            #print fila

     #def contar_metas(self):

        for fila in range(len(self.mapa)):

             for columna in range(len(self.mapa)):

                 if self.mapa[fila][columna]==4:

                     self.metas = self.metas + 1


     #def posicion_mono(self):

        for fila in range(len(self.mapa)):

             for columna in range(len(self.mapa)):

                 if self.mapa[fila][columna] == 0:

                     self.fila_mono = fila
                     self.columna_mono = columna 


     def siguiente_nivel(self):
         self.nivel = self.nivel + 1
         iniciar_juego(self)


     def derecha(self): #Metodo movimiento hacia la Derecha



     #Jalar cajas

         if self.mapa[self.fila_mono][self.columna_mono - 1] == 3 and self.mapa[self.fila_mono][self.columna_mono + 1] == 1 and self.activar_jalar == True:

            self.mapa[self.fila_mono][self.columna_mono + 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono] = 3 #Jala la caja
            self.mapa[self.fila_mono][self.columna_mono - 1] = 1 #Pone un espacio en el lugar de la caja
            self.columna_mono = self.columna_mono + 1 #Actualiza la nueva posicion del mono


     #Encimar dos cajas 

        #Verifica si hay dos cajas delante del mono y si su fuerza esta activada 
         elif self.mapa[self.fila_mono][self.columna_mono + 1] == 3 and self.mapa[self.fila_mono][self.columna_mono + 2] == 3 and self.activar_fuerza == True:

            self.mapa[self.fila_mono][self.columna_mono + 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono + 2] = 6 #Encima una caja sobre la otra
            self.mapa[self.fila_mono][self.columna_mono] = 1 #Pone un espacio en el lugar del mono
            self.columna_mono = self.columna_mono + 1 #Actualiza la nueva posicion del mono


    #Avanzar con dos cajas encimadas

         elif self.mapa[self.fila_mono][self.columna_mono + 1] == 6 and self.mapa[self.fila_mono][self.columna_mono + 2] == 1 and self.activar_fuerza == True:

            self.mapa[self.fila_mono][self.columna_mono + 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono + 2] = 6 #Encima una caja sobre la otra
            self.mapa[self.fila_mono][self.columna_mono] = 1 #Pone un espacio en el lugar del mono
            self.columna_mono = self.columna_mono + 1 #Actualiza la nueva posicion del mono

    #Derecha y espacio

         elif self.mapa[self.fila_mono][self.columna_mono + 1] == 1: #Verifica si hay un espacio delante

            self.mapa[self.fila_mono][self.columna_mono + 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono] = self.espacio #Pone un camino en donde estaba el mono
            self.espacio = 1 #Guarda el valor del camino
            self.columna_mono = self.columna_mono + 1 #Actualiza la nueva posicion del mono

     #Mover cajas 

         #Verifica si hay una caja delante y delante de la caja un espacio
         elif self.mapa[self.fila_mono][self.columna_mono + 1] == 3 and self.mapa[self.fila_mono][self.columna_mono + 2] == 1:

            self.mapa[self.fila_mono][self.columna_mono + 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono + 2] = 3 #Mueve la caja 
            self.mapa[self.fila_mono][self.columna_mono] = self.espacio #Pone un camino en donde estaba el mono
            self.espacio = 1 #Guarda el valor del camino
            self.columna_mono = self.columna_mono + 1 #Actualiza la nueva posicion del mono

     #Caja en meta 

         elif self.mapa[self.fila_mono][self.columna_mono + 1] == 3 and self.mapa[self.fila_mono][self.columna_mono + 2] == 4:

            self.mapa[self.fila_mono][self.columna_mono + 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono + 2] = 5 #Mueve la caja 
            self.mapa[self.fila_mono][self.columna_mono] = 1 #Pone un camino en donde estaba el mono
            self.columna_mono = self.columna_mono + 1 #Actualiza la nueva posicion del mono
            self.metas = self.metas - 1 # Descuenta las metas

     #Pasar metas

         elif self.mapa[self.fila_mono][self.columna_mono + 1] == 4:

            self.mapa[self.fila_mono][self.columna_mono + 1] = 0 #Mueve el mono hacia la meta
            self.mapa[self.fila_mono][self.columna_mono] = self.espacio #Pone un camino donde esta el mono
            self.espacio = 4 #Guarda el valor del camino
            self.columna_mono = self.columna_mono + 1 #Actualiza la nueva posicion del mono

    #Sacar caja de la meta a un espacio 

         elif self.mapa[self.fila_mono][self.columna_mono + 1] == 5 and self.mapa[self.fila_mono][self.columna_mono + 2] == 1:

             self.mapa[self.fila_mono][self.columna_mono + 1] = 0
             self.mapa[self.fila_mono][self.columna_mono + 2] = 3
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 4
             self.columna_mono = self.columna_mono + 1
             self.metas = self.metas + 1

    #Empujar la caja/meta hacia otra meta

         elif self.mapa[self.fila_mono][self.columna_mono + 1] == 5 and self.mapa[self.fila_mono][self.columna_mono + 2] == 4:

             self.mapa[self.fila_mono][self.columna_mono + 1] = 0
             self.mapa[self.fila_mono][self.columna_mono + 2] = 5
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 4
             self.columna_mono = self.columna_mono + 1
    


    #Salto hacia una caja 

         elif self.mapa[self.fila_mono][self.columna_mono + 1] == 3 and self.mapa[self.fila_mono][self.columna_mono + 2] == 3:

            self.mapa[self.fila_mono][self.columna_mono + 1] = 3
            self.mapa[self.fila_mono][self.columna_mono + 2] = 0 
            self.mapa[self.fila_mono][self.columna_mono] = self.espacio
            self.espacio = 3
            self.columna_mono = self.columna_mono + 2


     def izquierda(self): #Metodo movimiento hacia la izquierda 


    #Jalar cajas

         if self.mapa[self.fila_mono][self.columna_mono + 1] == 3 and self.mapa[self.fila_mono][self.columna_mono - 1] == 1 and self.activar_jalar == True:

            self.mapa[self.fila_mono][self.columna_mono - 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono] = 3 #Jala la caja
            self.mapa[self.fila_mono][self.columna_mono + 1] = 1 #Pone un espacio en el lugar de la caja
            self.columna_mono = self.columna_mono - 1 #Actualiza la nueva posicion del mono


    #Encimar dos cajas 

        #Verifica si hay dos cajas delante del mono y si su fuerza esta activada 
         elif self.mapa[self.fila_mono][self.columna_mono - 1] == 3 and self.mapa[self.fila_mono][self.columna_mono - 2] == 3 and self.activar_fuerza == True:

            self.mapa[self.fila_mono][self.columna_mono - 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono - 2] = 6 #Encima una caja sobre la otra
            self.mapa[self.fila_mono][self.columna_mono] = 1 #Pone un espacio en el lugar del mono
            self.columna_mono = self.columna_mono - 1 #Actualiza la nueva posicion del mono


    #Avanzar con dos cajas encimadas

         elif self.mapa[self.fila_mono][self.columna_mono - 1] == 6 and self.mapa[self.fila_mono][self.columna_mono - 2] == 1 and self.activar_fuerza == True:

            self.mapa[self.fila_mono][self.columna_mono - 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono - 2] = 6 #Encima una caja sobre la otra
            self.mapa[self.fila_mono][self.columna_mono] = 1 #Pone un espacio en el lugar del mono
            self.columna_mono = self.columna_mono - 1 #Actualiza la nueva posicion del mono


     #Izquierda y espacio

         elif self.mapa[self.fila_mono][self.columna_mono - 1] == 1: #Verifica si hay un espacio delante

             self.mapa[self.fila_mono][self.columna_mono - 1] = 0 #Mueve el mono
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio #Pone un camino en donde estaba el mono
             self.espacio = 1 #Guarda el valor del camino
             self.columna_mono = self.columna_mono - 1 #Actualiza la nueva posicion del mono

     #Mover cajas

         #Verifica si hay una caja delante y delante de la caja un espacio
         elif self.mapa[self.fila_mono][self.columna_mono - 1] == 3 and self.mapa[self.fila_mono][self.columna_mono - 2] == 1:

            self.mapa[self.fila_mono][self.columna_mono - 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono - 2] = 3 #Mueve la caja 
            self.mapa[self.fila_mono][self.columna_mono] = self.espacio #Pone un camino en donde estaba el mono
            self.espacio = 1 #Guarda el valor del camino
            self.columna_mono = self.columna_mono - 1 #Actualiza la nueva posicion del mono

     #Caja en meta 

         elif self.mapa[self.fila_mono][self.columna_mono - 1] == 3 and self.mapa[self.fila_mono][self.columna_mono - 2] == 4:

            self.mapa[self.fila_mono][self.columna_mono - 1] = 0 #Mueve el mono
            self.mapa[self.fila_mono][self.columna_mono - 2] = 5 #Mueve la caja 
            self.mapa[self.fila_mono][self.columna_mono] = 1 #Pone un camino en donde estaba el mono
            self.columna_mono = self.columna_mono - 1 #Actualiza la nueva posicion del mono
            self.metas = self.metas - 1 # Descuenta las metas

     #Pasar metas 

         elif self.mapa[self.fila_mono][self.columna_mono - 1] == 4:

            self.mapa[self.fila_mono][self.columna_mono - 1] = 0 #Mueve el mono hacia la meta
            self.mapa[self.fila_mono][self.columna_mono] = self.espacio #Pone un camino donde esta el mono
            self.espacio = 4 #Guarda el valor del camino
            self.columna_mono = self.columna_mono - 1 #Actualiza la nueva posicion del mono

     #Sacar caja de la meta a un espacio 

         elif self.mapa[self.fila_mono][self.columna_mono - 1] == 5 and self.mapa[self.fila_mono][self.columna_mono - 2] == 1:

             self.mapa[self.fila_mono][self.columna_mono - 1] = 0
             self.mapa[self.fila_mono][self.columna_mono - 2] = 3
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 4
             self.columna_mono = self.columna_mono - 1
             self.metas = self.metas + 1

     #Empujar la caja/meta hacia otra meta

         elif self.mapa[self.fila_mono][self.columna_mono - 1] == 5 and self.mapa[self.fila_mono][self.columna_mono - 2] == 4:

             self.mapa[self.fila_mono][self.columna_mono - 1] = 0
             self.mapa[self.fila_mono][self.columna_mono - 2] = 5
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 4
             self.columna_mono = self.columna_mono - 1
             


     #Salto hacia una caja 

         elif self.mapa[self.fila_mono][self.columna_mono - 1] == 3 and self.mapa[self.fila_mono][self.columna_mono - 2] == 3:

            self.mapa[self.fila_mono][self.columna_mono - 1] = 3
            self.mapa[self.fila_mono][self.columna_mono - 2] = 0 
            self.mapa[self.fila_mono][self.columna_mono] = self.espacio
            self.espacio = 3
            self.columna_mono = self.columna_mono - 2



     def arriba(self): #Metodo movimiento hacia arriba

    #Jalar cajas  

         if self.mapa[self.fila_mono + 1][self.columna_mono] == 3 and self.mapa[self.fila_mono - 1][self.columna_mono] == 1 and self.activar_jalar == True:

             self.mapa[self.fila_mono - 1][self.columna_mono] = 0
             self.mapa[self.fila_mono + 1][self.columna_mono] = 1
             self.mapa[self.fila_mono][self.columna_mono] = 3
             self.fila_mono = self.fila_mono - 1

    #Encimar dos cajas 

         elif self.mapa[self.fila_mono - 1][self.columna_mono] == 3 and self.mapa[self.fila_mono - 2][self.columna_mono] == 3 and self.activar_fuerza == True:

             self.mapa[self.fila_mono - 1][self.columna_mono] = 0
             self.mapa[self.fila_mono - 2][self.columna_mono] = 6
             self.mapa[self.fila_mono][self.columna_mono] = 1
             self.fila_mono = self.fila_mono - 1


    #Avanzar con dos cajas encimadas

         elif self.mapa[self.fila_mono - 1][self.columna_mono] == 6 and self.mapa[self.fila_mono - 2][self.columna_mono] == 1 and self.activar_fuerza == True:

            self.mapa[self.fila_mono -1 ][self.columna_mono] = 0 #Mueve el mono
            self.mapa[self.fila_mono - 2][self.columna_mono] = 6 #Encima una caja sobre la otra
            self.mapa[self.fila_mono][self.columna_mono] = 1 #Pone un espacio en el lugar del mono
            self.fila_mono = self.fila_mono - 1 #Actualiza la nueva posicion del mono



    #Arriba y espacio

         elif self.mapa[self.fila_mono - 1][self.columna_mono] == 1: #Verifica si hay un espacio delante

           self.mapa[self.fila_mono - 1][self.columna_mono] = 0 #Mueve el mono
           self.mapa[self.fila_mono][self.columna_mono] = self.espacio #Pone un camino en donde estaba el mono
           self.espacio = 1 #Guarda el valor del camino
           self.fila_mono = self.fila_mono - 1 #Actualiza la nueva posicion del mono


    #Mover cajas

         #Verifica si hay una caja adelante y adelante de la caja un espacio
         elif self.mapa[self.fila_mono - 1][self.columna_mono] == 3 and self.mapa[self.fila_mono - 2][self.columna_mono] == 1:

            self.mapa[self.fila_mono - 1][self.columna_mono] = 0 #Mueve el mono hacia la caja
            self.mapa[self.fila_mono - 2][self.columna_mono] = 3 #Mueve la caja hacia el espacio
            self.mapa[self.fila_mono][self.columna_mono] = self.espacio #Pone un camino donde estaba el mono
            self.espacio = 1 #Guarda el valor del camino
            self.fila_mono = self.fila_mono - 1 #Actuliza la nueva poscion del mono


    #Caja en metas 

         elif self.mapa[self.fila_mono - 1][self.columna_mono] == 3 and self.mapa[self.fila_mono - 2][self.columna_mono] == 4:

            self.mapa[self.fila_mono - 1][self.columna_mono] = 0
            self.mapa[self.fila_mono - 2][self.columna_mono] = 5
            self.mapa[self.fila_mono][self.columna_mono] = 1
            self.fila_mono = self.fila_mono - 1
            self.metas = self.metas - 1 #Descuenta las metas


    #Pasar metas
        
         elif self.mapa[self.fila_mono - 1][self.columna_mono] == 4:

            self.mapa[self.fila_mono - 1][self.columna_mono] = 0
            self.mapa[self.fila_mono][self.columna_mono] = self.espacio
            self.espacio = 4
            self.fila_mono = self.fila_mono - 1

    #Sacar caja de la meta a un espacio 

         elif self.mapa[self.fila_mono - 1][self.columna_mono] == 5 and self.mapa[self.fila_mono - 2][self.columna_mono] == 1:

             self.mapa[self.fila_mono - 1][self.columna_mono] = 0
             self.mapa[self.fila_mono - 2][self.columna_mono] = 3
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 4
             self.fila_mono = self.fila_mono - 1
             self.metas = self.metas + 1

    #Empujar la caja/meta hacia otra meta


         elif self.mapa[self.fila_mono - 1][self.columna_mono] == 5 and self.mapa[self.fila_mono - 2][self.columna_mono] == 4:

             self.mapa[self.fila_mono - 1][self.columna_mono] = 0
             self.mapa[self.fila_mono - 2][self.columna_mono] = 5
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 4
             self.fila_mono = self.fila_mono - 1
            

    #Salto hacia una caja 

         elif self.mapa[self.fila_mono - 1][self.columna_mono] == 3 and self.mapa[self.fila_mono - 2][self.columna_mono] == 3:

             self.mapa[self.fila_mono - 1][self.columna_mono] = 3
             self.mapa[self.fila_mono - 2][self.columna_mono] = 0
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 3
             self.fila_mono = self.fila_mono - 2


     def abajo(self): #Metodo hacia abajo

    #Jalar cajas  

         if self.mapa[self.fila_mono - 1][self.columna_mono] == 3 and self.mapa[self.fila_mono + 1][self.columna_mono] == 1 and self.activar_jalar == True:

             self.mapa[self.fila_mono + 1][self.columna_mono] = 0
             self.mapa[self.fila_mono - 1][self.columna_mono] = 1
             self.mapa[self.fila_mono][self.columna_mono] = 3
             self.fila_mono = self.fila_mono + 1


   #Encimar dos cajas 

         elif self.mapa[self.fila_mono + 1][self.columna_mono] == 3 and self.mapa[self.fila_mono + 2][self.columna_mono] == 3 and self.activar_fuerza == True:

             self.mapa[self.fila_mono + 1][self.columna_mono] = 0
             self.mapa[self.fila_mono + 2][self.columna_mono] = 6
             self.mapa[self.fila_mono][self.columna_mono] = 1
             self.fila_mono = self.fila_mono + 1

   #Avanzar con dos cajas encimadas 

         elif self.mapa[self.fila_mono + 1][self.columna_mono] == 6 and self.mapa[self.fila_mono + 2][self.columna_mono] == 1 and self.activar_fuerza == True:

            self.mapa[self.fila_mono + 1][self.columna_mono] = 0 #Mueve el mono
            self.mapa[self.fila_mono + 2][self.columna_mono] = 6 #Encima una caja sobre la otra
            self.mapa[self.fila_mono][self.columna_mono] = 1 #Pone un espacio en el lugar del mono
            self.fila_mono = self.fila_mono + 1 #Actualiza la nueva posicion del mono


    #Abajo y espacio 

         elif self.mapa[self.fila_mono + 1][self.columna_mono] == 1: #Verifica si hay un espacio delante

           self.mapa[self.fila_mono + 1][self.columna_mono] = 0 #Mueve el mono
           self.mapa[self.fila_mono][self.columna_mono] = self.espacio #Pone un camino en donde estaba el mono
           self.espacio = 1 #Guarda el valor del camino
           self.fila_mono = self.fila_mono + 1 #Actualiza la nueva posicion del mono


    #Mover cajas  

        #Verifica si hay una caja adelante y delante de la caja un espacio

         elif self.mapa[self.fila_mono + 1][self.columna_mono] == 3 and self.mapa[self.fila_mono + 2][self.columna_mono] == 1:

           self.mapa[self.fila_mono + 1][self.columna_mono] = 0 #Mueve el mono hacia la caja
           self.mapa[self.fila_mono + 2][self.columna_mono] = 3 #Mueve la caja hacia el espacio
           self.mapa[self.fila_mono][self.columna_mono] = self.espacio #Pone un camino donde estaba el mono
           self.espacio = 1 #Guarda el valor del camino
           self.fila_mono = self.fila_mono + 1 #Actualiza la nueva posicion del mono 


    #Caja en meta

         elif self.mapa[self.fila_mono + 1][self.columna_mono] == 3 and self.mapa[self.fila_mono + 2][self.columna_mono] == 4:

            self.mapa[self.fila_mono + 1][self.columna_mono] = 0 #Mueve el mono hacia la caja
            self.mapa[self.fila_mono + 2][self.columna_mono] = 5 #Mueve la caja hacia el espacio
            self.mapa[self.fila_mono][self.columna_mono] = 1#Pone un camino donde estaba el mono
            self.fila_mono = self.fila_mono + 1 #Actualiza la nueva posicion del mono 
            self.metas = self.metas - 1 #Descuenta las metas 


    #Pasar metas 

         elif self.mapa[self.fila_mono + 1][self.columna_mono] == 4:

             self.mapa[self.fila_mono + 1][self.columna_mono] = 0
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 4
             self.fila_mono = self.fila_mono + 1

    #Sacar caja de la meta a un espacio 

         elif self.mapa[self.fila_mono + 1][self.columna_mono] == 5 and self.mapa[self.fila_mono + 2][self.columna_mono] == 1:

             self.mapa[self.fila_mono + 1][self.columna_mono] = 0
             self.mapa[self.fila_mono + 2][self.columna_mono] = 3
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 4
             self.fila_mono = self.fila_mono + 1
             self.metas = self.metas + 1


    #Empujar la caja/meta hacia otra meta


         elif self.mapa[self.fila_mono + 1][self.columna_mono] == 5 and self.mapa[self.fila_mono + 2][self.columna_mono] == 4:

             self.mapa[self.fila_mono + 1][self.columna_mono] = 0
             self.mapa[self.fila_mono + 2][self.columna_mono] = 5
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 4
             self.fila_mono = self.fila_mono + 1
             


    #Salto hacia una caja 

         elif self.mapa[self.fila_mono + 1][self.columna_mono] == 3 and self.mapa[self.fila_mono + 2][self.columna_mono] == 3:

             self.mapa[self.fila_mono + 1][self.columna_mono] = 3
             self.mapa[self.fila_mono + 2][self.columna_mono] = 0
             self.mapa[self.fila_mono][self.columna_mono] = self.espacio
             self.espacio = 3
             self.fila_mono = self.fila_mono + 2

  
        


objeto = Sokoban() #Creacion de un objeto

objeto.iniciar_juego() 
#objeto.cargar_mapa()
#objeto.contar_metas()
#objeto.posicion_mono()

while True: #Ciclo repetitivo

    
   
    os.system("cls") #Linea que limpia la pantalla 
    
    print "Juego del super sokoban"
    print ""    
    print " D---Derecha      A--Izquierda\n W--Arriba        S--Abajo"
    print " L-Activar jalar cajas\n O-Desactivar jalar cajas"
    print  " F-Activar fuerza\n G-Desactivar fuerza "
    print""

    objeto.imprimir_mapa() #Llamar al metodo para imprimir el mapa
    
    print ""
    print "Faltan " + str (objeto.metas) + " metas para terminar el nivel"
    
    print ""
    print "Hacia donde quiere moverse:   Derecha,Izquierda,Arriba,Abajo...." #Pregunta el movimiento 

    
    if objeto.metas == 0:

        print "Nivel superado"
        break
        #objeto.siguiente_nivel()
    
    avanzar = readchar.readchar () #Guarda el caracter en una variable 


    if avanzar == "D" or avanzar == "d": #Valida el movimiento a la derecha

        
        objeto.derecha() #Llamar al metodo para moverse a la derecha
        
        
    elif avanzar == "A" or avanzar == "a": #Valida el movimiento a la izquierda
    
        objeto.izquierda() #Llamar al metodo para moverse a la izquierda

        
    elif avanzar == "W" or avanzar == "w": #Valida el movimiento hacia arriba
        
        objeto.arriba()

    elif avanzar == "S" or avanzar == "s": #Valida el movimiento hacia abajo

        objeto.abajo()  #Llamar al metodo para moverse hacia abajo

    elif avanzar == "L" or avanzar == "l":

        objeto.activar_jalar = True

    elif avanzar == "O" or avanzar == "o":

        objeto.activar_jalar = False

    elif avanzar == "F" or avanzar == "f":

        objeto.activar_fuerza = True

    elif avanzar == "G" or avanzar == "g":

        objeto.activar_fuerza = False 


    
    



    

   

    


        

    



        


        