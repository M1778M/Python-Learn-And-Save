import hashlib as hs
import base64 as bs
#sha1 / sha256
sha = hs.sha1("string".encode('utf-8'))
print(sha.digest())
#md2 / md5
print(hs.md5('Hello'.encode('utf-8')).hexdigest())

##########33
t = hs.md5("Hello".encode('utf-8')).digest()

print(bs.b64decode(b"%s" % (t)))