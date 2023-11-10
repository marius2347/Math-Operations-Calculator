# --- Math Operations Calculator ---
from typing import List, Any

# modules
import numpy as np
import math as mt

from numpy import ndarray, dtype


# classes


# class for arithmetic functions
class Arithmetic:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y


# class for algebra functions


class Algebra:
    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def absolute(self):
        return np.absolute(self.x)

    def square_root(self):
        return np.sqrt(self.x)

    def radical(self):
        return self.x ** (1 / self.y)

    def exponent(self):
        return self.x ** self.y

    def logarithm(self):
        return mt.log(self.y, self.x)

    def factorial(self):
        return mt.factorial(self.x)

    def modulus(self):
        return self.x % self.y


# functions for matrix


def matrixProduct(AFirstLine, ASecondLine, AThirdLine, BFirstLine, BSecondLine, BThirdLine):
    return np.array((AFirstLine, ASecondLine, AThirdLine)) @ np.array((BFirstLine, BSecondLine, BThirdLine))


def matrixTranspose(matrixParameter):
    return matrixParameter.T


def matrixDeterminant(matrixP):
    return np.linalg.det(matrixP)


# class for linear algebra functions
class LinearAlgebra:
    def __init__(self, x: List, y: List):
        self.x = x
        self.y = y

    def vectorAddition(self) -> List:
        ListVectors = []
        for a, b in zip(self.x, self.y):
            ListVectors.append(a + b)
        return ListVectors

    def crossProduct(self):
        return np.cross(self.x, self.y)

    def dotProduct(self):
        return np.dot(self.x, self.y)


# class for set functions
class Set:
    def __init__(self, x: set, y: set):
        self.x = x
        self.y = y

    def union(self):
        return self.x.union(self.y)

    def intersection(self):
        return self.x.intersection(self.y)


# input select operation type
print("Please choose a type of operation!")
inputOperation = input(
    "For Arithmetic Type 1: Addition, Subtraction, Multiplication & Division Operator\nFor Algebra Type 2: Absolute "
    "Value, Square Root, Radical, Exponent,"
    "Logarithm, Factorial & Modulus\nFor Linear Algebra Type 3: Vector Addition, "
    "Cross Product, Dot Product, "
    "Matrix Multiplication, Transpose & Determinant Operator\nFor Set Type 4: Union Operator & Intersection "
    "Operator\nNumber of operation: ")

# conditions for operation type
inputOperator = ""
print("\nNow choose an operator!")
if inputOperation == "1":
    inputOperator = input("Addition Operator - 1, Subtraction Operator - 2, Multiplication Operator - 3, "
                          "Division Operator - 4\nNumber of operator: ")
elif inputOperation == "2":
    inputOperator = input("Absolute Value Operator - 1, Square Root Operator - 2, Radical Operator - 3, Exponent "
                          "Operator - 4, "
                          "Logarithm Operator - 5, Factorial Operator - 6, Modulus Operator - 7\nNumber of operator: ")
elif inputOperation == "3":
    inputOperator = input("Vector Addition Operator - 1, Cross Product Operator - 2, "
                          "Dot Product"
                          " Operator - 3, Matrix Multiplication Operator - 4, Matrix Transpose Operator - 5, "
                          "Matrix Determinant - 6 "
                          "\nNumber of operator: ")
elif inputOperation == "4":
    inputOperator = input("Union Operator - 1, Intersection Operator - 2\nNumber of operator: ")
else:
    print("Wrong operation type!")

# arithmetic operations
opArithmetic = ""
opArithmeticBool = False
if inputOperation == "1":
    opArithmeticBool = True
    print("Please type your numbers down here: ")
    List = list(map(float, input().split()))
    opArithmetic = List[0]
    for i in range(0, len(List) - 1):
        operationArithmetic = Arithmetic(opArithmetic, List[i + 1])
        if inputOperator == "1":
            opArithmetic = round(operationArithmetic.addition(), 2)
        if inputOperator == "2":
            opArithmetic = round(operationArithmetic.subtraction(), 2)
        if inputOperator == "3":
            opArithmetic = round(operationArithmetic.multiplication(), 2)
        if inputOperator == "4":
            opArithmetic = round(operationArithmetic.division(), 2)

# algebra operations
opAlgebra = []
opAlgebraF = []
if inputOperation == "2":
    operationAlgebra = Algebra(opAlgebra)
    if inputOperator == "3":
        print("Please type firstly the root number and secondly the nth root: ")
        a, b = input().split()
        operationAlgebra = Algebra(int(a), int(b))
    elif inputOperator == "4":
        print("Please type firstly base number and the power number: ")
        a, b = input().split()
        operationAlgebra = Algebra(int(a), int(b))
    elif inputOperator == "5":
        print("Please type firstly base number and the operand number: ")
        a, b = input().split()
        operationAlgebra = Algebra(int(a), int(b))
    elif inputOperator == "7":
        print("Please type firstly the numerator and secondly the denominator: ")
        a, b = input().split()
        operationAlgebra = Algebra(int(a), int(b))
    else:
        print("Please type your numbers down here: ")
        if inputOperator == "6":
            opAlgebraF = list(map(int, input().split()))
        else:
            opAlgebra = list(map(float, input().split()))
            operationAlgebra = Algebra(opAlgebra)

    if inputOperator == "1":
        opAlgebra = [round(x, 2) for x in operationAlgebra.absolute()]
    if inputOperator == "2":
        opAlgebra = [round(x, 2) for x in operationAlgebra.square_root()]
    if inputOperator == "3":
        opAlgebra = operationAlgebra.radical()
    if inputOperator == "4":
        opAlgebra = operationAlgebra.exponent()
    if inputOperator == "5":
        opAlgebra = operationAlgebra.logarithm()
    if inputOperator == "6":
        for x in opAlgebraF:
            operationAlgebra = Algebra(x)
            opAlgebra.append(operationAlgebra.factorial())
    if inputOperator == "7":
        opAlgebra = operationAlgebra.modulus()

# linear algebra operations
opLinearAlgebra = []
opLinearAlgebraBool = False
if inputOperation == "3":
    opLinearAlgebraBool = True
    if inputOperator == "1" or inputOperator == "2" or inputOperator == "3":
        print("Type the two vectors one below the other: ")
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        operationAlgebra = LinearAlgebra(a, b)
        if inputOperator == "1":
            opLinearAlgebra = operationAlgebra.vectorAddition()
        if inputOperator == "2":
            opLinearAlgebra = operationAlgebra.crossProduct()
        if inputOperator == "3":
            opLinearAlgebra = operationAlgebra.dotProduct()
    elif inputOperator == "4":
        print("Type the first matrix 3 / 3:")
        A = list(map(int, input().split()))
        Aa = list(map(int, input().split()))
        Aaa = list(map(int, input().split()))
        print("Type the second matrix 3 / 3:")
        B = list(map(int, input().split()))
        Bb = list(map(int, input().split()))
        Bbb = list(map(int, input().split()))
        opLinearAlgebra = matrixProduct(A, Aa, Aaa, B, Bb, Bbb)
    elif inputOperator == "5":
        print("Type the matrix 3 / 3:")
        A = list(map(int, input().split()))
        Aa = list(map(int, input().split()))
        Aaa = list(map(int, input().split()))
        matrix = np.array((A, Aa, Aaa))
        opLinearAlgebra = matrixTranspose(matrix)
    elif inputOperator == "6":
        print("Type the matrix 3 / 3:")
        A = list(map(int, input().split()))
        Aa = list(map(int, input().split()))
        Aaa = list(map(int, input().split()))
        opLinearAlgebra = matrixDeterminant(np.array((A, Aa, Aaa)))

# set operations
opSetBool = False
if inputOperation == "4":
    opSetBool = True
    print("Please type the first set of numbers: ")
    A = set(map(int, input().split()))
    print("Please type the second set of numbers: ")
    B = set(map(int, input().split()))
    opSet = Set(A, B)
    if inputOperator == "1":
        print(opSet.union())
    elif inputOperator == "2":
        print(opSet.intersection())

# results of arithmetic, algebra, linear algebra and set operations
if opArithmeticBool:
    print("The result of Arithmetic Operation is: {}".format(opArithmetic))

try:
    if len(opAlgebra):
        print("The result of Algebra Operation is: {}".format(opAlgebra).replace("[", "").replace("]", ""))
except:
    if opAlgebra or inputOperator == "3" or inputOperator == "5" or inputOperator == "7":
        print("The result of Algebra Operation is: {}".format(round(opAlgebra, 2)))

if opLinearAlgebraBool:
    print("The result of Linear Algebra Operation is: {}".format(opLinearAlgebra))
