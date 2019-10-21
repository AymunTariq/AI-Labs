import numpy as np
import math

class Complex():
    def __init__(self, r, i):
        self.Real = r
        self.Imaginary = i
    def magnitude(self):
        mag =  math.sqrt((self.Real)**2 + (self.Imaginary)**2)
        return print(mag)
    def orientation(self):
        if(self.Imaginary ==0):
            print("undefined")
        elif(self.Real ==0):
            print("undefined")
        else:
            ori =  math.atan(self.Imaginary/self.Real)
            return print(ori);
    def printComplex(self):
        print(str(self.Real) + " + " + str(self.Imaginary) + "i" )
#
# r= int(input("enter real"))
# i=int(input("enter img"))
# comp = Complex(r,i)
# comp.magnitude()
# comp.orientation()


#########################  task2 ###################

def DFT8point(x):
    M = len(x[0])
    X = np.zeros([1, M], dtype = Complex)
    N=8;

    for n in range(0, M-1):
        sum = Complex(0, 0)
        for k in range(0, N+1):
            com = Complex(math.cos(2*math.pi*k*n/8),-math.sin(2*math.pi*k*n/8) )
            com.Real = x[0][k] * com.Real
            com.Imaginary = x[0][k] * com.Imaginary
            sum.Real = sum.Real + com.Real
            sum.Imaginary = sum.Imaginary + com.Imaginary

        X[0][n] = sum
    return X

x = np.ones([1, 9], dtype= float)
x = 2*x
X = DFT8point(x)

for i in range(0,9):
    X[0][i].printComplex();
    X[0][i].magnitude();
    X[0][i].orientation();



#################### task3 ##################

#
class Tree():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        # self.searchVar = x
    # def search(self,searchVar):
    #     if(searchVar==self.data):
    #         print("Key found: "+ self.data)
    #     elif(searchVar<self.data):
    #         print(self.left.s)



root = Tree()
root.data = 8
root.left = Tree()
root.left.data = 3
root.right = Tree()
root.right.data = 10

root.left.left = Tree()
root.left.left.data = 1
root.left.right = Tree()
root.left.right.data = 6

root.left.right.left = Tree()
root.left.right.left.data = 4

root.left.right.right = Tree()
root.left.right.right.data = 7

root.right.right = Tree()
root.right.right.data = 14

root.right.right.left = Tree()
root.right.right.left.data = 13

print(root.right.right.left.data);
