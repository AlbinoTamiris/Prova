def makeChange(n):
    #função para calcular as formas de representar
    # uma quantidade de centavos em quarters, dimes, nickels e pennies
    results = set()

    def helper(quarters, dimes, nickels, pennies, remaining):
        if remaining == 0:  # não há mais valor para dividir
            results.add((quarters, dimes, nickels, pennies))
            return
        if remaining >= 25:  # Tenta adicionar um quarter
            helper(quarters + 1, dimes, nickels, pennies, remaining - 25)
        if remaining >= 10:  # Tenta adicionar um dime
            helper(quarters, dimes + 1, nickels, pennies, remaining - 10)
        if remaining >= 5:  # Tenta adicionar um nickel
            helper(quarters, dimes, nickels + 1, pennies, remaining - 5)
        if remaining >= 1:  # Tenta adicionar um penny
            helper(quarters, dimes, nickels, pennies + 1, remaining - 1)

    # Chama a função auxiliar com valores iniciais
    helper(0, 0, 0, 0, n)
    return results

# Um exemplo de uso:
n = 12
combinations = makeChange(n)

# Imprimindo as combinações

print(f"Combinations to make {n} cents:")
for combination in combinations:
    print(combination)


