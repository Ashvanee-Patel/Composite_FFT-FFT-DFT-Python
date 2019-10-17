"""--------------------------DFT || FFT || composite FFT--------------------------------
--------------------------This is the code of composite FFT ---------------------------------
------------------------------Ashvanee Patel || July 2018-----------------------------------"""
#---------------------------------------------------------------------------------------------------
"""
FFT (Fast Fourier Transformation): 
A FFT algorithm computes the Discrete Fourier Transform (DFT) of a sequence,
Fourier analysis converts a signal from its original domain (often Time or space) to a frequency domain and vice versa. 
It’s manages reduce the complexity of computing the DFT,
If we applies the definition of DFT, then compute complexity O (n log n) .
The complexity of the FFT is O (n2), n is the size of data size.
"""
import math

def fft(D):
    Df = []        # For FFT OutPut
    N =  len(D)
    def fun1():
        X = []
        pi = 180
        b = 0
        while(b < m):
            X.append([])
            k1 = 0
            while(k1 < N1):
                X[b].append(k1)
                X[b][k1] = 0
                DFT = 0
                for n in range(0,(N1-1)+1):
                    sr = math.cos(math.radians(2*pi*n*m*k1/N))
                    si = math.sin(math.radians((-1)*2*pi*n*m*k1/N))*(1j)
                    w = sr + si
                    DFT = DFT + (D[(m*n) + b])*w
                X[b][k1] = DFT
                k1 = k1+1
            b = b+1



        k = 0
        c = 0
        while(k < N):
            FFT = 0
            if(c == N1):
                c = 0
            for b in range(0,m):
                sr = math.cos(math.radians(2*pi*b*k/N))
                si = math.sin(math.radians((-1)*2*pi*b*k/N))*(1j)
                w = sr + si
                FFT = FFT + (X[b][c])*w
            Df.insert(k,FFT)

            c = c+1
            k = k +1 #"""

        #print(Df)


    if(N>1):
        x = []
        for i in range (1,int(N/2)+1):
            if((N%i)==0):
                x.append(i)
            else:
                x = x
        y = len(x)
        a = int(y/2)

        if(y==1):
            m = x[a]
            N1 = N
            fun1()
            print(Df)

        elif((y%2)==0):
            N1 = m = x[a]
            fun1()
            print(Df)

        else:
            m = x[a]
            N1 = x[a+1]
            fun1()
            print(Df)

    else:
        print("FFT Result  : ",D[0])

    
