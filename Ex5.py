def factorial_while(n):
    if n < 0:
        return "positive integers only"
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
def factorial_for(n):
    if n < 0:
        return "positive integers only"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
num = int(input("Enter a number："))
print(f"While：{factorial_while(num)}")
print(f"For：{factorial_for(num)}")
