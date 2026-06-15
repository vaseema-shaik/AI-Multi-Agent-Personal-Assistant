def review_code(code):

    if "(" in code and ")" not in code:
        return "Missing closing parenthesis"

    return "No obvious errors found"