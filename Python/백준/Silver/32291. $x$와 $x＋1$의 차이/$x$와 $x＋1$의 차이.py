def divisor(number):
    result = []
    for i in range(1, int(number**(1/2))+1):
        if number%i==0:
            result.append(i)
            if i < number//i:
                result.append(int(number//i))
    result.sort() 
    return result 

result = divisor(int(input())+1)
result.pop()
print(*result)