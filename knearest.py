import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def knearest(data):
    print("Enter Your Weight and Height : ")
    a,b = input().split()
    print("Enter Nearest K : ")
    k = input()
    a = int(a)
    b = int(b)
    k = int(k) 
    n=len(data)
    for i in range(n):
        for j in range(2):
            data[i][j] = int(data[i][j])    
    print(" weight, height, size, ecludedistance")
    for row in data:
             c1=np.sqrt((row[0]-a)**2+(row[1]-b)**2)
             row.append(c1)
             print(row)
    display(data,k)
    
def display(data,k):   
    data.sort(key=lambda x:x[3])
    sizevotes = {}
    for i in range(k):
        if data[i][2] in sizevotes:
            sizevotes[data[i][2]] += 1
        else:
            sizevotes[data[i][2]] = 1
    
    print(sizevotes)
    for x in sizevotes:
        print("Your size is chosen By : ", x, sizevotes[x])
    
    
def getData(file):
    csv_file = csv.reader(open(file))    
    data = []
    print(".........Traine data...........")    
    for row in csv_file:
        data.append(row)        
        print(row)        
    return data
    
def main():
    file = "C:\\Users\\Priyanka\\Downloads\\shopping.csv"
    data = getData(file)         
    knearest(data[1:])  
    
main()


