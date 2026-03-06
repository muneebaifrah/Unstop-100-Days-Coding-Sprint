def process_queries(queries):
    size = 1000
    hashmap = [[] for _ in range(size)]
    
    def hash_func(key):
        return key % size
    
    result = []
    
    for q in queries:
        if q[0] == 1:  # insert/update
            _, key, value = q
            idx = hash_func(key)
            found = False
            
            for i, (k, v) in enumerate(hashmap[idx]):
                if k == key:
                    hashmap[idx][i] = (key, value)
                    found = True
                    break
            
            if not found:
                hashmap[idx].append((key, value))
        
        elif q[0] == 2:  # get
            _, key = q
            idx = hash_func(key)
            val = -1
            
            for k, v in hashmap[idx]:
                if k == key:
                    val = v
                    break
            
            result.append(val)
        
        elif q[0] == 3:  # delete
            _, key = q
            idx = hash_func(key)
            
            for i, (k, v) in enumerate(hashmap[idx]):
                if k == key:
                    hashmap[idx].pop(i)
                    break
    
    return result


if __name__ == "__main__":
    n = int(input().strip())
    queries = []
    
    for _ in range(n):
        parts = list(map(int, input().split()))
        queries.append(tuple(parts))
    
    ans = process_queries(queries)
    
    for x in ans:
        print(x)