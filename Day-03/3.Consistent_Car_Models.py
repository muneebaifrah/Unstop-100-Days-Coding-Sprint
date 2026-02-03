def count_consistent_cars(components, models):
    allowed = set(components)  
    count = 0
    for model in models:
        if all(c in allowed for c in model):
            count += 1
    return count


components = input().strip()
n = int(input().strip())
models = input().strip().split()  
result = count_consistent_cars(components, models)
print(result)
