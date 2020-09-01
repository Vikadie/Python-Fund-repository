population = [int(i) for i in input().split(", ")]
minimum_wealth = int(input())

ans = []
possible = 1
for i in population:
    if i < minimum_wealth:
        diff = minimum_wealth - i
        i_index = population.index(i)
        ind = population.index(max(population))
        while diff > 0:
            if max(population) <= minimum_wealth:
                possible = 0
                break
            elif max(population) >= minimum_wealth + diff:
                population[i_index] = minimum_wealth
                population[ind] -= diff
                diff = 0
            else:
                diff -= (max(population) - minimum_wealth)
                population[i_index] += max(population) - minimum_wealth
                population[ind] = minimum_wealth
                ind = population.index(max(population))
        if possible == 0:
            break

if possible:
    print(population)
else:
    print("No equal distribution possible")
