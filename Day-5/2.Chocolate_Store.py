def process_queries(q, queries):
    stock = {}
    for query in queries:
        if query[0] == '1':
            choco = query[1]
            qty = int(query[2])
            if choco in stock:
                stock[choco] += qty
            else:
                stock[choco] = qty
        else:
            choco = query[1]
            qty = int(query[2])
            available = stock.get(choco, 0)
            sell = min(available, qty)
            print(sell)
            stock[choco] = available - sell

if __name__ == "__main__":
    q = int(input())
    queries = [input().split() for _ in range(q)]
    process_queries(q, queries)
