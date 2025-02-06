def greedy_algorithm(items, budget):

    # Створюємо список калорій до вартості
    items_with_ratio = []
    for item, data in items.items():
        items_with_ratio.append((item, data["calories"] / data["cost"]))

    # Сортуємо страви за спаданням співвідношення калорій до вартості
    items_with_ratio.sort(key=lambda x: x[1], reverse=True)

    selected_items = []
    total_calories = 0
    remaining_budget = budget

    # Вибираємо страви, поки не досягнемо бюджету
    for item, ratio in items_with_ratio:
        cost = items[item]["cost"]
        calories = items[item]["calories"]

        if cost <= remaining_budget:
            selected_items.append(item)
            total_calories += calories
            remaining_budget -= cost

    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)

    # Таблицю для зберігання результатів
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюєм таблицю
    for i in range(1, n + 1):
        item = list(items.keys())[i - 1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]

        for j in range(1, budget + 1):
            if cost <= j:
                dp[i][j] = max(calories + dp[i - 1][j - cost], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # Список обраних страв
    selected_items = []
    i = n
    j = budget
    while i > 0 and j > 0:
        item = list(items.keys())[i - 1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]

        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(item)
            j -= cost

        i -= 1

    return selected_items, dp[n][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Greedy algorithm:")
print("Selected items:", greedy_result[0])
print("Total calories:", greedy_result[1])

dynamic_result = dynamic_programming(items, budget)
print("\nDynamic programming:")
print("Selected items:", dynamic_result[0])
print("Total calories:", dynamic_result[1])