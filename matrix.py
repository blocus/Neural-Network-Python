#! /usr/bin/python
import random

def isnan(x):
    if not isinstance(x, int):
        return False
    if not isinstance(x, float):
        return False
    if not isinstance(x, complex):
        return False
    return True


class Matrix():
    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.matrix = []
        for i in range(self.rows):
            tmp = []
            for j in range(self.cols):
                tmp.append(0)
            self.matrix.append(tmp)

    def show(self, presision = 2):
        leng = []
        for j in range(self.cols):
            max = 0
            for i in range(self.rows):
                x = self.matrix[i][j]
                if x - int(x) != 0:
                    x = round(x, presision)
                x = str(x)
                l = len(x)
                xSplt = x.split('.')
                if len(xSplt) == 2:
                    l = len(xSplt[0])+presision+1
                if l > max:
                    max = l
            leng.append(max)
        for i in range(self.rows):
            s = ""
            for j in range(self.cols):
                x = self.matrix[i][j]
                e = str(x)
                if x - int(x) != 0:
                    e = str(round(x, presision))
                else:
                    e = str(int(x))
                l = len(e)
                s += " " * (leng[j] - l) + e + "   "
            print s
        print "-"*64

    def randomize(self, start = -1, stop = 1, type = "f"):
        for i in range(self.rows):
            for j in range(self.cols):
                r = random.random() * 2 - 1
                if type == "f":
                    r = random.random() * (stop-start) + start
                elif type == "d":
                    r = random.randint(start, stop)
                self.matrix[i][j] = r

    def addNumber(self, x = 0):
        if isnan(x):
            print "arg is not a number"
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] += x
        return True

    def multiplyNumber(self, x = 0):
        if isnan(x):
            print "arg is not a number"
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] *= x
        return True

    def add(self, B):
        if not isinstance(B, Matrix):
            print "arg is not a Matrix"
            return False
        if self.cols != B.cols or self.rows != B.rows:
            print "the two matrix are different size"
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] += B.matrix[i][j]
        return True

    def setList(self, L):
        tmp = []
        if not isinstance(L, list):
            return False
        nb = 0
        for l in L:
            if not isinstance(l, list):
                return False
            t = []
            if len(l) > nb:
                nb = len(l)
            for e in l:
                if isnan(e):
                    return False
                t.append(e)
            tmp.append(t)
        for i in range(len(tmp)):
            l = len(tmp[i])
            tmp[i] += [0]*(nb - l)
        self.matrix = tmp
        self.rows = len(tmp)
        self.cols = nb
        return True

    def multiply(self, B):
        if not isinstance(B, Matrix):
            print "arg is not a Matrix"
            return False
        if self.cols != B.rows:
            print "Can't multiply "+str(self.rows)+"x"+str(self.cols)+" * "+str(B.rows)+"x"+str(B.cols)
            return False
        tmp = []
        for i in range(self.rows):
            tmp.append([])
            for j in range(B.cols):
                t = 0
                for k in range(self.cols):
                    t += (self.matrix[i][k] * B.matrix[k][j])
                tmp[i].append(t)
        self.matrix = tmp
        self.cols = B.cols
        return True

    def identity(self, n):
        if isnan(n):
            return False
        tmp = Matrix(n, n)
        for i in range(n):
            tmp.matrix[i][i] = 1
        self.matrix = tmp.matrix
        self.rows = n
        self.cols = n

    def isId(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if i == j and self.matrix[i][j] != 1:
                    return False
                if i != j and self.matrix[i][j] != 0:
                    return False
        return True



M = Matrix(5, 5)
M1 = Matrix(2, 5)
M.randomize(-4, 4, "d")
# M1.randomize(-4, 4, "d")
M1.identity(5)

M.show()
M1.show()
M.multiply(M1)
M.show()

print M1.isId()
print M.isId()

# print M.matrix
