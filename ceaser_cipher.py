Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def ceaser(d,t,s):
  a=[]
  a[:0] = t
  if(d=='decode'):
    s*=-1
  for i in range(0,len(a),1):
    if(a[i] in alphabet):
      a[i]=alphabet[abs(alphabet.index(a[i])+s)%26]
    b="".join(a)
  print(f"the {d}d message is {b}")
ceaser(direction,text,shift)