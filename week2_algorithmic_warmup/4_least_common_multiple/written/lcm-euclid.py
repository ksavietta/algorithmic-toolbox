# Uses python3
import sys

def gcd_efficient(a,b):
    g = max([a,b])
    l = min([a,b])
    current_gcd = 0
    while ( l > 0 ):
        remainder = g % l
        g = l
        l = remainder
        current_gcd = g
    return current_gcd

def lcm_euclid(a,b):
    return (a * b) // gcd_efficient(a, b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_euclid(a, b))
