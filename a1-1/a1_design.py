class Column():
    '''Class representing a column'''

    def __init__(self):
        '''(Column)'''
        pass

    def get_value(self, n):
        '''(Column, int) -> int or str
        Get the value stored at position n in the column list
        '''
        pass

    def set_value(self, n, item):
        '''(Column, int, int or str) -> NoneType
        Change the value stored at position n to item
        REQ position n MUST exist in the the column and it must store an int or
        a str
        '''
        pass

    def add_value(self, item):
        '''(Column, int or str) -> NoneType
        Add item to the end of the Column
        '''
        pass

class Row():
    '''Class representing a row'''

    def __init__(self):
        '''(Row)'''
        pass

    def get_value(self, n):
        '''(Row, int) -> int or str
        Get the value stored at position n in the row list
        '''
        pass

    def set_value(self, n, item):
        '''(Row, int, int or str) -> NoneType
        Change the value stored at position n to item
        REQ position n MUST exist in the the row and it must store an int or
        a str
        '''
        pass

    def add_value(self, item):
        '''(Row, int or str) -> NoneType
        Add item to the end of the Row
        '''
        pass


class Matrix():
    '''Class representing a Matrix'''

    def __init__(self, n_rows, n_col):
        '''(Matrix, int, int)'''
        pass

    def get_value(self, n_row, n_col):
        '''(Matrix, int, int) -> int or str
        Get the value stored at position n in the Matrix
        '''
        pass

    def set_value(self, n_row, n_col, item):
        '''(Matrix, int, int, int or str) -> NoneType
        Change the value stored at position n row and n column to item
        REQ position n MUST exist in the the row and column and it must store
        an int or a str
        '''
        pass

    def add_value(self, item):
        '''(Matrix, int or str) -> NoneType
        Add item to the end of the Matrix
        '''
        pass


    def add(self, r1, c1, r2, c2):
        '''(Matrix, int, int, int, int) -> int
        Add values from (r1, c1) + (r2, c2)
        where (r1,c1) resolves to a single value, since they are are the same
        thing.
        '''
        pass

    def mult(self, r1, c1, r2, c2):
        '''(Matrix, int, int, int, int) -> int
        Do this: (r1, c1) * (r2, c2)
        where (r1,c1) resolves to a single value, since they are are the same
        thing.
        '''
        pass


    def diff(self, r1, c1, r2, c2):
        '''(Matrix, int, int, int, int) -> int
        Do this: (r1, c1) - (r2, c2)
        where (r1,c1) resolves to a single value, since they are are the same
        thing.
        '''
        pass

    def transpose(self):
        '''(Matrix) -> NoneType
        Applies the transpose operation to the Matrix, where the rows and the
        columns are switched.
        '''
        pass

    def swap_col(self, c1, c2):
        '''(Matrix, int, int) -> NoneType
        Switches c1 (some specified column number) to c2, and c2 to c1
        '''
        pass


    def swap_row(self, r1, r2):
        '''(Matrix, int, int) -> NoneType
        Switches r1 (some specified row number) to r2, and r2 to r1
        '''
        pass









