from container import *


def banana_verify(source, goal, cont, moves):
    '''(str, str, Container, list of str)-> bool
     Check if the list of moves return the goal word given the source word. If
     the result is what we expected then return True if not, return False
    '''
    # this string stores the result we get after going through all the moves
    # may or may not result in the source word.
    resultant = ""
    # keeping track of the index of the string that we are going to modify.
    count = 0
    # loop through the moves in order
    while count < len(source):
        for i in range(len(moves)):
            # chech if i is a push, move or a get and respond accordingly
            if moves[i] == 'P':
                # put the item in the container
                try:
                    cont.put(source[count])
                    count += 1
                except ContainerFullException:
                    return False
            elif moves[i] == 'M':
                # Moves command moves the letter from source to resultant
                resultant += source[count]
                count += 1
            elif moves[i] == 'G':
                # Get command moves the letter from the container to resultant
                # and empties the container.
                try:
                    resultant += cont.get()
                except ContainerEmptyException:
                    return False
    return (resultant == goal)
