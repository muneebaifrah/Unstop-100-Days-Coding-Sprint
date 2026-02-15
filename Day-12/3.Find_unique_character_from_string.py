def determine_winner(N, smit_str, joy_str):
    # Count unique characters
    smit_unique = len(set(smit_str))
    joy_unique = len(set(joy_str))
    
    # Calculate mean
    smit_mean = smit_unique / N
    joy_mean = joy_unique / N
    
    # Compare and determine winner
    if smit_mean > joy_mean:
        return "SMIT"
    elif joy_mean > smit_mean:
        return "JOY"
    else:
        return "TIE"

# Read input
if __name__ == "__main__":
    N = int(input())
    smit_str = input().strip()
    joy_str = input().strip()
    print(determine_winner(N, smit_str, joy_str))
