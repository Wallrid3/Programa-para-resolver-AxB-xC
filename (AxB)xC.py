# ==========================================
# Exercício 3.3 - Operações com conjuntos
# Um programa par aresolver a letra n (AxB)xC)
# ==========================================

# Conjunto universo
S = set(range(10))

print("========================================")
print("         CONJUNTO UNIVERSO")
print("========================================")

print("O conjunto universo S contém os elementos:")
print("S =", S)

print("\nTodos os elementos dos conjuntos A e B")
print("devem pertencer ao conjunto universo S.")

# ------------------------------------------
# Entrada dos conjuntos A e B
# ------------------------------------------


def ler_conjunto(nome):
    entrada = input(
        f"Digite os elementos do conjunto {nome} "
        "(separados por espaço): "
    )

    try:
        conjunto = {int(x) for x in entrada.split()}
        
        # Verifica se os elementos pertencem ao universo
        if not conjunto.issubset(S):
            print(f"Erro: os elementos devem estar entre 0 e 9.")
            return ler_conjunto(nome)

        return conjunto

    except ValueError:
        print("Erro: digite apenas números inteiros.")
        return ler_conjunto(nome)


A = ler_conjunto("A")
B = ler_conjunto("B")

#Aqui mantivemos o conjunto C fixo como na atividade 3.3 apresentada, mas você pode alterá-lo conforme necessário.
# C = {x | x ∈ Z e 2 <= x < 5}
C = {x for x in S if 2 <= x < 5}

# Produto cartesiano
# A × B = {(a,b) | a ∈ A e b ∈ B}
def produto_cartesiano(A, B):
    return [(a, b) for a in sorted(A) for b in sorted(B)]


# ------------------------------------------
# Resultados
# ------------------------------------------
import time

print("\n================================")
print("        CONJUNTOS DIGITADOS")
print("================================")

#Aqui é para fazer a graça que sistema ta pensando (Os pokect da vida)
time.sleep(3)

print("================================")
print("          RESULTADO")
print("================================")

#Aqui o sistema vai mostrar o resultado do produto cartesiano de A e B e depois o produto cartesiano do resultado com C
time.sleep(3)
print("n) (A × B) × C =",
      produto_cartesiano(
    produto_cartesiano(A, B), C
      ))


print("FIM DA OPERAÇÃO")