#Crear set vacio
from cgi import print_form


s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(2)

print(s)
s.remove(1)
print(s)

print(f"El set tiene {len(s)} elementos.")


