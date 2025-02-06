import random

def roll_dice(num_rolls):
    results = {}
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        if total in results:
            results[total] += 1
        else:
            results[total] = 1
    return results

def calculate_probabilities(results, num_rolls):
    probabilities = {}
    for total, count in results.items():
        probabilities[total] = count / num_rolls
    return probabilities

# Кількість симуляцій
num_rolls = 100000  

# Виконуємо
results = roll_dice(num_rolls)

# Рахуємо ймовірності
probabilities = calculate_probabilities(results, num_rolls)


print("Сума\tЙмовірності")
print("-" * 25)
for total in sorted(probabilities.keys()):
    print(f"{total}\t{probabilities[total]:.4f}")