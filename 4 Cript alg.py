# vigener
def vigener(text, key):
  alpArr = []
  alp = "abcdefghijklmnopqrstuvwxyz"
  alpArr += alp
  m = len(key) 
  ciphertext = ""
  for index in range(len(text)):
    if text[index] == " ":
      key = key[-1]+key[:-1]
      ciphertext += " "
    else:
      ciphertext += alpArr[((alpArr.index(text[index]) + alpArr.index(key[index % m])) % 26)]
  return ciphertext
print("\nVigener")
print("text: lorem ipsum")
print("key: firstkey")
print("ciphertext:",vigener("lorem ipsum", "firstkey"))
# ===========================================================================================
# RSA
def mod_inverse(e, m):
    for x in range(1, m):
        if (e * x) % m == 1:
            return x
    return -1
print("===========")
print("Rsa")
print("text: hello")    
def KeyGen():
  p = 313
  q = 191
  n = p*q
  m = (p - 1) * (q - 1)
  e = 2167
  d = mod_inverse(e, m)
  return [(e, n), (d, n)]
print("keys:",KeyGen())
def Encrypt(message):
  e, n = KeyGen()[0]
  c = [pow(ord(c), e, n) for c in message]
  return c
print("encrypt:",Encrypt("hello"))

def Decrypt(message):
  d, n = KeyGen()[1]
  c = [chr(pow(c, d, n)) for c in message]
  return ''.join(c)
print("decrypt:", Decrypt(Encrypt("hello")))

