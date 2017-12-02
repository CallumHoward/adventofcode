from hashlib import md5
from itertools import count

for a in count():
    if md5('ckczppom' + str(a)).hexdigest().startswith('000000'):
    #if md5('bgvyzdsv' + str(a)).hexdigest().startswith('000000'):
        print a
        break


input = 'ckczppom'
prefix = '000000'
print (a for a in count() if md5(input + str(a)).hexdigest().startswith(prefix)).next()
