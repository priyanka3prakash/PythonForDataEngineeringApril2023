import base64

# encoding & encryption

# print(dir(base64))

sentence = "Today is good day"

# encoded = base64.b64encode(sentence)
# TypeError: a bytes-like object is required, not 'str'

# result = sentence.encode("utf-8")  # str to bytes
# print(type(result))

encoded = base64.b64encode(sentence.encode("utf-8"))
print(f"encoded     : {encoded}")   #  b'VG9kYXkgaXMgZ29vZCBkYXk='

original_msg = base64.b64decode(encoded)
print(f"original_msg: {original_msg}")  #  b'Today is good day'


# Assignment : try base16, base84, base128
