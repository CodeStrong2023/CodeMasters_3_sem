def celsius_fahrenheit(celsius):
        return  celsius * 9 / 5 + 32 # Precedencia operación

def fahrenhei_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 /9


celsius = float(input('Digite el valor en celsius'))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -->{resultado:.2f} ')

fahrenheit = float(input('Digite ekl valor en fahrenheit'))
resultado = fahrenhei_celsius(fahrenheit)
print(f'{fahrenheit} F a C --> {resultado:.2f}')