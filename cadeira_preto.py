# complete os exercícios abaixo, adicione as docstrings no padrão correto (pra que serve, oque recebe, oque retorna)
# não esqueça do cabeçalho do arquivo



# Verifica se o numero e par
def e_par(n: int) -> bool:
    """ 
     Verifica se o n umero e par
     args:
     (n: int)
     n variavel que recebe o numero inteiro
     Returns:
     true se for par e false para impar

    """
    return n % 2 == 0

def fatorial(n: int) -> int:

    """ 
    Calcula o fatorial de um numero n
    args:
    (n: int)
    n variavel que recebe o numero inteiro
    Returns:
    Retorna o fatorial do numero n
    """

    if n <0:
        raise ValueError("nao deve ser negativo")
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado
    

# Retorna o maior elemento de uma lista 
def maximo(nums):
    
    """
    Recebe uma lista de numeros e retorna o maior numero
    args:
    nums: lista de numeros
    retuns:
    maior numero dentro dessa lista

    """
    if not nums:
        raise ValueError("lista vazia")
    maior = nums[0]
    for n in nums:
        if n > maior:
            maior = n
    return maior


def total_por_vendedor(vendas):
    """
    Calcula o total vendido por cada vendedor.
    args:
    vendas: lista de tuplas (nome, valor).
    Returns:
    dict {nome: soma_valores}

    """
    totais = {}
    for nome, valor in vendas:
        if nome in totais:
            totais[nome] += valor
        else:
            totais[nome] = valor
    return totais
    ...

def melhor_vendedor(totais: dict):
    """
    Retorna o vendedor com maior total vendido.
    args:
    dict {nome: total}.
    returns:
    (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    Raise ValueError se o dicionario estiver vazio
    """
    if not totais:
        raise ValueError("dicionario vazio")
    
    melhor_vendedor = None
    maior_total = float('-inf')
    for nome, total in totais.items():
        if total > maior_total:
            maior_total = total
            melhor_vendedor = nome
    return melhor_vendedor, maior_total


