# Programa que decide se um dado número é feliz ou não.
# Um número é feliz se ao se realizar uma soma dos quadrados dos digitos do número,
# obtém-se ao final o número 1 (possivelmente após várias iterações).
# Não é feliz caso contrário.


def main():
    numero: str = input("Digite um número: ")

    while not numero.isnumeric():
        print("Entrada inválida. Digite apenas números!")
        numero: str = input("Digite um número: ")

    if feliz(numero):
        print(f"{numero} é um número feliz.")
    else:
        print(f"{numero} não é um número feliz.")


def digitos_quadrados(numero: str) -> int:
    soma: int = 0

    for digito in numero:
        soma += int(digito) ** 2

    return soma


def feliz(numero: str) -> bool:
    numeros_calculados: List[int] = []
    soma_parcial: int = digitos_quadrados(numero)

    # Todo número não-feliz passa pelo ciclo 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ...
    # Então, achar uma repetição desse ciclo é uma condição de parada.
    while soma_parcial > 1 and soma_parcial not in numeros_calculados:
        numeros_calculados.append(soma_parcial)
        soma_parcial = digitos_quadrados(str(soma_parcial))

    return soma_parcial == 1

if __name__ == "__main__":
    main()
