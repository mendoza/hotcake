num = 100000
from random import randint
from random import choice

def generar_alfanumerico(num):
    
    lista_abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lista_numeros = ["1","2","3","4","5","6","7","8","9"]

    lista_alfa = list()

    while len(lista_alfa)<num:
        print 'va por la ---- ', len(lista_alfa)

        encontro = int 
        encontro =0
        for i in range(num):
            
            cadena = lista_abecedario[randint(0,len(lista_abecedario)-1)] + lista_numeros[randint(0,len(lista_numeros)-1) ] + lista_abecedario[randint(0,len(lista_abecedario)-1)] +  lista_numeros[randint(0,len(lista_numeros)-1) ] + lista_abecedario[randint(0,len(lista_abecedario)-1)] +  lista_numeros[randint(0,len(lista_numeros)-1) ] 

            if(len(lista_alfa)==0):
                print 'estaba vacia'
                lista_alfa.append(cadena)
            else:
                #for m in range (len(lista_alfa)):
                if cadena in lista_alfa:
                    encontro +=1
                    #print encontro
                
                if encontro == 0:
                    lista_alfa.append(cadena)
                    #print 'no encontro'
                    encontro=0
                else:
                    print 'no hizo ni pija'
                    encontro=0
        print 'va por la ---- ', len(lista_alfa)
        #print lista_alfa

    return lista_alfa

        
with open("Nuevo.qls", "w") as file:
    file.write(str(["String", "String", "String", "Int", "String", "String"])+'\n')
    file.write(str(["ID", "Nombre", "Apellido", "Edad", "Email", "Sexo"])+'\n')
    file.write(str(num)+"\n")
    lista_nombres = ["Lakeesha","Yolonda","Robin","Mel","Laveta","Matilde","Augusta","Louella","Cyrstal","Nikki","Nidia","Floretta","Carla","Deloras","Nana","Corrine","Wilford","Richard","Suzan","Stacy","Adrianna","Olimpia","Darren","Latoya","Valarie","Collene","Walter","Arlette","Claudette","Eloisa","Rheba","Sunni","Hae","Hannelore","Roxane","Ela","Harrison","Allene","Malorie","Diane","Normand","Micheline","Rufina","Jeanelle","Adelia","Shirleen","Nestor","Edwina","Buena","Armanda"]
    lista_apellidos = ["Robles", "Maldonado", "House", "Dunlap", "Dudley", "Rowe", "Howell", "Phelps", "Mcgrath", "Watkins", "Mitchell", "Davila", "Marshall", "Church", "Henson", "Bright", "Wilson", "Lynn","Cohen","Strickland","Landry","Parker","Adams","Avery","Galvan","Pope","Tate","Ortiz","Rivera","Bailey","Goodwin","Reed","Bond","Mendoza","Morrow","Bradshaw","Page","Hess","Baker","Rodgers","Ritter","Fritz","Vaughan","Mclean","Montgomery","Huynh","Montes","Crawford","Durham","Chase"]
    print("Empieza el ciclo")
    lista_key = generar_alfanumerico(num)
    for i in range(num):
        name = choice(lista_nombres)
        apellido  = choice(lista_apellidos)
        persona = str(lista_key[i])+"|"+name+"|" + apellido+"|"+str(choice(range(1,90))) + "|"+str(name+"@unitec.edu") + "|"+str(randint(0,1))+'\n'
        file.write(persona)
    print("termino de cargar los registros :v")