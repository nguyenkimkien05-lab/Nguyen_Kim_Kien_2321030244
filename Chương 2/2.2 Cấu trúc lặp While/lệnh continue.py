# Vong lap while va continue trong Python

value = 5

while value > 0:
    value -= 1

    # Bo qua vong lap khi value = 3
    if value == 3:
        continue

    print("Gia tri hien tai:", value)
