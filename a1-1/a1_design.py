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

    def get_value(self, n_row,):
        '''(Column, int) -> int or str
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







