from random import randint

"""xDy+z
Types of dice used in games: D3, D4, D6, D8, D10, D12, D20, D100.
"""

def dice_throw(throw):
    temp = throw.split("D")
    x = 1 if temp[0] == "" else int(temp[0])
    print(f"X:{x}")
    y_z = temp[1]

    symbol = "+"
    if "-" in y_z:
        symbol = "-"

    temp = y_z.split(symbol)

    y = int(temp[0])
    z = int(temp[1]) if len(temp) > 1 else 0
    print(f"Y:{y}")
    print(f"Z:{z}")

    result = 0
    for _ in range(x):
        result += randint(1,y)

    result = eval(f"{result}{symbol}{z}")

    return result



print(dice_throw("2D10+10"))
print("-----------------")
print(dice_throw("D6"))
print("-----------------")
print(dice_throw("2D3"))
print("-----------------")
print(dice_throw("D12-1"))