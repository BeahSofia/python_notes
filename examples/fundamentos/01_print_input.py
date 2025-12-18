print("=== Exemplo 01: print e input ===")

nome = input("Qual é o seu nome?")
idade = input("Quantos anos você tem?")

# Converter par número (pode dar erro se o usuário não digitar um número)
idade = int(idade)

print(f"Olá, {nome}! Ano que vem você terá {idade + 1} anos.")

