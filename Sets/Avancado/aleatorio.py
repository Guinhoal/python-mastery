import random 

conjunto1 = set()
conjunto2 = set()

iterator = random.randint(1, 30)
while iterator > 0:
    conjunto1.add(random.randint(1, 50))
    iterator -= 1

iterator = random.randint(1, 30)
while iterator > 0:
    conjunto2.add(random.randint(1, 50))
    iterator -= 1

print("União:")
print(conjunto1.union(conjunto2))
print("Interseção:")
print(conjunto1.intersection(conjunto2))
print("Diferença:")
print(conjunto1.difference(conjunto2))
