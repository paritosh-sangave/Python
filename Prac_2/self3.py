square = lambda x: x**2
print(square)
# <function <lambda> at 0x000001BCFD41F040>

def calc_custom_result(n1, n2):
    if n1 % 2 == 0:
        return n1 + n2
    else: 
        return n1*n1 + n2

test_lambda = lambda p1, p2: calc_custom_result(p1, p2)
print(f"result = {test_lambda(10,20)}")
# result = 30