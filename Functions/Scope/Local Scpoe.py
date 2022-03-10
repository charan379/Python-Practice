# local scope example using function

def add(x,y):
    # here result is a local variable
    result = x +y
    return result

fn , sn = 1, 2

print(add(fn,sn))

# We call print or use local variable result out side function
print(result)