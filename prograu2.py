import re

def derizqui(str, princ):#Resive la incognita y la cadena   ::::Esta funcion es cuando los operadores son iguales en casos donde las operaciones_
               element=str  #se van resolviendo de izquierda a derecha
               print("Elementos del tripo :"+element)
               print("")                                      #A partir de aquí empieza generar la esctructa del triplo
               print("_t0 = "+element[3:4]+" "+element[5:6]+" "+element[7:8]) #Forma el triplo leyendo la cadena por posiciones
               print("_t1 = "+"_t0 "+element[11:12]+" "+element[13:14])
               print("_t2 = _t1 "+element[15:16]+" "+element[17:18])
               print(princ+" = "+"t2")

def cuarto(str, princ): #Esta funcion recibe dos parametros la incognita y la expresió con_
               element=str   #la que se va a construir los triplos
               print("Esta en la funcion")
               print("Elementos del tripo :"+elemento)
               print("")                               #Aquí contruye los triplos tomando caracteres de las partes de la expresión
               print("_t0 = "+elemento[3:4]+" "+elemento[5:6]+" "+elemento[7:8])
               print("_t1 = "+elemento[15:16]+" "+elemento[17:18]+" "+elemento[19:20])
               print("_t2 = _t0 "+" "+elemento[11:12]+" _t1")
               print(principal+" = "+" _t2")

filename="recurso.txt"     
textfile=open(filename,"r") #Abre el archivo donde esta la expresion en modo de lectura

textfile.seek(0) #Se empieza a leer la expresion iniciando en el indice 0
principal=textfile.read(1)#Lee la letra principal o incognita de la operación

print("Elige el ejemplo: [RESPETAR LOS ESPACIOS ENTRE VAIRABLES Y OPERADORES") 
print("----------------------------------------")
print("1. Formato para el ejemplo 1: X = 2 + 5 * Y")
print("-----------------------------------------")
print("2. Formato para el ejemplo 2: X = a / a + b * b")
print("------------------------------------------------")
print("3. Formato para el ejemplo 3: X = ( a + 2 ) / 3 + b")
print("------------------------------------------------")
print("4. Formato para el ejemplo 4: X = ( a + 2 ) / ( 3 - b )")
print("------------------------------------------------")
print("5. Formato para el ejemplo 5: X = 2 * y - ( ( 4 * y ) + z )")
print("Ingrese una opcion:")
opci= int(input())

if(opci==1):
    regex = r"\s[\d|aA-zZ]\s[\*|\/]\s[\d|aA-zZ]\s[\+|\-]\s[\d|aA-zZ]" #Expresiones reguales par cada tipo de jerarquía
    reg =re.compile(regex)                                            #de operaciones, pudiendo operar con número y con
    regex1 = r"\s[\d|aA-zZ]\s[\+|\-]\s[\d|aA-zZ]\s[\*|\/]\s[\d|aA-zZ]" #letras 
    reg1 =re.compile(regex1)
    regex2 = r"\s[\d|aA-zZ]\s[\*|\/]\s[\d|aA-zZ]\s[\*|\/]\s[\d|aA-zZ]"
    reg2 =re.compile(regex2)
    regex3 = r"\s[\d|aA-zZ]\s[\+|\-]\s[\d|aA-zZ]\s[\+|\-]\s[\d|aA-zZ]"
    reg3 =re.compile(regex3)


    for line in textfile:   #Aquí se encuentra cada estructura que se puede llegar a generar 
        lista = reg.findall(line) #depediendo del tipo de expresión que se ingrese.
        for elemento in lista:
               if re.search(regex,elemento): #En todas las estrucutras se encuentra la condicional, que auyda 
                  print("Elementos del triplo: "+elemento) #a que se genere una unica estructura.
                  print("_t0 = "+elemento[1:2]+" "+elemento[3:4]+" "+elemento[5:6])
                  print("_t1 = "+"_t0"+" "+elemento[7:8]+" "+elemento[9:10])
                  print(principal+" = "+"_t1")
                  break
        #De aquí en adelante son las diferentes estructuras que se pueden llegar a cumplir 
        #El algoritmo es el mismo solo cambia las estructuras y las posiciones que maneja
        lista1 = reg1.findall(line)
        for elemento in lista1:
               if re.search(regex1,elemento):
                  print("expresion>> "+elemento)
                  print("_t0 = "+elemento[5:6]+" "+elemento[7:8]+" "+elemento[9:10])
                  print("_t1 = "+"_t0"+" "+elemento[3:4]+" "+elemento[1:2])
                  print(principal+" = "+"_t1")

                  break
        lista2 = reg2.findall(line)
        for elemento in lista2:
               if re.search(regex2,elemento):
                  print("Elementos de expresion "+elemento)
                  print("_t0 = "+elemento[1:2]+" "+elemento[3:4]+" "+elemento[5:6])
                  print("_t1 = "+"_t0"+" "+elemento[7:8]+" "+elemento[9:10])
                  print(principal+" = "+"_t1")
                  break

        lista3 = reg3.findall(line)
        for elemento in lista3:
               if re.search(regex3,elemento):
                  print("Elementos de expresion "+elemento)
                  print("_t0 = "+elemento[1:2]+" "+elemento[3:4]+" "+elemento[5:6])
                  print("_t1 = "+"_t0"+" "+elemento[7:8]+" "+elemento[9:10])
                  print(principal+" = "+"_t1")
                  break

#Las demás opciones siguen el mismo algoritmo
elif(opci==2):
        #Esta son todas las combianciones posibles del ejecicio dos, SE TOMA EN CUENTA EL ESPACIO
        #ANTES Y DESPUES DE CADA CARACTER 
        regex1 = r"\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s?\*?\s?\/?\s[\d|a-z]" 
        reg1 =re.compile(regex1)
        regex2 = r"\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s?\+?\s?\-?\s[\d|a-z]" 
        reg2 =re.compile(regex2)
        regex3 = r"\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s?\+?\s?\-?\s[\d|a-z]" 
        reg3 =re.compile(regex3)
        regex4 = r"\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s?\+?\s?\-?\s[\d|a-z]" 
        reg4 =re.compile(regex4)
        regex5 = r"\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s?\*?\s?\/?\s[\d|a-z]" 
        reg5 =re.compile(regex5)
        regex6 = r"\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s?\*?\s?\/?\s[\d|a-z]" 
        reg6 =re.compile(regex6)
        regex7 = r"\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s?\*?\s?\/?\s[\d|a-z]" 
        reg7 =re.compile(regex7)
        regex8 = r"\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s?\+?\s?\-?\s[\d|a-z]" 
        reg8 =re.compile(regex8)

        for line in textfile:
          #Aquí se encuentra las estructuras para cada expresion regular que se pudieras llegar a cumplir
          #El algoritmo es el mismo que el anterior solo cambias las posiciones que maneja
          #Esto depende de la jerarquia de operaciones

            lista = reg1.findall(line)
            for elemento in lista:
                 if re.search(regex1,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[1:2]+" "+elemento[3:4]+" "+elemento[5:6])
                     print("_t1 = "+elemento[9:10]+" "+elemento[11:12]+" "+elemento[13:14])
                     print("_t2 ="+"_t0 "+elemento[7:8]+" _t1")
                     print(principal+" = "+"t2")
                     break
        
            lista = reg2.findall(line)
            for elemento in lista:
                 if re.search(regex2,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[5:6]+" "+elemento[7:8]+" "+elemento[9:10])
                     print("_t1 = _t0 "+" "+elemento[11:12]+" "+elemento[13:14])
                     print("_t2 = _t1 "+elemento[3:4]+" "+elemento[1:2])
                     print(principal+" = "+"t2")
                     break

            lista = reg3.findall(line)
            for elemento in lista:
                 if re.search(regex3,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[1:2]+" "+elemento[3:4]+" "+elemento[5:6])
                     print("_t1 = "+"_t0 "+elemento[7:8]+" "+elemento[9:10])
                     print("_t2 = _t1 "+elemento[11:12]+" "+elemento[13:14])
                     print(principal+" = "+"t2")
                     break
  
            lista = reg4.findall(line)
            for elemento in lista:
                 if re.search(regex4,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[1:2]+" "+elemento[3:4]+" "+elemento[5:6])
                     print("_t1 = _t0 "+elemento[7:8]+" "+elemento[9:10])
                     print("_t2 = _t1 "+elemento[11:12]+" "+elemento[13:14])
                     print(principal+" = "+"t2")
                     break
    
            lista = reg5.findall(line)
            for elemento in lista:
                 if re.search(regex5,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[1:2]+" "+elemento[3:4]+" "+elemento[5:6])
                     print("_t1 = "+elemento[9:10]+" "+elemento[11:12]+" "+elemento[13:14])
                     print("_t2 ="+" _t0 "+elemento[7:8]+"_t1")
                     print(principal+" = "+"t2")
                     break
 
            lista = reg6.findall(line)
            for elemento in lista:
                 if re.search(regex6,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[9:10]+" "+elemento[11:12]+" "+elemento[13:14])
                     print("_t1 = "+"_t0"+" "+elemento[7:8]+" "+elemento[5:6])
                     print("_t2 = "+"_t1 "+elemento[3:4]+" "+elemento[1:2])
                     print(principal+" = "+"t2")
                     break
   
            lista = reg7.findall(line)
            for elemento in lista:
                 if re.search(regex7,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[9:10]+" "+elemento[11:12]+" "+elemento[13:14])
                     print("_t1 = "+"_t0"+" "+elemento[7:8]+" "+elemento[5:6])
                     print("_t2 = "+"_t1 "+elemento[3:4]+" "+elemento[1:2])
                     print(principal+" = "+"t2")
                     break
     
            lista = reg8.findall(line)
            for elemento in lista:
                 if re.search(regex8,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[1:2]+" "+elemento[3:4]+" "+elemento[5:6])
                     print("_t1 = "+elemento[9:10]+" "+elemento[11:12]+" "+elemento[13:14])
                     print("_t2 ="+" _t0 "+elemento[7:8]+"_t1")
                     print(principal+" = "+"t2")
                     break

elif(opci==3):
        regex1 = r"\s\(\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s\)\s\+?\s?\-?\s[\d|a-z]\s?\*?\s?\/?\s[\d|a-z]" 
        reg1 =re.compile(regex1)
        regex2 = r"\s\(\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s\)\s\*?\s?\/?\s[\d|a-z]\s?\+?\s?\-?\s[\d|a-z]" 
        reg2 =re.compile(regex2)
        regex3 = r"\s\(\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s\)\s\+?\s?\-?\s[\d|a-z]\s?\+?\s?\-?\s[\d|a-z]" 
        reg3 =re.compile(regex3)
        regex4 = r"\s\(\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s\)\s\*?\s?\/?\s[\d|a-z]\s?\+?\s?\-?\s[\d|a-z]" 
        reg4 =re.compile(regex4)
        regex5 = r"\s\(\s[\d|a-z]\s\*?\s?\/?\s[\d|a-z]\s\)\s\*?\s?\/?\s[\d|a-z]\s?\*?\s?\/?\s[\d|a-z]" 
        reg5 =re.compile(regex5)
        regex6 = r"\s\(\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s\)\s\*?\s?\/?\s[\d|a-z]\s?\*?\s?\/?\s[\d|a-z]" 
        reg6 =re.compile(regex6)
        regex7 = r"\s\(\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s\)\s\+?\s?\-?\s[\d|a-z]\s?\*?\s?\/?\s[\d|a-z]" 
        reg7 =re.compile(regex7)
        regex8 = r"\s\(\s[\d|a-z]\s\+?\s?\-?\s[\d|a-z]\s\)\s\+?\s?\-?\s[\d|a-z]\s?\+?\s?\-?\s[\d|a-z]" 
        reg8 =re.compile(regex8)

        for line in textfile:
            lista = reg1.findall(line)
            for elemento in lista:
                 if re.search(regex1,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[3:4]+" "+elemento[5:6]+" "+elemento[7:8])
                     print("_t1 = "+elemento[13:14]+" "+elemento[15:16]+" "+elemento[17:18])
                     print("_t2 ="+"_t0 "+elemento[11:12]+" _t1")
                     print(principal+" = "+"t2")
                     break
        
            lista = reg2.findall(line)
            for elemento in lista:
                 if re.search(regex2,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[3:4]+" "+elemento[5:6]+" "+elemento[7:8])
                     print("_t1 = _t0 "+" "+elemento[11:12]+" "+elemento[13:14])
                     print("_t2 ="+elemento[15:16]+" "+elemento[17:18])
                     print(principal+" = "+"t2")
                     break

            lista = reg3.findall(line)
            for elemento in lista:
                 if re.search(regex3,elemento):
                    derizqui(elemento, principal)
                    break
                     
            lista = reg4.findall(line)
            for elemento in lista:
                 if re.search(regex4,elemento):  
                    derizqui(elemento, principal)
                    break
    

            lista = reg5.findall(line)
            for elemento in lista:
                 if re.search(regex5,elemento):   
                    derizqui(elemento, principal)
                    break
 
            lista = reg6.findall(line)
            for elemento in lista:
                 if re.search(regex6,elemento):
                    derizqui(elemento, principal)
                    break

            lista = reg7.findall(line)
            for elemento in lista:
                  if re.search(regex7,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[3:4]+" "+elemento[5:6]+" "+elemento[7:8])
                     print("_t1 = "+elemento[13:14]+" "+elemento[15:16]+" "+elemento[17:18])
                     print("_t2 ="+"_t0 "+elemento[11:12]+" _t1")
                     print(principal+" = "+"t2")
                     break
     
            lista = reg8.findall(line)
            for elemento in lista:
                 if re.search(regex8,elemento):
                    derizqui(elemento, principal)
                    break

elif(opci==4):
       #Posibles estructuras que las operaciones pueden llegar a tener 
        regex1 = r"\s\(\s[\d|a-z]\s[\*|\/]\s[\d|a-z]\s\)\s[\+|\-]\s\(\s[\d|a-z]\s[\*|\/]\s[\d|a-z]\s\)" 
        reg1 =re.compile(regex1)
        regex2 = r"\s\(\s[\d|a-z]\s[\+|\-]\s[\d|a-z]\s\)\s[\*|\/]\s\(\s[\d|a-z]\s[\+|\-]\s[\d|a-z]\s\)" 
        reg2 =re.compile(regex2)
        regex3 = r"\s\(\s[\d|a-z]\s[\*|\/]\s[\d|a-z]\s\)\s[\+|\-]\s\(\s[\d|a-z]\s[\+|\-]\s[\d|a-z]\s\)" 
        reg3 =re.compile(regex3)
        regex4 = r"\s\(\s[\d|a-z]\s[\*|\/]\s[\d|a-z]\s\)\s[\*|\/]\s\(\s[\d|a-z]\s[\+|\-]\s[\d|a-z]\s\)" 
        reg4 =re.compile(regex4)
        regex5 = r"\s\(\s[\d|a-z]\s[\*|\/]\s[\d|a-z]\s\)\s[\*|\/]\s\(\s[\d|a-z]\s[\*|\/]\s[\d|a-z]\s\)" 
        reg5 =re.compile(regex5)
        regex6 = r"\s\(\s[\d|a-z]\s[\+|\-]\s[\d|a-z]\s\)\s[\*|\/]\s\(\s[\d|a-z]\s[\*|\/]\s[\d|a-z]\s\)" 
        reg6 =re.compile(regex6)
        regex7 = r"\s\(\s[\d|a-z]\s[\+|\-]\s[\d|a-z]\s\)\s[\+|\-]\s\(\s[\d|a-z]\s[\*|\/]\s[\d|a-z]\s\)" 
        reg7 =re.compile(regex7)
        regex8 = r"\s\(\s[\d|a-z]\s[\+|\-]\s[\d|a-z]\s\)\s[\+|\-]\s\(\s[\d|a-z]\s[\+|\-]\s[\d|a-z]\s\)" 
        reg8 =re.compile(regex8)
        regex9 = r"\s\(\s[\d|a-z]\s[\*|\-]\s[\d|a-z]\s\)\s[\*|\/]\s\(\s[\d|a-z]\s[\+|\-]\s[\d|a-z]\s\)" 
        reg9 =re.compile(regex9)
        regex10 = r"\s\(\s[\d|a-z]\s[\*|\/?\s[\d|a-z]\s\)\s[\*|\/]\s\(\s[\d|a-z]\s[\/|\*]\s[\d|a-z]\s\)" 
        reg10 =re.compile(regex10)
         
        #Al existir dos parentesis en la expresión o estructura del ejemplo
        # Sin importar los operadores que tenga, siempre se va a resolver primero lo que está dentro del parentesis
        # Es por eso que se creo una función en la cuando se cumpla la expresion
        # simplemente se llama la función que imprime la estructura de los triplos
        # con los valores correspondientes
        for line in textfile:
            lista = reg1.findall(line)
            for elemento in lista:
                 if re.search(regex1,elemento):   
                    cuarto(elemento, principal)
                    break
        
            lista = reg2.findall(line)
            for elemento in lista:
                 if re.search(regex2,elemento):   
                    cuarto(elemento, principal)
                    break

            lista = reg3.findall(line)
            for elemento in lista:
                 if re.search(regex3,elemento):                    
                    cuarto(elemento, principal)                    
                    break
                     
            lista = reg4.findall(line)
            for elemento in lista:
                 if re.search(regex4,elemento):   
                    cuarto(elemento, principal)
                    break

            lista = reg5.findall(line)
            for elemento in lista:
                 if re.search(regex5,elemento):   
                    cuarto(elemento, principal)
                    break
 
            lista = reg6.findall(line)
            for elemento in lista:
                 if re.search(regex6,elemento):
                    cuarto(elemento, principal)
                    break

            lista = reg7.findall(line)
            for elemento in lista:
                 if re.search(regex7,elemento):
                    cuarto(elemento, principal)
                    break
     
            lista = reg8.findall(line)
            for elemento in lista:
                 if re.search(regex8,elemento):
                    cuarto(elemento, principal)
                    break

            lista = reg9.findall(line)
            for elemento in lista:
                 if re.search(regex9,elemento):
                    cuarto(elemento, principal)
                    break 

            lista = reg10.findall(line)
            for elemento in lista:
                 if re.search(regex10,elemento):
                    cuarto(elemento, principal)
                    break                              
elif(opci==5):
   #Reconoce el ejemplo y una ligera combinacion del ejemplo que es cambiar las operaciones de MULPLICACIONES Y DIVISION
   #POR RESTA O SUMA y viceversa 
   regex = r"\s[\d|a-z]\s[\*|\/]\s[d|a-z]\s[\+|\-]\s\(\s\(\s[\d|a-z]\s[\*\|\/]\s[\d|a-z]\s\)\s[\+|\-]\s[\d|a-z]\s\)"
   reg =re.compile(regex) 
   regex1 = r"\s[\d|a-z]\s[\+|\-]\s[d|a-z]\s[\*|\/]\s\(\s\(\s[\d|a-z]\s[\+|\-]\s[\d|a-z]\s\)\s[\*|\/]\s[\d|a-z]\s\)"
   reg1 =re.compile(regex1) 
   for line in textfile:
            lista = reg.findall(line)
            for elemento in lista:
                 if re.search(regex,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[13:14]+" "+elemento[15:16]+" "+elemento[17:18])
                     print("_t1 = _t0 "+elemento[21:22]+" "+elemento[23:24])
                     print("_t2 = "+elemento[1:2]+" "+elemento[3:4]+" "+elemento[5:6])
                     print("_t3 = _t1 "+elemento[7:8]+" _t2")
                     print(principal+" = "+"_t3")
                     break

            lista1 = reg1.findall(line)
            for elemento in lista1:
                 print(elemento)
                 if re.search(regex1,elemento):
                     print("Elementos del tripo :"+elemento)
                     print("")
                     print("_t0 = "+elemento[13:14]+" "+elemento[15:16]+" "+elemento[17:18])
                     print("_t1 = _t0 "+elemento[21:22]+" "+elemento[23:24])
                     print("_t2 = "+" _t1 "+elemento[7:8]+" "+elemento[5:6])
                     print("_t3 = "+" _t2 "+elemento[3:4]+" "+elemento[1:2])
                     print(principal+" = "+"t3")
                     break
      #Gracias


