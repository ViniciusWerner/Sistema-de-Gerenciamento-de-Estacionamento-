import estacionamento

def main() -> None:
    while True:
        print("\n--- Sistema de Gerenciamento de Estacionamento ---")
        print("1. Registrar cliente e veículo")
        print("2. Registrar entrada")
        print("3. Listar clientes")
        print("4. Ver arrecadação do dia")
        print("5. Ver arrecadação do mês")
        print("6. Ver utilização de um veículo no mês")
        print("7. Listar bonificações")
        print("8. Listar ranking de veículos")
        print("9. Sair")
        
        opcao = int(input("Escolha uma opção: ").strip())
        try:
            match opcao:
                case 1:
                    print("--- REGISTRO DE VEÍCULO ---")
                    nome: str = input("Digite o nome do cliente: ").strip()
                    placa: str = input("Digite a placa do veículo: ").strip()
                    data: str = input("Digite a data (formato: dd/mm/aaaa): ").strip()
                    res = estacionamento.registrarVeiculo(nome, placa, data)
                    print(f"{nome.capitalize()} pagou uma taxa de R$20 para realizar o registro do veículo de placa ({res.placa})")
                    print("---------------------------")
                case 2:
                    print("--- REGISTRO DE ENTRADA ---")
                    placa = input("Digite a placa do veículo: ").strip()
                    horas = int(input("Digite o número de horas: ").strip())
                    data = input("Digite a data (formato: dd/mm/aaaa): ").strip()
                    res = estacionamento.registrarEntrada(placa, horas, data)
                    print(str(res))
                    print("---------------------------")
                case 3:
                    res = estacionamento.listarClientes()
                    print("--- CLIENTES ---")
                    print(res)
                    print("----------------")
                case 4:
                    print("--- ARRECAÇÃO DO DIA ---")
                    data = input("Digite a data (formato: dd/mm/aaaa): ").strip()
                    res = estacionamento.listarArrecadacaoDia(data)
                    print(f"R$ {res}")
                    print("------------------------")
                case 5:
                    print("--- ARRECAÇÃO DO MÊS ---")
                    data = input("Digite a data (formato: dd/mm/aaaa): ").strip()
                    res = estacionamento.listarArrecadacaoMes(data)
                    print(f"R$ {res}")
                    print("------------------------")
                case 6:
                    print("--- UTILIZAÇÃO DO VEÍCULO NO MÊS---")
                    placa = input("Digite a placa do veículo: ").strip()
                    data = input("Digite a data (formato: mm/aaaa): ").strip()
                    res = estacionamento.listarUtilizacaoVeiculoMes(placa, data) 
                    print(res)
                    print("-----------------------------")
                case 7:
                    res = estacionamento.listarBonificacoes()
                    print("--- BONIFICAÇÕES ---")
                    print(res)
                    print("--------------------")
                case 8:
                    res = estacionamento.listarRankingVeiculos()
                    print("--- RANKING ---")
                    print(res)
                    print("---------------")
                case 9:
                    break
                case _:
                    print("\033[31m" + "Opção inválida. Por favor, tente novamente." + "\033[0m")
        except Exception as e:
            print("\033[31m" + "Ocorreu um erro: " + str(e) + "\033[0m")


main()
