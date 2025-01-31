#!/usr/bin/env python3

def calculator():
    print("KALKULATOR")
    print("Dostępne operacje: +, -, *, /")
    
    try:
        num1 = float(input("Podaj pierwszą liczbę: "))
        operator = input("Wybierz operację (+, -, *, /): ")
        num2 = float(input("Podaj drugą liczbę: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Błąd: Dzielenie przez zero!")
                return
            result = num1 / num2
        else:
            print("Nieprawidłowy operator!")
            return
        
        print(f"Wynik: {result}")
    except ValueError:
        print("Błąd: Wprowadź poprawne liczby!")

if __name__ == "__main__":
    calculator()
