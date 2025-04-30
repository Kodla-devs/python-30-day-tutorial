selam = "merhaba"

kopya = selam

yeni_kopya = selam

print(id(selam))
print(id(kopya))

import sys
print(sys.getrefcount(selam))