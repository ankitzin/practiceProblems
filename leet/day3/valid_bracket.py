"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""

def isValid_(s):
    sm = 0
    mi = 0
    la = 0
    brac_dict = {
        '(':')',
        '{':'}',
        '[':']',
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for x in range(0,len(s),1):
        print(s[x])
        if s[x] == brac_dict[s[x]]:
            if '(' == s[x]:
              sm +=1
            elif ')' == s[x]:
                sm -= 1

            if '{' == s[x]:
              mi +=1
            elif '}' == s[x]:
                mi -= 1

            if '[' == s[x]:
              la +=1
            elif ']' == s[x]:
                la -= 1
        else:
            return False

    if mi == la == sm:
        return True
    else:
        return False


pairs = {')': '(',
             '}': '{',
             ']': '['}

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for c in s:
        if c not in pairs:
            stack.append(c)
        else:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return not stack

print(isValid("()[]"))
