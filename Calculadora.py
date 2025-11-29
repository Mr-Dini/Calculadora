print("Buenvenido a la calculadora")

while true:
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    choice = input("Ingrese su elección (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error: División por cero no permitida.")

    elif choice == '5':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break

    else:
        print("Entrada inválida. Por favor, intente de nuevo.")
