


import numpy as np


def conv2D(input,kernel,stride = 1,padding = 0):
    
    H = len(input)
    W = len(input[0])
    
    Kh = len(kernel)
    Kw = len(kernel[0])
    
    Hi = H + 2*padding
    Wi = W + 2*padding
    
    inp = [[0 for _ in range(Wi)] for _ in range(Hi)]
    
    for i in range(H):
        
        for j in range(W):
            
            inp[i+padding][j+padding] = input[i][j]    
    
    OH = ((H - Kh + 2*padding) // stride) + 1
    OW = ((W - Kw + 2*padding) // stride) + 1 
    
    Output = [[0 for _ in range(OW)] for _ in range(OH)]
    
    
    for i in range(OH):
        
        for j in range(OW):
            
            temp = 0
            
            for x in range(Kh):
                
                for y in range(Kw):
                    
                    temp += inp[i*stride + x][j*stride + y] * kernel[x][y]
                    
            
            Output[i][j] = temp
            
            
    return Output


def Util():
    
    input = [[2,3,6,9],
             [1,9,5,1],
             [4,7,8,5]]
    
    kernel = [[1,2],
              [3,1]]
    
    
    out = conv2D(input=input,kernel=kernel,stride=1,padding=1)
    
    for i in range(len(out)):
        
        for j in range(len(out[0])):
            
            print(out[i][j],end=" ")
        
        print("\n")
        
        
Util()