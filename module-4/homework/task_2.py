def gcd(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  
print(gcd(17, 13))  
print(gcd(-48, 18))