def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count=0
    if parens[0]==')' or parens[len(parens)-1]=='(':
        return False
    for par in parens:
        if par=='(':
            count+=1
        elif par==')':
            count-=1
    return True if count==0 else False
