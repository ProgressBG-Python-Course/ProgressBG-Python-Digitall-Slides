str_in_bytes =  b'123\xd0\xb0\xd0\xb1\xd0\xb2'
str_in_utf8 = str_in_bytes.decode()

print("String object:", str_in_utf8)
print("Type: ",type(str_in_utf8) )
print("Length:",len(str_in_utf8) )
