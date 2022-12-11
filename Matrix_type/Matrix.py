'''Mobin Azadani Ap E4 Q2'''

import unittest
class Integer:
    def __init__(self,number):
        self.number = number
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self,value):
        
        if isinstance(value,int):
            self._number = value
        elif isinstance(value,str):
            if not value.strip().isnumeric():
                raise ValueError('value must be an integer')
            self._number = int(value.strip())
        else:
            raise TypeError('value must be an integer')
       
        
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o,Integer):
            if self.number == __o.number:
                return True
            else:
                return False
        else:
            return False
    def __add__(self,value):
        if isinstance(value,Integer):
            return Integer(self.number+value.number)
        elif isinstance(value,Complex):
            return value + self #defined in Complex
        elif isinstance(value,Matrix):
            return value + self #defined in Matrix
        else:
            raise TypeError('added value must be Integer,Complex or Matrix obj!')
    def __sub__(self,value):
        if isinstance(value,Integer):
            return Integer(self.number -value.number)
        elif isinstance(value,Complex):
            return Integer(-1)*value + self #defined in Complex 
        elif isinstance(value,Matrix):
            return Integer(-1)*value + self  #defined in Matrix 
        else:
            raise TypeError('subtracted value must be Integer,Complex or Matrix obj!')
    def __mul__(self,value):
        if isinstance(value,Integer):
            return Integer(self.number*value.number)
        elif isinstance(value,Complex):
            return value * self #defined in Complex
        elif isinstance(value,Matrix):
            return value * self #defined in Matrix
        else:
            raise TypeError('added value must be Integer,Complex or Matrix obj!')
    def __repr__(self) -> str:
        return f'{self.number}'



class Complex:
    def __init__(self,real=None,imaginary=None,string=''):
        if real!= None and imaginary != None:
            self.real = real
            self.imaginary = imaginary
        elif string and isinstance(string,str):
            index = string.find('+')
            self.imaginary = string[:index-1]
            self.real = string[index+1:]
        else:
            raise TypeError('Complex arguments can not be empty')

    @property
    def real(self):
        return self._real
    @real.setter
    def real(self,value):

        if isinstance(value,int):
            self._real = value
        elif isinstance(value,str):
            if not value.strip().isnumeric():
                raise ValueError('value must be an integer')
            self._real = int(value.strip())
        else:
            raise TypeError('value must be an integer') 
    @property
    def imaginary(self):
        return self._imaginary
    @imaginary.setter
    def imaginary(self,value):
        if isinstance(value,int):
            self._imaginary = value
        elif isinstance(value,str):
            if not value.isnumeric():
                raise ValueError('value must be an integer')
            self._imaginary = int(value)
    def __eq__(self,value):
        if isinstance(value,Complex):
            if self.real == value.real and self.imaginary == value.imaginary:
                return True
        return False
    def __mul__(self,value):
        if isinstance(value,Integer):
            return Complex(self.real*value.number,self.imaginary*value.number)
        elif isinstance(value,Complex):
            return Complex(self.real*value.real - self.imaginary*value.imaginary,self.real+value.real)
        elif isinstance(value,Matrix):
            return value * self #defined in Matrix
        else:
            raise TypeError('added value must be Integer,Complex or Matrix obj!')
    def __sub__(self,value):
        if isinstance(value,Integer):
            return Complex(self.real-value.number,self.imaginary)
        elif isinstance(value,Complex):
            return Complex(self.real-value.real,self.imaginary-value.imaginary)
        elif isinstance(value,Matrix):
            return Integer(-1)*value + self #defined in Matrix
        else:
            raise TypeError('added value must be Integer,Complex or Matrix obj!')
    def __add__(self,value):
        if isinstance(value,Integer):
            return Complex(self.real+value.number,self.imaginary)
        elif isinstance(value,Complex):
            return Complex(self.real+value.real,self.imaginary+value.imaginary)
        elif isinstance(value,Matrix):
            return value + self #defined in Matrix
        else:
            raise TypeError('added value must be Integer,Complex or Matrix obj!')

    def __repr__(self) -> str:
        operator  = '+'
        if self.real < 0 :
            operator = ''
        if self.imaginary:
            return f'{self.imaginary}i{operator}{self.real}'
        return f'{self.real}'

class Matrix:
    def __init__(self,list,row,col):
        self.list = list
        self.row = row
        self.col = col
    @property
    def list(self):
        return self._list
    @list.setter
    def list(self,value):
        if isinstance(value,list):
            for number in value:
                if not isinstance(number,Integer) and not isinstance(number,Complex):
                    raise TypeError('Matrix items must be Integer or Complex!')
            self._list = value
        else:
            raise TypeError('first argument of Matrix obj must be a list')
    @staticmethod
    def make_unit_matrix(n):
        l = []
        for i in range(n):
            for j in range(n):
                if i==j:
                    l.append(Integer(1))
                else:
                    l.append(Integer(0))
        return Matrix(l,n,n)
    @staticmethod
    def get_ith_row(matrix,i):
        return matrix.list[i*matrix.row:(i+1)*matrix.row]
    @staticmethod
    def get_ith_col(matrix,i):
        return [matrix.list[j*matrix.col + i] for j in range(matrix.row)]
    @staticmethod
    def make_matrix_from_string(elements):
        l = []
        rows = elements.split(',')
        for row in rows:
            for number in row.split():
                if 'i' in number:
                    l.append(Complex(string=number))
                elif number.isnumeric():
                    l.append(Integer(number))
                else:
                    raise TypeError('Matrix values must be Integer or Complex')
        return Matrix(l,len(rows[0].split()),len(rows))
    def is_zero_matrix(matrix)->bool:
        for number in matrix.list:
            if number != Integer(0):
                return False
        return True
    def is_unit_matrix(matrix)->bool:
        for i in range(matrix.row):
            for j in range(matrix.col):
                if j == i :
                    if matrix.list[j*matrix.row + i] != Integer(1):
                        return False
                else:
                    if matrix.list[j*matrix.row + i] != Integer(0):
                        return False
        return True
    @staticmethod
    def is_top_triangular(matrix):
        for i in range(matrix.row):
            for j in range(matrix.col):
                if j > i :
                    if matrix.list[j*matrix.row + i] != Integer(0):
                        return False
        return True
    @staticmethod
    def is_botton_triangular(matrix):
        for i in range(matrix.row):
            for j in range(matrix.col):
                if j < i :
                    if matrix.list[j*matrix.row + i] != Integer(0):
                        return False
        return True
    def __eq__(self,value):
        if isinstance(value,Matrix):
            if self.row == value.row and self.col == value.col:
                for number1,number2 in zip(self.list,value.list):
                    if number1 != number2:
                        return False
                return True
        return False
    def __mul__(self,value):
        if isinstance(value,Integer) or isinstance(value,Complex):
            l = [value*number for number in self.list]
            return Matrix(l,self.row,self.col)
        elif isinstance(value,Matrix):
            l = []
            if self.col == value.row :
                for i in range(self.col):
                    col = Matrix.get_ith_col(i)
                    for j in range(value.row):
                        row = Matrix.get_ith_row(j)
                        element = sum([m*n for m,n in zip(col,row)])
                        l.append(element)
                return Matrix(l,self.row,value.col)
                
            else:
                raise ValueError('matrixes must be from same dimension')
        else:
            raise TypeError('multipled value must be Integer,Complex or Matrix obj!')
    def __sub__(self,value):
        if isinstance(value,Integer) or isinstance(value,Complex):
            l = [number-value for number in self.list]
            return Matrix(l,self.row,self.col)
        elif isinstance(value,Matrix):
            if self.row == value.row and self.col == value.col: 
                l = [number1-number2 for number1,number2 in zip(self.list,value.list)]
                return Matrix(l,self.row,self.col)
            else:
                raise ValueError('matrixes must be from same dimension')
        else:
            raise TypeError('subtracted value must be Integer,Complex or Matrix obj!')
    def __add__(self,value):
        if isinstance(value,Integer) or isinstance(value,Complex):
            l = [value+number for number in self.list]
            return Matrix(l,self.row,self.col)
        elif isinstance(value,Matrix):
            if self.row == value.row and self.col == value.col: 
                l = [number1+number2 for number1,number2 in zip(self.list,value.list)]
                return Matrix(l,self.row,self.col)
            else:
                raise ValueError('matrixes must be from same dimension')
        else:
            raise TypeError('added value must be Integer,Complex or Matrix obj!')
    def __repr__(self)->str:
        string = ''
        for i in range(self.col):
            string +=', '.join([str(number) for number in self.list[i*self.row:(i+1)*self.row]]) +'\n'
        string += ''
        return string
def Multiply(value1,value2):
    return value1*value2

def run_test(test_cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_cls)
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)
class test_matrix(unittest.TestCase):
    def test_integer_validation(self):
        with self.assertRaises(TypeError):
            n = Integer(2.5)
        with self.assertRaises(ValueError):
            n = Integer('a')
    def test_integer_create(self):
        n = Integer(5)
        m = Integer('10')
        self.assertEqual(m.number,10)
        self.assertEqual(n.number,5)
    def test_complex_validation(self):
        with self.assertRaises(TypeError):
            n = Complex(1.5,2)
    def test_complex_create(self):
        n = Complex(2,5)
        m = Complex(string='5i+3')
        self.assertEqual(n.real,2)
        self.assertEqual(n.imaginary,5)
        self.assertEqual(m.real,3)
        self.assertEqual(m.imaginary,5)
    def test_matrix_validation1(self):
        with self.assertRaises(TypeError):
            m = Matrix(2,3,4)
        with self.assertRaises(TypeError):
            m = Matrix('3',2,3)
    def test_matrix_validation2(self):
        with self.assertRaises(TypeError):
            m = Matrix([1,2,3],3,1)
        with self.assertRaises(TypeError):
            m = Matrix(['1','2'],1,2)
    def test_matrix_make_unit(self):
        for i in range(1,20):
            m = Matrix.make_unit_matrix(i)
            for i in range(m.row):
                for j in range(m.col):
                    if j == i :
                        self.assertEqual(m.list[j*m.row + i],Integer(1))
                    else:
                        self.assertEqual(m.list[j*m.row + i],Integer(0))
    def test_matrix_is_unite(self):
        for i in range(1,20):
            self.assertTrue(Matrix.is_unit_matrix(Matrix.make_unit_matrix(i)))
        m = Matrix([Integer(1),Integer(1),Integer(1),Integer(1)],2,2)
        self.assertFalse(Matrix.is_unit_matrix(m))
    def test_matrix_is_zero(self):
        for i in range(1,20):
            l = [Integer(0) for i in range(i)]
            self.assertTrue(Matrix.is_zero_matrix(Matrix(l,1,i-1)))
        m = Matrix([Integer(0),Integer(0),Integer(0),Integer(1)],2,2)
        self.assertFalse(Matrix.is_zero_matrix(m))
    def test_matrix_is_bottom(self):
        m = Matrix([Integer(4),Integer(0),Integer(6),Integer(6)],2,2)
        n = Matrix([Integer(0),Integer(10),Integer(5),Integer(6)],2,2)
        self.assertTrue(Matrix.is_botton_triangular(m))
        self.assertFalse(Matrix.is_botton_triangular(n))
    def test_matrix_is_top(self):
        m = Matrix([Integer(4),Integer(1),Integer(0),Integer(5)],2,2)
        n = Matrix([Integer(0),Integer(0),Integer(5),Integer(6)],2,2)
        self.assertTrue(Matrix.is_top_triangular(m))
        self.assertFalse(Matrix.is_top_triangular(n))
    def test_add1(self):
        
        self.assertEqual(Integer(3)+Integer(5),Integer(8))
        self.assertEqual(Integer(3)+Complex(3,5),Complex(6,5))
        self.assertEqual(Complex(1,5)+Integer(4), Complex(5,5))
    def test_add2(self):
        l = [Integer(5),Complex(2,3),Integer(-7),Complex(9,1)]
        self.assertEqual(Integer(5)+Matrix(l,4,1),Matrix([Integer(10),Complex(7,3),Integer(-2),Complex(14,1)],4,1))
        self.assertEqual(Complex(1,2)+Matrix(l,2,2),Matrix([Complex(6,2),Complex(3,5),Complex(-6,2),Complex(10,3)],2,2))
    def test_subtraction(self):
        l = [Integer(5),Complex(2,3),Integer(-7),Complex(9,1)]
        self.assertEqual(Matrix(l,4,1)-Integer(-1),Matrix(l,4,1)+ Integer(1))
        self.assertEqual(Matrix(l,2,2)-Complex(2,2),Matrix(l,2,2) +Complex(-2,-2))
    def test_multiply(self):
         l = [Integer(5),Complex(2,3),Integer(-7),Complex(9,1)]
         self.assertEqual(Integer(1)*Matrix(l,1,4),Matrix(l,1,4))
        
run_test(test_matrix)