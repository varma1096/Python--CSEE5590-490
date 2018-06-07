def print_hor(h):
    print(" --- " *h)

def print_vert(w):
    print("|   " * (w+1))

h_i =int(input("Enter the height of the board :"))
w_i =int(input("Enter the width of the board :"))

for index in range(h_i):
    print_hor(h_i)
    print_vert(w_i)

print_hor(h_i)