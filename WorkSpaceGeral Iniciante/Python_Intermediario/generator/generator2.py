def generator(v=0, maximum=0):
    while True:
        yield v
        print(f"passou da interacao #{v}")
        v += 1
        if v > maximum:
            return "ACABOU"


gen = generator(maximum=10)

for n in gen:
    print(f"executavel #{n}")
