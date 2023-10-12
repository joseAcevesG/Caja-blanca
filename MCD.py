# maximo comun divisor
def mcd(x, y):
    if x <= 0 or y <= 0:
        print("No deben ser negativos")
        return -1
    elif x == 1 or y == 1:
        return 1
    else:
        while x != y:
            if x > y:
                x = x - y
            else:
                y = y - x
        return x


# test de la funcion mcd
if __name__ == "__main__":
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    print("El maximo comun divisor de", num1, "y", num2, "es", mcd(num1, num2))
