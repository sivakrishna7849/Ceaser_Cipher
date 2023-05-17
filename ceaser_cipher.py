g = True
while(g):
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',      'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',   't', 'u', 'v', 'w', 'x', 'y', 'z']
  from art import logo
  print(logo)
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
  f=input("Do you want to run the code again if you want to run it again type 'yes' else type 'no'")
  if(f=="no"):
    g = False
    print("Goodbye")
    break
