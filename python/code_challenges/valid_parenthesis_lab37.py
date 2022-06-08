from black import out
from sqlalchemy import false


def validParen(self, s):
    output = []
    for paren in s:
        if paren == "{" or paren == "[" or paren == "(":
            output.appen(paren)
        else:
            if len(output) == 0:
                return False
            if paren == "}" and paren != "{":
                return False
            if paren == "]" and paren != "[":
                return False
            if paren == ")" and paren != "(":
                return False
    if len(output) != 0:
        return False
    else:
        return True
