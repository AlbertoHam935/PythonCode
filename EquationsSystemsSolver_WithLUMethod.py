'''
Este programa obtiene la solucion de un sistema de ecuaciones 
utilizando de apoyo el metodo de descomposicion LU

@autor:Alberto Ham 


'''
import math 
 
def DesLU(A):
    m=len(A)
    
    #asignamos 1 a la matriz L en diagonal principal 
    for i in range (m):
        L[i][i]=1
#Hacemos el escalonamiento 
    g=0
    for k in range(m-1):

        for i in range(k+1,m):

           #Obtenemos a L 
            for g in range(1,m):
                L[g][i-1]=U[g][i-1]/U[k][k]

            factor=U[i][k] / U[k][k]
            #Obtenemos a u 
            for j in range(m):
                 U[i][j]=U[i][j]-(factor*U[k][j])
        k=k+1
    

#Incio del codigo principal 

#Listas de apoyo en el codigo 
A=[]
L=[]
U=[]
B=[]
D=[]
X=[]


#Solo se solicita una dimension porque el sistema debe ser cuadrado
#para exista una solucion 
n=int(input("Dame las columnas y filas: "))

i=0
j=0


print("Ingresa la Matriz A (Coeficientes):")
for i in range(n):
  A.append([])
  U.append([])
  L.append([])
  for j in range (n):
    print("elemento a",i+1,j+1,":")
    v=float(input())
    A[i].append(v)
    U[i].append(v)
    L[i].append(0) 
print("Ingresa la matriz B(terminos independientes):")

for i in range(n):
    B.append(float(input()))

DesLU(A)  

#inicializamos a X y D 

for i in range(n):
  X.append(0)
  D.append(0)


#Hacemos el primer sistema [L][D]=[B]
D[0]=B[0]

for i in range(1,n):
  suma=0
  for j in range(n):
    suma=suma+L[i][j]*D[j]

  D[i]=(B[i]-suma)/L[i][i]


#Hacemos el segundo sistema [U][X]=[D]


X[n-1]=D[n-1]/U[n-1][n-1]

for i in range(n-2,-1,-1):
  suma2=0
  for j in range(n):
    suma2=suma2+U[i][j]*X[j]

  X[i]=(D[i]-suma2)/U[i][i]




#Imprimimos la matriz A, B y X 

print("La matriz A:")

for i in range(n):

    print(A[i])

print("El vector B:")
for i in range(n):

    print(B[i])


print("Las soluciones del sistema son: ")
for i in range(n):
    print(X[i])

