"""
Created on Wed Dec 21 18:45:44 2022

@author: Alberto Ham

Implementacion para metodo de factores cuadraticos 
"""

from numpy.polynomial.polynomial import Polynomial 
import math

#Creamos la funcion que nos otorga division de polinomios 
def div(p1, p2):

    #Conviertes los coeficientes a polinomios 
    Polinomio1=Polynomial(coef=p1)
    Polinomio2=Polynomial(coef=p2)
    
    y=Polinomio1//Polinomio2
    
    return y 

#Creamos programa que nos obtiene raices de polinomio cuadratico

def F_General(a,b,c):
    
    R=[]
    D=(pow(b,2))+(-1*4*(a*c))
    
    if D>=0:
        
        x1=(-1*b+math.sqrt(D))/(2*a)
        x2=(-1*b-math.sqrt(D))/(2*a)
        R=[x1,x2]
      
       
        
    else:
       
        b1=((math.sqrt(-1*D))/(2*a))
        a1=-1*b/(2*a)
   
        z1=complex(a1,b1)
        z2=complex(a1,-b1)
        
        R=[z1,z2] 
    return R

#Funcion que resuelve un sistema de ecuaciones de grado 2


#Vector de coeficientes, terminos Indepente
# , Vector incognitas a grabar y filas y columnas    
def Sol_sis(A,B,X,n,m):
    #inicializacion de la matriz X
    X.clear()
    for i in range(n):
        X.append(0)

    #escalonamiento 
    for k in range(m-1):
    
      for i in range(k+1,m):
        factor=A[i][k]/A[k][k]
    #modificamos el valor del vector B y se asigna a la misma posicion 
    
        B[i]=B[i]-factor*B[k]
    
        for j in range(n):
          A[i][j]=A[i][j]-(factor*A[k][j])
      k=k+1
    
    #sustitucion 
    
    #Hacemos las sustituciones correspondientes
    X[m-1]=B[m-1]/A[m-1][m-1]
    
    
    #Hacemos las segundas sustituciones
    for i in range(m-2,-1,-1):
      suma=0
      for j in range(n):
        suma=suma+A[i][j]*X[j]
    
      X[i]=(B[i]-suma)/A[i][i]
      

########################### Inicio de programa ##########################
A=[]
B=[]
C=[]
X=[]
A_1=[]
B_1=[]
P_1=[]
S_EC=[]
S=[]


n=int(input("Dame el grado del polinomio: "))

print("Ingresa los coeficientes de menor a mayor ")
print("iniciando por el termino Independiente:")
for i in range(n+1):
    
    A.append(float(input()))
    
Pol_O=Polynomial(coef=A) 
n=len(A)-1
Error_fijo=0.1

while (n>2):
    r=1
    s=1
    Er=1000000
    Es=1000000
    count=0

    while Er>.1 and Es>.1 :
        B.clear()
        C.clear()
        for i in range(n+1):
            B.append(0)
            C.append(0)

        #Hacemos las asignaciones del B y C 
        B[n]=A[n]
        B[n-1]=A[n-1]+r*B[n]
        
        for j in range(n-2,-1,-1):
            B[j]=A[j]+r*B[j+1]+s*B[j+2]
            
        C[n]=B[n]
        C[n-1]=B[n-1]+r*C[n]
        
        
        for g in range(n-2,-1,-1):
            C[g]=B[g]+r*C[g+1]+s*C[g+2]

        #Asignamos el sistema de ecuaciones
        A_1.clear()
        B_1.clear()

        A_1=[ [C[2], C[3]],[ C[1], C[2]] ]
        B_1=[-1*B[1], -1*B[0]]
        
        
        #Resolvemos el sistema
        Sol_sis(A_1, B_1, X, 2, 2)
        
        r_1=r+X[0]
        s_1=s+X[1]
        
        Er=abs((X[0]/r_1))*100
        Es=abs((X[1]/s_1))*100
        
       # print("Esto es rs",r,s)
        r=r_1
        s=s_1
        count=count+1
    #Obetenmos el polinomio para la division
    P_1=[-1*s,-1*r,1]
   
    #agregamos las soluciones de ese polinomio a la lista
    S=F_General(P_1[2],P_1[1],P_1[0])
    for i in range(2):
        S_EC.append(S[i])

    A=div(A,P_1).coef
      
    n=len(A)-1

#*** Este procedimiento se repite hasta tener un polinomio cuadratico o lineal***

#El polinopmio final entra a una de las opciones dependiendo si es lineal 
#o si es cuadratico y se agregan las raices
if (len(A)-1)==2:

    raizU=F_General(A[2],A[1],A[0])
    for i in range(2):  
        S_EC.append(raizU[i])


else:
   
    raizU=(-1*A[0])/A[1]
    S_EC.append(raizU)

print("El polinomio es:",Pol_O)
print("Las raices son:")
print(S_EC)




    



    















