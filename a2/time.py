import time
one_re = "0123e"
left = "("
right = ")"
star = "*"
operator = "|."
one = "1"
two = "2"
zero = "0"
epsilon = "e"


def perms(s):
    '''(str) -> list of str
    Return a list of all the permutations for s.
    REQ len(s) > 0
    '''
    result = []
    if len(s) == 2:
        ns = s[0] + s[1]
        result.append(ns)
        ns = s[1] + s[0]
        result.append(ns)
    else:
        ns = s[0]
        rest = perms(s[1:])
        for string in rest:
            for i in range(len(string)+1):
                perm_string = string[:i] + ns + string[i:]
                result.append(perm_string)
    return result


def clean(s):
    '''(str) -> str
    Removes the outer most parentheses from the str and returns it
    '''
    result = s
    length = len(s)
    if s[0] == left and s[length - 1] == right:
        result = s[1:-1]
    return result


def find_operator(s):
    '''(str) -> int
    Returns the index of where the operator symbol is in the string,
    if it isn't present return -1. Doesn't work with nested Parentheses.(BTW
    how the hell do you spell that word??)
    find_operator("(0.1)") -> 2
    find_operator("(01)") -> -1
    '''
    result = s.find(".")
    if result == -1:
        result = s.find("|")
    return result

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
    '''(str) -> bool
    check if the passed string is a valid regular expression.
    REQ len(s) > 0
    '''
    if len(s) == 1:
        if s in one_re:
            result = True
        else:
            result = False
    elif s[-1] == star:
        # if it ends with a star then remove it and check if the rest is a
        # regular expression or not.
        result = is_regex(s[:-1])
    elif s[0] == left:
        # if len(s) > 3 and s is a proper regex then it has to have outer
        # parenthess. So we should clean them if it doesn't then we know that
        # it's not a regex at all.
        ns = clean(s)
        # check if s still starts and ends with the parenthese. if they do then
        # we need to identify it's end and set that as r1, the first character
        # of the remaining string as the symbol and the rest as r2.
        if ns[0] == left:
            # Split the regex into 2 parts and make the recursive call
            index_end = find_right(ns)
            r1 = ns[0:index_end+1]
            symbol = ns[index_end+1]
            r2 = ns[index_end+2:]
            is_r1 = is_regex(r1)
            is_r2 = is_regex(r2)
            if is_r1 and is_r2 and symbol in operator:
                result = True
            else:
                result = False
        else:
            # since we removed the parantheses, we need to figure out the
            # operator symbol: "|" or "." then we can split the expression into
            # three, a r1, r2 and symbol
            # since there are no parantheses we know that there is only one of
            # the operator symbol now.
            i_symbol = find_operator(ns)
            if i_symbol == -1:
                # if there are no operators then you should only have 2
                # characters in ns.
                if len(ns) == 2:
                    result = is_regex(ns)
                else:
                    result = False
            else:
                r1 = ns[0:i_symbol]
                symbol = ns[i_symbol]
                r2 = ns[i_symbol+1:]
                print(r1)
                is_r1 = is_regex(r1)
                is_r2 = is_regex(r2)
                if is_r1 and is_r2 and symbol in operator:
                    result = True
                else:
                    result = False
    else:
        result = False
    return result

def regex_perm(s):
    ps = perms(s)
    #print(ps)
    i = 0
    index = True
    if '' not in ps:
        while index:
            if i < len(ps):
                print(ps[i])
                regex = is_regex(ps[i])
                if regex == False:
                    ps.pop(i)
                else:
                    i +=1
            else:
                index = False
    return ps
if __name__ == '__main__':
    start_time = time.time()
    #thing = regex_perm('(0|1)*')
    red = is_regex("(1.(1|0).2")
    print(red)
    #print(thing, len(thing))
    #print(is_regex(thing[119]))
    print("this took:" , time.time() - start_time)
