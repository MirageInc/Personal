import numpy as np
import math

class Expr: # To add: sort out imul, sub, isub, iadd functions; alter show() to allow for Expr-exponents; add Polynomial object with .solve() method; create Parser.
    def __init__(self, terms):
        self.arr = terms
        self.vars = []
        for i in terms:
            for j in range(0, len(i[1])):
                if i[1][j] not in self.vars and type(i[1][j]) == str:
                    self.vars.append(i[1][j])

    def show(self): # Returns evaluable string.
        ns = ''
        count = 1
        for i in self.arr:
            if count > 1:
                ns += '+'
            ns += '('+str(i[0])
            c = 0
            for j in range(0, len(i[1]),2):
                ns += '*('+str(i[1][j])+'**'+str(i[1][j+1])+')'
            ns += ')'
            count += 1
        return ns

    def eval(self, varl): # Evaluates the expression with specific values of each variable.
        if not (len(varl) >= len(self.vars)):
            print("Ill-defined evaluation.")
            return 0
        else:
            ev = self.show()
            for i in range(0, len(self.vars)):
                ev = ev.replace(varl[i][0],str(varl[i][1]))
            return eval(ev)

    def term(self, n): # Returns nth term of expression as an expression object.
        return Expr([self.arr[n-1]])

    def termply(self, t, scale): # Multiplies nth term by scale factor.
        self.arr[t-1][0] *= scale

    def col(self): # Collects like terms.
        l = []
        newarr = []
        for i in self.arr:
            varsl = [i[1][k] for k in range(0, len(i[1]),2)]
            varsl.sort()
            if varsl not in l:
                l.append(varsl)
                scalar = 0
                for j in self.arr:
                    varso = [j[1][k] for k in range(0, len(j[1]),2)]
                    varso.sort()
                    if varsl == varso:
                        scalar += j[0]
                newarr.append([scalar,i[1]])
        self.arr = newarr
    
    def fadd(self, other, exp, k): # Defines addition of expressions.
        if type(other) == int or type(other) == float:
            new = Expr([i for i in self.arr])
            new.arr.append([other*(-1)**exp,[]])
            new.col()
            if k == 1:
                self = new
            if k == 0:
                return new
            
        if type(other) == Expr:
            self.col()
            other.col()
            new = []
            for i in range(0,len(self.arr)):
                found = False
                for j in range(0, len(other.arr)):
                    if self.arr[i][1] == other.arr[j][1]:
                        new.append([self.arr[i][0]+other.arr[j][0]*(-1)**exp,self.arr[i][1]])
                        found = True
                        break
                if found == False:
                    new.append(self.arr[i])
            varl = [new[i][1] for i in range(0, len(new))]
            for i in other.arr:
                if i[1] not in varl:
                    new.append([i[0]*(-1)**exp,i[1]])
            if k == 1:
                self = Expr(new)
            if k == 0:
                return Expr(new)

    def __add__(self, other):
        return self.fadd(other, 0, 0)
    def __sub__(self, other):
        return self.fadd(other, 1, 0)

    def fmul(self, other, exp, k): # Defines multiplication of expressions.
        if type(other) == int or type(other) == float:
            self.col()
            new = []
            for i in self.arr:
                if exp == 0:
                    new.append([i[0]*other,i[1]])
                if exp == 1:
                    new.append([i[0]/other, i[1]])
            if k == 1:
                self = Expr(new)
            if k == 0:
                return Expr(new)

        if type(other) == Expr:
            self.col()
            other.col()
            new = []
            for i in range(0, len(self.arr)):
                for j in range(0, len(other.arr)):
                    newt = []
                    if exp == 0:
                        newt.append(self.arr[i][0]*other.arr[j][0])
                    if exp == 1:
                        newt.append(self.arr[i][0]/other.arr[j][0])
                    newt.append([])
                    for k in range(0, len(self.arr[i][1]),2):
                        found = False
                        for r in range(0, len(other.arr[j][1]),2):
                            if self.arr[i][1][k] == other.arr[j][1][r]:
                                newt[1].append(self.arr[i][1][k])
                                newt[1].append(self.arr[i][1][k+1]+other.arr[j][1][r+1]*(-1)**exp)
                                found = True
                                break
                        if found == False:
                            newt[1].append(self.arr[i][1][k])
                            newt[1].append(self.arr[i][1][k+1])
                    varl = [newt[1][k] for k in range(0, len(newt[1]),2)]
                    for k in range(0,len(other.arr[j][1]),2):
                        if other.arr[j][1][k] not in varl:
                            newt[1].append(other.arr[j][1][k])
                            newt[1].append(other.arr[j][1][k+1])
                    new.append(newt)
            if k == 1:
                self = Expr(new)
            if k == 0:
                return Expr(new)

    def __mul__(self, other):
        return self.fmul(other, 0, 0)
    def __truediv__(self, other):
        return self.fmul(other, 1, 0)

class Matrix:
    def __init__(self, dimensions, values):
        self.dim = dimensions
        self.val = values
        if len(self.val) < self.dim[0]*self.dim[1]:
            for i in range(0, self.dim[0]*self.dim[1]-len(self.val)):
                self.val.append(0)
        self.mat = np.zeros(dimensions)
        self.update()
        
    def update(self):
        row = -1
        for i in range(0, len(self.val)):
            if i%self.dim[1] == 0:
                row += 1
            self.mat[row][i%self.dim[1]] = self.val[i]
    
    def show(self):
        print(self.mat)

    def comp(self, other, exp, k):
        if self.dim != other.dim:
            print("Invalid dimensions.")
        else:
            new = Matrix(self.dim, self.val)
            for i in range(0, len(new.val)):
                new.val[i] += other.val[i]*(-1)**exp
            new.update()
            if k == 1:
                self = new
            if k == 0:    
                return new

    def __add__(self, other):
        return self.comp(other, 2, 0)
        
    def __iadd__(self, other):
        return self.comp(other, 2, 1)

    def __sub__(self, other):
        return self.comp(other, 1, 0)
    def __isub__(self, other):
        return self.comp(other, 1, 1)

    def __mul__(self, other):
        if self.dim[1] != other.dim[0]:
            print("Invalid dimensions.")
        else:
            new = Matrix([self.dim[0], other.dim[1]], [])
            for row in range(0, new.dim[0]):
                for col in range(0, new.dim[1]):
                    for k in range(0, self.dim[1]):
                        new.mat[row][col] += self.mat[row][k]*other.mat[k][col]
            return new

b = Expr([[2,['x',1,'y',3]],[10,['z',1]]])

