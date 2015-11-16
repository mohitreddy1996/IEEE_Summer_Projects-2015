plain_txt=raw_input("Enter the plaintext/Message ")
plain_txt=plain_txt.upper()
key=raw_input("enter the Key ")
key=key.upper()
cipher_txt=[]*(len(plain_txt))

for i in range(0,len(plain_txt)):
	c=chr(((ord(plain_txt[i])-65)+(ord(key[i%len(key)])-65))%26 + 65)
	cipher_txt.append(c)

print "Plain Text : %s"%plain_txt
print "Key : %s"%key
cipher_txt="".join(cipher_txt)
print "cipher text : %s"%cipher_txt

