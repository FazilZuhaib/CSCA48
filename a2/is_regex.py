def find_right(s):
    '''(str) -> int
    Returns the index of where the right parantheses is at
    '''
    found = False
    # level of parentheses we are in
    level = 1
    # starting at 1 because we know 0 is left
    index = 1
    while not found:
        if s[index] == right and level == 1:
            found = True
        elif s[index] == right and level != 1:
            level -= 1
            index += 1
        else:
            if s[index] == left:
                level += 1

            index += 1
    return index

def is_regex(s):
    '''(str) -> bool'''
    if len(s) == 1:
        if s in one_re:
            result = True
        else:
            result = False
    elif s[-1] == star:
        result = is_regex(s[:-1])
    elif s[0] == left and s[-1] == right:
        ns = s[1:-1]
        if ns[0] == left:
            i_right = find_right(ns)
            r1 = ns[0:i_right+1]
            symbol = ns[i_right+1]
            r2 = ns[i_right+1:]
        else:
            # check if the left bracket
            left_index = ns.find(left)
            if left_index == -1:
                # no left brackets at all means that
            else:





        is_r1 = is_regex(r1)
        is_r2 = is_regex(r2)
        if is_r1 and is_r2 and (symbol in "|."):
            result = True
        else:
            result = False
    else:
        result = False
