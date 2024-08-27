def convert_to_math_expression(human_expr):
    # Dictionary to map human-readable operators to mathematical operators
    conversion_dict = {"plus": "+", "minus": "-", "times": "*", "divided by": "/"}

    # Replace human-readable operators with mathematical operators
    for word, symbol in conversion_dict.items():
        human_expr = human_expr.replace(word, symbol)

    return human_expr


def evaluate(expression):
    math_expr = convert_to_math_expression(expression)
    return float(eval(math_expr))
