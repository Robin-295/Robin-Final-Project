import random
import flask


#algorithm for finding the greatest common divisor

def gcd(a,b):
    while b !=0:
        a, b = b, a % b
    return a


#algorithm to find the multiplicative inverse of two numbers

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi


#actual keypair generation
#I'm using flask here so that this will work with HTML

@app.route("/generate_keypair", methods=["POST"])
def generate_keypair(p, q):
    #n = pq
    #p and q are currently placeholders. In final implementation p and q will come from user input
    n = p * q

    #phi is the totient of n
    phi = (p-1) * (q-1)

    #choose integer e
    e = random.randrange(1, phi)

    #verify that e and phi are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #use multiplicative inverse to generate the private key
    d = multiplicative_inverse(e, phi)

    #return keypair
    #public key = (e, n), private key = (d, n)
    return ((e, n), (d, n))

