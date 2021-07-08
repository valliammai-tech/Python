# Question 1) - Your function will take N arrays as Arguments and a string X, Integer Y,
#               you must return a final list of all possible elements from all Arrays ;
#                - Whose length is greater than length of string X by at-least twice,
#                - Whose value contains the pattern string x
#
# Conditions for an element to be shortlisted;
# --------------------------------------------
# 1. The element in the list must not be == string X
# 2. The total number of elements in each list must be greater than 1
# 3. The elements in the list have to be Alphabets alone , no other special chars or types allowed
# 4. The max number of lists that can be passed is Integer Y


def func(argument1, argument2, **arguments):
    result = []
    for arg in arguments.values():
        output = [match for match in arg if len(arguments) <= argument2 if len(arg) > 1 if
                  argument1.lower() in match.lower() if len(match) > len(argument1) * 2 if
                  match.isalpha() or '' in match]
        result.extend(output)
    return result
