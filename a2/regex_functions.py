"""
# Copyright Fazil Zuhaib, Nick Cheng, Brian Harrington, Danny Heap
# 2013, 2014, 2015, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2016
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from regextree import RegexTree, StarTree, DotTree, BarTree, Leaf

# Do not change anything above this comment except for the copyright
# statement

# Student code below this comment.
# SOME GLOBAL CONSTANTS
one_re = "0123e"
left = "("
right = ")"
star = "*"
dot = '.'
bar = '|'
operator = "|."
one = "1"
two = "2"
zero = "0"
epsilon = "e"

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

def split(s):
    '''(str) -> list of str
    split the string at the 'main' occurance of either . or |
    and return a list components.
    '''

    if len(s) == 0:
        r1 = "None"
        r2 = "None"
        symbol = "None"
    elif s[0] == left:
        right_index = find_right(s)
        r1 = s[:right_index+1]
        if right_index == len(s)-1:
            symbol = "None"
            r2 = "None"
        else:
            symbol = s[right_index+1]
            r2 = s[right_index+2:]
    else:
        found = False
        i = 0
        while not found:
            if (i < len(s) and s[i] in operator):
                found = True
            elif i > len(s):
                # since i is greater than len(s) and we haven't found a symbol
                # we are going to return a bogus symbol which is going to be
                # the middle character of the string we got. this would work
                # becuase if a string that was send by split doens't have a
                # symbol in it then its not a regex. And all functions that use
                # this helper either require a valid regex to be inputted or is
                # checking if the string is a regex or not. so we are gucci
                i = len(s)//2
                found = True
            else:
                i +=1
        r1 = s[:i]
        r2 = s[i+1:]
        symbol = s[i]
    return [r1, r2, symbol]


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


def get_children(tree, result = []):
    '''(RegexTree) -> list of str
    Given a regex tree get all of the children and their symbols.
    '''
    symbol = tree.get_symbol()
    result.append(symbol)
    if type(tree) == StarTree:
        # get it's children
        child = tree.get_children()
        # recurive to break it down further.
        lchild = get_children(child)
    elif type(tree) == BarTree or type(tree) == DotTree:
        # type is going to be either dot or bar.
        c1, c2 = tree.get_children()
        # recursive to break the children down to list
        lc1 = get_children(c1)
        lc2 = get_children(c2)
    return result


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
    elif len(s) != 0:
        if s[-1] == star:
            # if it ends with a star then remove it and check if the rest is a
            # regular expression or not.
            result = is_regex(s[:-1])
        elif s[0] == left and s[-1] == right:
            # remove brackets
            ns = s[1:-1]
            r1, r2, symbol = split(ns)
            is_r1 = is_regex(r1)
            is_r2 = is_regex(r2)
            if is_r1 and is_r2 and symbol in operator:
                result = True
            else:
                result = False
        else:
            result = False

    else:
        result = False

    return result

def all_regex_permutations(s):
    '''(str) -> set
    Return a set consisting of all regex permutations of s.
    REQ s has to be a valid regex
    '''
    result = set()
    if len(s) == 1 or len(s) == 2:
       result.add(s)
    elif s[-1] == star:
        # remove the star and then get the permutations
        # then add the star at every position after 1 and index_symbol +1
        perm_wo_star = all_regex_permutation(s[:-1])
        for perm in perm_wo_star:
            # check lenghh.
            if len(perm) == 1:
                perm += star
                pass

    else:
        r1, r2, symbol = split(s[1:-1])
        r1_perms = all_regex_permutations(r1)
        r2_perms = all_regex_permutations(r2)
        for r1_perm in r1_perms:
            for r2_perm in r2_perms:
                ns = left + r1_perm + symbol + r2_perm + right
                result.add(ns)
                ns = left + r2_perm + symbol + r1_perm + right
                result.add(ns)
    return result



def regex_match(r, s):
    '''(RegexTree, str) -> bool
    Check if the given string, s, matches the given regex, r.
    REQ RegexTree resolves to a valid regex string
    '''
    # check the root of the tree
    symbol = r.get_symbol()
    if type(r) == Leaf:
        if len(s) == 1 and s == symbol:
            result = True
        else:
            result = False
    elif symbol == star:
        # you know its a unary tree therefore only one child.
        rl = r.get_children()
    else:
        rl, rr = r.get_children()
        rls = rl.get_symbol()
        rrs = rr.get_symbol()
        if symbol == bar:
            if rls in s[0] or rrs in s[1]:
                result = True
            else:
                result = False

        else:
            if rls in s[0] and rrs in s[1]:
                result = True
            else:
                result = False

    return result


    # now we know whether it's or or and. (the ors are real LOL).
    # check for the left part of the statement and then the right.
    # then look at left and right parts of the string in accordance with the
    # symbol in the root of the tree.



def build_regex_tree(regex):
    '''(string) -> RegexTree
    Builds a corresponding regex tree.
    REQ regex is a valid regular expression
    '''
    if len(regex) == 1:
        root = Leaf(regex)
    elif regex[-1] == star:
        child = build_regex_tree(regex[:-1])
        root = StarTree(child)
    else:
        # remove the brackets!
        nregex = regex[1:-1]
        r1,r2,symbol = split(nregex)
        childr1 = build_regex_tree(r1)
        childr2 = build_regex_tree(r2)
        if symbol == dot:
            root = DotTree(childr1, childr2)
        else:
            root = BarTree(childr1, childr2)
    return root


if __name__ == "__main__":
    s = '((1.2)|1)'
    #s = ''
    print(s)
    x = build_regex_tree(s)
    print(x)
    y = get_children(x)
    print(y)



#    ns = "abc"
#    f = perms(ns)
#    print(f)
    #c = clean(s)
    #d = find_right(c)
    #print(c)
    #print(d)
