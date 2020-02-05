
"""
    Teste PyJobs - 
"""

#
# Função
#

def lucro(inp):
    x = []
    b=[]
    l = len(inp)
    for x in range(l):
        a = [a-inp[x] for a in inp[x+3:]]   #Compara todas as possíveis transações apartir do recebimento no terceiro dia.
        if a == []:
            b.append(0) # Quando não há transações
        else:
            b.append(max(a))    # faz com que , mesmo que haja várias transações lucrativas, apenas a maior seja utilizada
    return max(b)


#
# Entradas Teste
#

inp = [7,1,5,3,6,4]

inp2 = [7,6,4,3,1]

#
# Execuções
#

print(lucro(inp))
print(lucro(inp2))