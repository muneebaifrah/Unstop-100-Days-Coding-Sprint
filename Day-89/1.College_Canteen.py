def count_workers_unable_to_collect_parts(workers, parts):
    count0 = workers.count(0)
    count1 = workers.count(1)
    
    for p in parts:
        if p == 0:
            if count0 == 0:
                return count1
            count0 -= 1
        else:
            if count1 == 0:
                return count0
            count1 -= 1
    return 0


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    workers = list(map(int, data[1:n+1]))
    parts = list(map(int, data[n+1:2*n+1]))
    
    result = count_workers_unable_to_collect_parts(workers, parts)
    print(result)

if __name__ == "__main__":
    main()