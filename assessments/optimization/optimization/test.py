from itertools import product

neighbors = [
                dict(zip(("wait duration", "toast duration", "power"), offsets))
                for offsets in product((-1, 0, 1), repeat=3)
                ]

print(neighbors)