import base64

str=raw_input()

s=str.decode('hex')

a=base64.b64encode(s)

print "The given string in base64 : " + a
