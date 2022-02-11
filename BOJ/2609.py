a, b = map(int, input().split())

gcd = lambda a,b: b if a%b==0 else gcd(b, a%b)
lcm = lambda a,b: a*b//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))
