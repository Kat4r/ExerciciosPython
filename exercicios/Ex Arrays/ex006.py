cart = [
  { 'name': 'Dark Souls III', 'price': 95.03 },
  { 'name': 'Shadow of the Tomb Raider', 'price': 101.19 },
  { 'name': 'Sekiro: Shadows Die Twice', 'price': 179.99 },
  { 'name': 'Resident Evil 2', 'price': 119.90 },
  { 'name': 'Death Stranding', 'price': 149.99 }
]
step = 0
for i in cart:
    for v in i.values():
        if step == 0:
            print(f"- Nome {v}", end='')
            step += 1
        else:
            print(f" / Preço {v}\n")
            step = 0

            