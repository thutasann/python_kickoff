print("--------------- RETURN STATEMENT ---------------- ")

# return statement = Functions send Python values/objects back to the caller.
#                  These values/objects are known as the function's return value


def multiply(num_1, num_2):
    result = num_1 * num_2
    return result


result = multiply(2, 4)
print("result -> " + str(result))
