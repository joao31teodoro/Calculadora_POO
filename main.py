from calculadora import Adicao, Subtracao, Multiplicacao, Divisao, Calculadora

def main():
    calc = Calculadora()
    operacoes = {"+": Adicao, "-": Subtracao, "*": Multiplicacao, "/": Divisao}

    while True:
        operacao_input = input("Digite a operação (+, -, *, /) ou '=' para calcular o total ou 'z' para desfazer a última operação: ")

        if operacao_input == "=":
            print(f"Resultado: {calc.calcular_total()}")
            continue
        elif operacao_input == "z":
            if calc.operacoes:
                calc.operacoes.pop()
                print("Última operação desfeita.")
            else:
                print("Nenhuma operação para desfazer.")
            continue
        elif operacao_input not in operacoes:
            print("Operação inválida. Tente novamente.")
            continue

        try:
            valor = float(input("Digite o valor para a operação: "))
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue
        operacao = operacoes[operacao_input](valor)
        calc.add_operacao(operacao)
        print(f"Operação {operacao_input} com valor {valor} adicionada.")

if __name__ == "__main__":
    main()
