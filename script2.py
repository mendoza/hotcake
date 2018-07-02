num = int(raw_input("Cuantos ocupa: "))
from random import randint
from random import choice

def generar_alfanumerico(num):
    lista_areas = ["0101","0102","0107","0301","0404","0420","0501","0502","0503","0511","0601","0801","0703","1001","1006","1101","1104","1401","1501","1601","1808","1804","1801","1811","1514","1804"]
    lista_alfa = list()
    while len(lista_alfa)<num:
        print 'va por la ---- ', len(lista_alfa)
        encontro = int 
        encontro =0
        for i in range(num):
            par = '%05d'
            new_size = (par % randint(0,99999))
            cadena = lista_areas[randint(0,len(lista_areas)-1)] +"-"+  str(randint(1900,2018)) +"-"+str(randint(10000,99999)) #+"-"+ str(new_size)
            #print cadena
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
                   # print 'no hizo ni pija'
                    encontro=0
        print 'va por la ---- ', len(lista_alfa)
        #print lista_alfa
    return lista_alfa

        
with open("RNP.qls", "w") as file:
    # numero identidad --- Nombre --- codigo postal --- hijos ---- casas ---- carros
    file.write(str(["String", "String", "Int", "String" ,"Int", "Int", "Int"])+'\n')
    file.write(str(["No.Idenitdad", "Nombre", "CodigoPostal","EstadoCivil" ,"Hijos", "Casas", "Carros"])+'\n')
    par = '%' + str(10) + 'd'
    new_size = (par % num)
    file.write(str(new_size)+"\n")
    lista_nombres = ["Lakeesha","Yolonda","Robin","Mel","Laveta","Matilde","Augusta","Louella","Cyrstal","Nikki","Nidia","Floretta","Carla","Deloras","Nana","Corrine","Wilford","Richard","Suzan","Stacy","Adrianna","Olimpia","Darren","Latoya","Valarie","Collene","Walter","Arlette","Claudette","Eloisa","Rheba","Sunni","Hae","Hannelore","Roxane","Ela","Harrison","Allene","Malorie","Diane","Normand","Micheline","Rufina","Jeanelle","Adelia","Shirleen","Nestor","Edwina","Buena","Armanda"]
    lista_estadoCivil = ["Soltero(a)", "Casado(a)", "Viudo(a)", "Divorciado(a)","Comprometido(a)"]
    lista_postal = ["31101", "31301", "32101", "32301", "12101", "12111", "41101", "41202", "21101", "21102", "21103", "21104", "21301", "21112", "51101", "51201", "13101", "13201","11101","12101","33101","14101","14201","34101","15101","15201","42101","42201","43101","43201","16101","16201","22101","22114","52101","52102","23101","23201"]
    print("Empieza el ciclo")
    lista_key = generar_alfanumerico(num)
    lista_key = sorted(lista_key)
    for i in range(num):
        name = choice(lista_nombres)
        codigo_postal  = choice(lista_postal)
        Estado= choice(lista_estadoCivil)
        persona = str(lista_key[i])+"|"+name+"|" + codigo_postal+"|"+ Estado+"|"+str(randint(1,30)) + "|"+str(randint(0,10)) + "|"+str(randint(0,10))+'\n'
        file.write(persona)
    print("termino de cargar los registros :v")
