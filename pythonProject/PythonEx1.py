def func(argument1, argument2, **arguments, ):
    result = []
    for arg in arguments.values():
        output = [match for match in arg if len(arguments) <= argument2 if len(arg) > 1 if
                  argument1.lower() in match.lower() if len(match) > len(argument1) * 2 if
                  match.isalpha() or '' in match]
        result.extend(output)
    return result
