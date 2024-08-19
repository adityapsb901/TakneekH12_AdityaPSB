def inv(c): #Function to transform closing brackets to opening for comparison
    if c == '}':
        return "{"
    elif c ==']':
        return "["
    elif c ==")":
        return "("
    else:
        return c


def bracket_check(s):
    p = 1
    L = []
    for i in s:
        if i in '({[': #building a stack while opening brackets appear
            L += i
        else:
            try: #This is in a try except block in case the stack is empty
                if L.pop() != inv(i): #removing elements from a stack and comparing
                    p = -1 
                    break # if elements don't match, then loop is terminated and string is invalid
            except:
                p = -1
                break
    return p
s1 = input('>>>')

print(bracket_check(s1))
                
