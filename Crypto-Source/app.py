#This will be the "main" function
#Needs to call Key generator, encrypt, and derypt functions

from flask import Flask, redirect, render_template, request
import random 

# Configure application name
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


#algorithm for finding the greatest common divisor
#This function is used in key generation

def gcd(a,b):
    while b !=0:
        a, b = b, a % b
    return a


#algorithm to find the multiplicative inverse of two numbers
#Used in key generation

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

@app.route('/KeyGeneration', methods=["POST"])
def generate_keypair(p, q):
    #n = pq
    p = request.form.get("p")
    q = request.form.get("q")
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



#Function for encryption
#uses public key
@app.route('/Encrypt', methods=["POST"])
def encrypt(e, n, plaintext):
    plaintext = request.form.get(plaintext)
    e = request.form.get("e")
    n = request.form.get("n")

    #encrypt by plaintext^e mod n
    ciphertext = [(ord(char) ** e) % n for char in plaintext]

    #Return encrypted text
    return ciphertext



#function for decryption
#uses private key
@app.route('/Decrpyt', methods=["POST"])
def decrypt(d, n, ciphertext):
    ciphertext = request.form.get(ciphertext)
    d = request.form.get("d")
    n = request.form.get("n")

    #decrypt by ciphertext^d % n
    plaintext = [chr((char ** d) % n) for char in ciphertext]

    #return plaintext
    return ''.join(plaintext)