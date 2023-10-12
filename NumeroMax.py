def NumeroMax(x, y, z):
    if x > y and x > z:
        max_value = x
        max_variable = "x"
    elif z > y:
        max_value = z
        max_variable = "z"
    else:
        max_value = y
        max_variable = "y"
    
    return max_value, max_variable

if __name__ == "__main__":
    x = int(input("Introduce x: "))
    y = int(input("Introduce y: "))
    z = int(input("Introduce z: "))
    max_value, max_variable = NumeroMax(x, y, z)
    print("El máximo es:", max_value, ", contenido de la variable", max_variable)