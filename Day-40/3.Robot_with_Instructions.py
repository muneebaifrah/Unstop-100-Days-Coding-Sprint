def execute_instructions(n, pos, instruction):
    m = len(instruction)
    answer = [0] * m  # Initialize the answer array

    # For each starting point in the instruction string
    for i in range(m):
        row, col = pos  # Start from the initial position
        steps = 0
        
        # Execute instructions starting from i
        for j in range(i, m):
            move = instruction[j]
            if move == 'L':
                col -= 1
            elif move == 'R':
                col += 1
            elif move == 'U':
                row -= 1
            elif move == 'D':
                row += 1
            
            # Check if robot is out of bounds
            if row < 0 or row >= n or col < 0 or col >= n:
                break
            steps += 1
        
        answer[i] = steps

    return answer

# Reading input and testing the function
if __name__ == "__main__":
    n = int(input())
    pos = list(map(int, input().split()))
    m = int(input())
    instruction = input().strip()

    result = execute_instructions(n, pos, instruction)
    print(*result)