import numpy as np

skaler=np.array(5) #nokta
vektorel=np.array([5,10]) #tek boyutlu
matris=np.array([[1,2,3],[77,8,9],[4,6,5]]) #eni boyu olan yapi
tensor=np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]]) #cok boyutlu
print(skaler)
print(vektorel)
print(matris)
print(tensor)

sayilar=np.array([1,2,3,4,"alper"])
print(sayilar.dtype) #veri cinsi alindi

print(np.identity(6)) #kösegen matris yapti
print(np.eye(5,k=1)) #1 birim köse matrisi oteledi


