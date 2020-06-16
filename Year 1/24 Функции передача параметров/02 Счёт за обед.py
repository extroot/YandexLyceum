def count_food(a):
    global daily_food
    return sum([daily_food[x - 1] for x in a])
