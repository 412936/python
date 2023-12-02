#6var
subject =  {'r': [3, 25],
         'p': [2, 15],
         'a': [2, 15],
         'm': [2, 20],
         'i': [1, 5],
         'k': [1, 15],
         'x': [3, 20],
         't': [1, 25],
         'f': [1, 15],
         'd': [1, 10],
         's': [2, 20],
         'c': [2, 20]
         }

size = 3
inf = True
d = True
points = 15


backpack = [['-' for j in range(size)] for i in range(size)]
point = 0

def add_item_to_backpack(items):
    global point
    item = subject[items]
    item_size = item[0]
    item_points = item[1]
    for i in range(size):
        for j in range(size):
            if backpack[i][j] == '-':
                if item_size <= size - i and item_size <= size - j:
                    backpack[i][j] = items
                    point += item_points
                    return True
    return False

if inf and d:
    add_item_to_backpack('d')

while True:
    item_added = False
    for items in subject.keys():
        if add_item_to_backpack(items):
            item_added = True
    if not item_added:
        break

for i in range(size):
    for j in range(size):
        print("[{}]".format(backpack[i][j]), end="")
    print()
print("Итоговые очки выживания:", point)