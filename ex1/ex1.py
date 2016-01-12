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

def mutate_list(input_list):
    '''(list)->NoneType
    Mutates global input_list [almost the same as ex6.py from A08] 
    - Element type = int is mutiplied by 2
    - Element type = bool is inverted
    - Element type = str has it's first and last letters removed. 
    - 0th element is changed to "Hello" regardless of it's orignal type

    >>> thing = [1, 2, "Thing", False]
    mutate_list(thing)
    thing 
    ["Hello", 4, "hin", True]

    '''
    input_list[0] = "Hello"
    # Traverse through every single element and change them one by one
    for i in range(1, len(input_list)):
        # Check the type of the current element and apply the appropriate
        # constraint
        if (type(input_list[i]) == int):
            input_list[i] = input_list[i]*2
        elif(type(input_list[i] == str):
            temp_string = input_list[i]
            # [1:-1] goes from 2nd character to the second last character
            input_list[i] = temp_string[1:-1]
        elif(type(input_list[i]) == bool):
            # temporarily create a boolean var to save the current value
            temp_bool = input_list[i]
            input_list[i] = not temp_bool
            


