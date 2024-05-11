from pwn import xor
from Crypto.Cipher import AES

iv = b'\xf5\x8e\x85ye\xc8j(%\xc4K\xc1g#\x86\x1a'
ct = b'h\x08\xafmDV\xaa\xcd\xea\xe9C\xdd7/\x1fF\xe2?\xcb\xb0\x1d F\xcc\xe5\xa6\x9dTJ\\\xd1\x90\xac\xe0\x1c\x891}\x83*\x86\xee\xc4~\xa0\x18\xa8\x06\xea"{|\x0b\x92[\x9a[\x91\xc8\x19\xb7FK\x01\xb5\xf98\x80\x9bR)2\x84`\xb3E\t\xd5\xe5\xf0[\x83\xc6\x19\x82\r\x7f\xfaGF\xdb\xcb\xab\xd5~\x95\t\xdd\xb5E>F\xdd\xa9\xa6\x82\x86\xee"\x99\xd9\xcc\xaf\xce\xf0\'\xb3\xf4~\xcf\xdb\xc8\xbd3\x01\xd0,}]\xd5V\xd3?\xb0\xe7\xb4[4\x8a\xa2[\xa1TV\xd16\x1f\xbd"\xc8\xa2\\K\x16I%\xdaL\xc6\xfb\xb7f.\x98\xc3\xf4J\x1b\xe9TT\x83-\x98BO\xb4\x00~\xb5w\xcf7m\xa1\xea\xa9\xf6\xa6\xee\x00Y\xdfE\x9c7\xe3\xa3\xa2\x1f=.\x85\x08l\xacN\xfb2\x89\x8bB\x7f\x94\x91p\x10ep\x9b\x06oz\x87&U]J\x019\x12W\xce<\xc8\xa8\xb4v\xaf,\xb1n\x8b\xf5\xfe\xf8\r\xa7:r\xe8\xe0fvKN\\\xea\xe0\xa1\xe3\x99\xcc\xfd\x1a\x99Q\x90\xdf}\xae\xad'

key = xor(ct, b"\x10")[-16:]
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(xor(ct, key))
print(pt)