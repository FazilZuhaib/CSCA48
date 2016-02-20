class MatrixIndexError(Exception):

    '''An attempt has been made to access an invalid index in this matrix'''


class MatrixDimensionError(Exception):

    '''An attempt has been made to perform an operation on this matrix which
    is not valid given its dimensions'''


class MatrixInvalidOperationError(Exception):

    '''An attempt was made to perform an operation on this matrix which is
    not valid given its type'''


class MatrixNode():

    '''A general node class for a matrix'''

    def __init__(self, contents, right=None, down=None):
        '''(MatrixNode, obj, MatrixNode, MatrixNode) -> NoneType
        Create a new node holding contents, that is linked to right
        and down in a matrix
        '''
        self._contents = contents
        self._right = right
        self._down = down

    def __str__(self):
        '''(MatrixNode) -> str
        Return the string representation of this node
        '''
        return str(self._contents)

    def get_contents(self):
        '''(MatrixNode) -> obj
        Return the contents of this node
        '''
        return self._contents

    def set_contents(self, new_contents):
        '''(MatrixNode, obj) -> NoneType
        Set the contents of this node to new_contents
        '''
        self._contents = new_contents

    def get_right(self):
        '''(MatrixNode) -> MatrixNode
        Return the node to the right of this one
        '''
        return self._right

    def set_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set the new_node to be to the right of this one in the matrix
        '''
        self._right = new_node

    def get_down(self):
        '''(MatrixNode) -> MatrixNode
        Return the node below this one
        '''
        return self._down

    def set_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set new_node to be below this one in the matrix
        '''
        self._down = new_node


class Matrix():

    '''A class to represent a mathematical matrix'''

    # Series of helper methods used

    def _find_up_to_right(self, m):
        '''(Matrix, int) -> MatrixNode
        Given the head of a Matrix Node return the node that's m if m exists or
        return the node that has highest lower value than m.         
        '''
        curr, ncurr, count = self._head, curr.get_right(), 0
        while ncurr.get_contents() is not None and curr.get_contents() <= m:
            # keep track of the number of traversals are needed to reach the
            # goal
            curr, ncurr, count = curr.get_right(), curr.get_right(), count+1

        return curr, count

    def _find_up_to_down(self, n):
        '''(Matrix, int) -> MatrixNode
        Given the head of a Matrix return the node that's n, iff n exists or 
        return the node that has the highest lower value than n.
        '''
        curr, ncurr, count = self._head, curr.get_down(), 0
        while ncurr.get_contents() is not None and curr.get_contents() <= m:
            # keep track of the number of traversals are needed to reach the
            # goal
            curr, ncurr, count = curr.get_down(), curr.get_down(), count+1

        return curr, count



    def __init__(self, m, n, default=0):
        '''(Matrix, int, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        '''
        self._head = MatrixNode(None)

    def get_val(self, i, j):
        '''(Matrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        '''

    def set_val(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m
        '''
        # curr = node that either represents 'i'/'j' or the node before 'i'/'j'
        # count represents the amount of visits made to get to rcurr.
        # letter before represents the direction
        rcurr, rcount = self._find_up_to_right(i)
        dcurr, dcount = self._find_up_to_down(j)
        if rcurr.get_contents() == i and dcurr.get_contents() == j:
            if rcount < dcount:
                for i in range(dcount):
                    dcurr = dcurr.get_right()
        


    def get_row(self, row_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the row_num'th row of this matrix
        '''

    def set_row(self, row_num, new_row):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the row_num'th row of this matrix to those of new_row
        '''

    def get_col(self, col_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the col_num'th column of this matrix
        '''

    def set_col(self, col_num, new_col):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the col_num'th column of this matrix to
        those of new_row
        '''

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix
        '''

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix
        '''

    def add_scalar(self, add_value):
        '''(Matrix, float) -> NoneType
        Increase all values in this matrix by add_value
        '''

    def subtract_scalar(self, sub_value):
        '''(Matrix, float) -> NoneType
        Decrease all values in this matrix by sub_value
        '''

    def multiply_scalar(self, mult_value):
        '''(Matrix, float) -> NoneType
        Multiply all values in this matrix by mult_value
        '''

    def add_matrix(self, adder_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the sum of this matrix and adder_matrix
        '''

    def multiply_matrix(self, mult_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the product of this matrix and mult_matrix
        '''


class OneDimensionalMatrix(Matrix):

    '''A 1xn or nx1 matrix.
    (For the purposes of multiplication, we assume it's 1xn)'''

    def get_item(self, i):
        '''(OneDimensionalMatrix, int) -> float
        Return the i'th item in this matrix
        '''

    def set_item(self, i, new_val):
        '''(OneDimensionalMatrix, int, float) -> NoneType
        Set the i'th item in this matrix to new_val
        '''


class SquareMatrix(Matrix):

    '''A matrix where the number of rows and columns are equal'''

    def transpose(self):
        '''(SquareMatrix) -> NoneType
        Transpose this matrix
        '''

    def get_diagonal(self):
        '''(Squarematrix) -> OneDimensionalMatrix
        Return a one dimensional matrix with the values of the diagonal
        of this matrix
        '''

    def set_diagonal(self, new_diagonal):
        '''(SquareMatrix, OneDimensionalMatrix) -> NoneType
        Set the values of the diagonal of this matrix to those of new_diagonal
        '''


class SymmetricMatrix(SquareMatrix):

    '''A Symmetric Matrix, where m[i, j] = m[j, i] for all i and j'''


class DiagonalMatrix(SquareMatrix, OneDimensionalMatrix):

    '''A square matrix with 0 values everywhere but the diagonal'''


class IdentityMatrix(DiagonalMatrix):

    '''A matrix with 1s on the diagonal and 0s everywhere else'''

if __name__ == '__main__':
    def x(y):
        return y,y

    thing = x(1)
    print(thing)