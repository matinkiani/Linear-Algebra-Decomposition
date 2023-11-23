import numpy as np

mode = int(input("Noe Voroodi dadan ra moshakhas konid:\n1-File\n2-Input\n3-Matrise Pishfarz\n"))


if mode == 1:
    input("Save Your data and press Enter ")
    f = open("data.txt","r")
    n = int(f.readline())
    data = np.empty(shape=(n,n))
    k = 0
    for i in f:
        li = i.split()
        intLi = list(map(int,li)) # Tabdile liste Str be Int?
        data[k]=(intLi)
        k+=1

elif mode == 2:
    n = int(input("Tedade satr va sotun ha ra vared konid!\n"))
    data = np.empty(shape=(n,n))
    print(f"matrise {n}*{n} ra vared konid\n")
    for i in range(n):
        c = input()
        li = c.split()
        intLi = list(map(int,li)) # Tabdile liste Str be Int?
        data[i]=(intLi)


else:
    data = np.empty(shape=(3,3))
    data[0] = [ 2, 6,-2]
    data[1] = [-4, 4, 2]
    data[2] = [ 1, 2, 3]


n = len(data)

choice = int(input("1-Bedune zakhire sazi eghtesadi\n2-Ba zakhire sazi eghtesadi\n"))
if(choice==1):
    A = np.empty(shape=(n,n,n))
    P = np.empty(shape=(n,n,n))
    M = np.empty(shape=(n,n,n))

    A[0] = data

    for i in range(1,n): #sakhte A

        #Sakhte P
        P[i] = np.identity(n)
        maxNum = abs(A[i-1][i-1][i-1])
        maxIndex = i-1
        for j in range(i,n):
            if abs(A[i-1][j][i-1]) > maxNum:
                maxNum = abs(A[i-1][j][i-1])
                maxIndex = j
        P[i][[i-1,maxIndex]] = P[i][[maxIndex,i-1]]


        A[i] = np.dot(P[i],A[i-1]) #Hanooz M zarb nashode!

        #Sakhte M
        M[i] = np.identity(n)
        for j in range(i,n):
            M[i][j][i-1] = -1*(A[i][j][i-1] / A[i][i-1][i-1])

        #Update kardane A
        A[i] = np.dot(M[i],A[i])


    #Matrise U
    U = A[n-1]

    #Matrise M
    MM = np.identity(n)
    for i in range(1,n):
        MM = np.dot(np.dot(M[i],P[i]),MM)

    #Matrise P
    PP = np.identity(n)
    for i in range(1,n):
        PP = np.dot(P[i],PP)

    #Matrise L
    mVarun = np.linalg.inv(MM)
    L =     np.dot(PP,mVarun)




    strAns = f"A[0]:\n{A[0]}\n\n"

    for i in range(1,n):
        strAns+= f"P[{i}]:\n{P[i]}\n\nM[{i}]:\n{M[i]}\n\nA[{i}]:\n{A[i]}\n\n"

    strAns += f"P:\n{PP}\n\nM:\n{MM}\n\nL:\n{L}\n\nU:\n{U}"


    export = int(input("1-Khorooji dar Terminal\n2-Save dar file\n"))
    if export == 1:
        print(strAns)
    else:
        file = open("output.txt","w")
        file.write(strAns)
        file.close()
        print("Results saved!")

    print(L.dot(U))





else:
    A = np.array(data)
    row = np.empty(shape=(n-1))

    for i in range(1,n):


        #P
        maxNum = abs(A[i-1][i-1])
        maxIndex = i-1
        for j in range(i,n):
            if abs(A[j][i-1]) > maxNum:
                maxNum = abs(A[j][i-1])
                maxIndex = j
        A[[i-1,maxIndex]] = A[[maxIndex,i-1]]
        row[i-1]=maxIndex

        #M
        for j in range(i,n):
            A[j][i-1] = -1*(A[j][i-1] / A[i-1][i-1])

        #Update
        for j in range(i,n):
            for k in range(i,n):
                A[j][k]=A[j][k] + (A[j][i-1]*A[i-1][k])


    # U
    U = np.zeros(shape=(n,n))
    for j in range(n):
        for k in range(n):
            if j<=k:
                U[j][k]=A[j][k]



    #M
    M = np.empty(shape=(n,n,n))
    for j in range(1,n):
        M[j]=np.identity(n)
        for k in range(j,n):
            M[j][k][j-1] = A[k][j-1]


    #P
    P = np.empty(shape=(n,n,n))
    for j in range(1,n):
        P[j] = np.identity(n)
        P[j][[j-1,int(row[j-1])]] = P[j][[int(row[j-1]),j-1]]

    #Matrise P
    PP = np.identity(n)
    for i in range(1,n):
        PP = np.dot(P[i],PP)


    #Matrise M
    MM = np.identity(n)
    for i in range(1,n):
        MM = np.dot(np.dot(M[i],P[i]),MM)


    #Matrise L
    mVarun = np.linalg.inv(MM)
    L =     np.dot(PP,mVarun)




    export = int(input("1-Khorooji dar Terminal\n2-Save dar file\n"))

    strAns = f"A[0]:\n{data}\n\n"

    for i in range(1,n):
        strAns+= f"P[{i}]:\n{P[i]}\n\nM[{i}]:\n{M[i]}\n\n"

    strAns += f"P:\n{PP}\n\nM:\n{MM}\n\nL:\n{L}\n\nU (A[{n-1}]):\n{U}"
    if export == 1:
        print(strAns)
    else:
        file = open("output.txt","w")
        file.write(strAns)
        file.close()
        print("Results saved!")
