import math 
import numpy as np



gender_detected=[0.2,0.6,0.01,0.008]
for k in range(len(gender_detected)):
    gen = gender_detected[k]
    if gen< 0.5:
        gen = math.floor((1-gen )*100)
    else :
        gen  = math.floor(gen *100)
    gender_detected[k]=gen
print(gender_detected)


L = [1,2,3,5,8,9]

for ele in L :
    ele=ele*2
print(L)