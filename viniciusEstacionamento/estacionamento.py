from typing import Any, Optional, Set


# Definindo estruturas

class Data:
    dia: int
    mes: int
    ano: int

    def __init__(self, dia: int, mes: int, ano: int) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano

class Veiculo:
    nomeCliente: str
    placa: str
    createdAt: Data

    def __init__(self, nomeCliente: str, placa: str, createdAt: Data) -> None:
        self.nomeCliente = nomeCliente
        self.placa = placa
        self.createdAt = createdAt

class Entrada:
    placaVeiculo: str
    horas: int
    createdAt: Data

    def __init__(self, placaVeiculo: str, horas: int, createdAt: Data) -> None:
        self.placaVeiculo = placaVeiculo
        self.horas = horas
        self.createdAt = createdAt

    def __str__(self) -> str:
        return f"Registrado! Placa: {self.placaVeiculo}, Horas: {self.horas}, Data: {self.createdAt.dia}/{self.createdAt.mes}/{self.createdAt.ano}"


# Funções auxiliares

## Filtros de Veículos

def filterVeiculosByPlaca(veiculos: list[Veiculo], placa: str) -> Optional[Veiculo]:
    for v in veiculos:
        if v.placa == placa:
            return v
    return None

def filterVeiculosByNomeCliente(veiculos: list[Veiculo], nomeCliente: str) -> list[Veiculo]:
    res: list[Veiculo] = []
    for v in veiculos:
        if v.nomeCliente == nomeCliente:
            res.append(v)
    return res

def filterVeiculosByDia(veiculos: list[Veiculo], data: Data) -> list[Veiculo]:
    res: list[Veiculo] = []
    for v in veiculos:
        if v.createdAt.dia == data.dia and v.createdAt.mes == data.mes and v.createdAt.ano == data.ano:
            res.append(v)
    return res
    
def filterVeiculosByMes(veiculos: list[Veiculo], data: Data) -> list[Veiculo]:
    res: list[Veiculo] = []
    for v in veiculos:
        if v.createdAt.mes == data.mes and v.createdAt.ano == data.ano:
            res.append(v)
    return res

## Filtros de Entradas

def filterEntradasByPlaca(entradas: list[Entrada], placa: str) -> list[Entrada]:
    res: list[Entrada] = []
    for e in entradas:
        if e.placaVeiculo == placa:
            res.append(e)
    return res

def filterEntradasByDia(entradas: list[Entrada], data: Data) -> list[Entrada]:
    res: list[Entrada] = []
    for e in entradas:
        if e.createdAt.dia == data.dia and e.createdAt.mes == data.mes and e.createdAt.ano == data.ano:
            res.append(e)
    return res

def filterEntradasByMes(entradas: list[Entrada], data: Data) -> list[Entrada]:
    res: list[Entrada] = []
    for e in entradas:
        if e.createdAt.mes == data.mes and e.createdAt.ano == data.ano:
            res.append(e)
    return res

## Criadores

def createData(data: str) -> Data:
    s: list[str] = data.split("/")
    if len(s) == 3 and len(s[0]) == 2 and len(s[1]) == 2 and len(s[2]) == 4:
        dia = int(s[0])
        mes = int(s[1])
        ano = int(s[2])
        return Data(dia, mes, ano)
    else:
        raise Exception('Formato de data inválida')

# Sistema

veiculos: list[Veiculo] = []
entradas: list[Entrada] = []
taxaVeiculo = 20
taxaEntrada = 5

def registrarVeiculo(nomeCliente: str, placa: str, data: str) -> Veiculo:
    v: Optional[Veiculo] = filterVeiculosByPlaca(veiculos, placa)
    if v:
        raise Exception('Placa já cadastrada!')
    else:
        newV = Veiculo(nomeCliente, placa, createData(data))
        veiculos.append(newV)
        return newV

def registrarEntrada(placaVeiculo: str, horas: int, data: str) -> Entrada:
    v: Optional[Veiculo] = filterVeiculosByPlaca(veiculos, placaVeiculo)
    if v:
        e = Entrada(placaVeiculo, horas, createData(data))
        entradas.append(e)
        return e
    else:
        raise Exception('Placa não cadastrada!')

def listarClientes() -> Set[str]:
    res: Set[str] = set()
    for v in veiculos:
        res.add(v.nomeCliente.capitalize())
    return res

def listarArrecadacaoDia(data: str) -> float:
    total_arrecadado = 0
    total_arrecadado += len(filterVeiculosByDia(veiculos, createData(data))) * taxaVeiculo
    total_arrecadado += sum(e.horas * taxaEntrada for e in filterEntradasByDia(entradas, createData(data)))
    return total_arrecadado

def listarArrecadacaoMes(data: str) -> float:
    total_arrecadado = 0
    total_arrecadado += len(filterVeiculosByMes(veiculos, createData(data))) * taxaVeiculo
    total_arrecadado += sum(e.horas * taxaEntrada for e in filterEntradasByMes(entradas, createData(data)))
    return total_arrecadado

def listarUtilizacaoVeiculoMes(placa: str, data: str) -> str:
    entradas_do_mes = filterEntradasByMes(filterEntradasByPlaca(entradas, placa), createData("01/" + data))
    if not entradas_do_mes:
        return "Nenhuma entrada registrada para este veículo neste mês."
    
    total_horas = sum(entrada.horas for entrada in entradas_do_mes)
    return f"Utilização do veículo com placa {placa} no mês {data}: {total_horas} horas + (Bonificação: {__calcularBonificacaoDaPlaca__(entradas, placa)} horas)"

def __calcularBonificacaoDaPlaca__(entradas: list[Entrada], placa: str) -> float:
    entradasDoVeiculo: list[Entrada] = filterEntradasByPlaca(entradas, placa)
    horas = 0
    for e in entradasDoVeiculo:
        horas += e.horas
    if horas >= 10:
        return horas * 0.10
    else:
        return 0

def listarBonificacoes() -> str:
    res: str = ""
    for v in veiculos:
        bonificacao: float = __calcularBonificacaoDaPlaca__(entradas, v.placa)
        res += f'Bonificação para o veículo {v.placa}: {bonificacao}h'
    return res

def listarRankingVeiculos() -> str:
    count: dict[str, int] = dict()
    for e in entradas:
        if e.placaVeiculo in count:
            count[e.placaVeiculo] += e.horas
        else:
            count[e.placaVeiculo] = e.horas
    ranking: list[Any] = []
    for k, v in count.items():
        ranking.append({"placaVeiculo": k, "horas": v})
    ranking.sort(key=lambda x: x["horas"], reverse=True)
    res: str = ""
    for i, e in enumerate(ranking):
        bonificacao: float = __calcularBonificacaoDaPlaca__(entradas, e["placaVeiculo"])
        res += f'{i + 1} - Placa {e["placaVeiculo"]} com {e["horas"]}h + (Bonificação: {bonificacao} horas)'
    return res

