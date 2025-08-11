# Implementation (loop)

# prev1 = 0
# prev2 = 1
# count = 2

# print(prev1)
# print(prev2)

# for fibo in range(5):
#     newfibo = prev1 + prev2
#     prev1 = prev2
#     prev2 = newfibo
#     print(newfibo)


# Implementation 2 (Recursion)

# def fibo(prev1, prev2):
#     global count
#     if count <= 5:
#         newfibo = prev1 + prev2
#         print(newfibo)
#         prev1 = prev2
#         prev2 = newfibo
#         count += 1
#         return fibo(prev1, prev2)
#     return


# fibo(prev1, prev2)


# Implementation 3 (recursion with formula)

def fibo_for(number):
    if number <= 1:
        return number
    return fibo_for(number - 1) + fibo_for(number - 2)


print(f"Answer: {fibo_for(5)}")
