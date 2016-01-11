def greeting(name):
    '''(str)->str
    Takes in a string <name> and returns a greeting in the form of:
    "Hello <name> how are you today?"

    REQ len(name)>0

    >>> greeting("Fazil")
    "Hello Fazil how are you today?"

    >>> greeting("Nick")
    "Hello Nick how are you today?"
    '''
    return "Hello " + name + " how are you today?"
