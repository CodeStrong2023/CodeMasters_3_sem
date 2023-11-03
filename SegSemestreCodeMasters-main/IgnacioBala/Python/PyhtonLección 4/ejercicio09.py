frase1 = input("Digite una frase")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f"\nFRASE FINAL : {frase1}")
print(f"n de caracteres: {len(frase1)}")