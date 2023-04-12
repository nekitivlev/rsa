import argparse
import random
from math import gcd


def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i=i+1
    return True


def generatePrime():
    for x in range(random.randint(int(10e8 + 1), int(10e9)), int(10e10)):
        if isPrime(x):
            return x
    return 10e9 + 7


def euclid(e, m):
    if e == 0:
        return 0, 1
    (d1, y1) = euclid(m % e, e)
    return y1 - (m // e) * d1, d1


def generateKeys():
    p = generatePrime()
    q = generatePrime()
    assert (isPrime(p))
    assert (isPrime(q))
    n = p * q
    m = (p - 1) * (q - 1)
    e, d = generate_ed(m)
    assert (e * d % m == 1)
    return (e, n), (d, n)


def generate_ed(m):
    e = random.randint(2, m)
    while gcd(e, m) != 1:
        e = random.randint(2, m)
    (d, y) = euclid(e, m)
    d = (d % m + m) % m
    return e, d


def powMod(x, pwr, n):
    if pwr == 0:
        return 1
    if pwr % 2 == 1:
        return x * powMod(x, pwr - 1, n) % n
    temp = powMod(x, pwr // 2, n)
    return temp * temp % n


def encrypt(e, n, input, output):
    plainText = input.read()
    result = ""
    for char in plainText:
        result += str(powMod(ord(char), e, n)) + "\n"
    output.write(result)


def decrypt(d, n, input, output):
    result = ""
    for ln in input.readlines():
        ln = ln.rstrip()
        result += chr(powMod(int(ln), d, n))
    output.write(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='RSA crypto-algorithm',
        description='Generates public or private key and encodes or decodes text')

    parser.add_argument('-m', '--mode', choices=['generate', 'encrypt', 'decrypt'], help='choose mode of program')
    parser.add_argument('-k', '--key', type=str, help='key for encoding/decoding')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), help='input file')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), help='output file')

    args = parser.parse_args()

    if args.mode == 'generate':
        keys = generateKeys()
        print("public key:", str(keys[0][0]) + "," + str(keys[0][1]))
        print("private key:", str(keys[1][0]) + "," + str(keys[1][1]))
    elif args.mode == 'encrypt':
        if args.key is None:
            print("arguments should contain public key")
            exit(0)
        key = args.key.strip()
        arr = key.split(",")
        if len(arr) != 2:
            print("wrong public key")
            exit(0)
        if args.input is None:
            print("null input filepath")
            exit(0)
        if args.output is None:
            print("null output filepath")
            exit(0)
        e = int(arr[0])
        n = int(arr[1])
        if e is None or n is None:
            print("null public key")
        encrypt(e, n, args.input, args.output)
    else:
        if args.key is None:
            print("arguments should contain public key")
            exit(0)
        key = args.key.strip()
        arr = key.split(",")
        if len(arr) != 2:
            print("wrong public key")
            exit(0)
        if args.input is None:
            print("null input filepath")
            exit(0)
        if args.output is None:
            print("null output filepath")
            exit(0)
        d = int(arr[0])
        n = int(arr[1])
        if d is None or n is None:
            print("wrong public key")
        decrypt(d, n, args.input, args.output)
