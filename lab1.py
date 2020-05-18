from math import sqrt
import csv


def leerArchivo():
    users = []
    movs = {}
    usuario=[]
    with open('Movie_Ratings.csv') as File:
        reader = csv.reader(File, delimiter=',',lineterminator='\n',
                            quoting=csv.QUOTE_MINIMAL)
        
        for row in reader:
            if len(users) == 0:
                for i in range(1,len(row)):
                    users.append(row[i])
            else:
                for j in range(1,len(row)):
                    if(row[j]==''):
                        movs[row[0]]=row[j]
                    else:
                        movs[row[0]]=float(row[j])
                    usuario.append(movs.popitem())
                    
        x=len(usuario)/len(users)

        user_={}
        for j in range(len(users)):
            dicc={}
            for i in range(j,len(usuario),int(x)):
              key,value= usuario[i]
              if(value!= ''):
                dicc[key]=value
            user_[users[j]] = dicc

    return user_

    

def manhattan(r1, r2):
    dist = 0
    total = 0
    for key in r1:
        if key in r2:
            dist += abs(r1[key] - r2[key])
            total += 1
    if total > 0:
        return dist 
    else:
        return -1 #No hay rating en comun

def Euclidiana(r1, r2):
    dist = 0
    total = 0
    for key in r1:
        if key in r2:
            dist += pow( r1[key] - r2[key],2)
            total += 1
    if total > 0:
        return sqrt(dist)
    else:
        return -1 #No hay rating en comun

def Minkowski(r1, r2,r):
    dist = 0
    total = 0
    for key in r1:
        if key in r2:
            dist += pow( abs(r1[key] - r2[key]),r)
            total += 1
    if total > 0:
        if r != 0: 
            return pow(dist,1/r)
        else:
            return -1
    else:
        return -1 #No hay rating en comun





usuariosExcel=leerArchivo()
print("Manhatan:")
print(manhattan(usuariosExcel["Patrick C"],usuariosExcel["Thomas"]))
print("Euclidiana:")
print(Euclidiana(usuariosExcel["Patrick C"],usuariosExcel["Thomas"]))
print("Minkowski:")
print(Minkowski(usuariosExcel["Patrick C"],usuariosExcel["Thomas"],1))
