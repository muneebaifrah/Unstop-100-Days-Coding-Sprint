def user_logic(arr1, arr2):
    # Write your logic here.
    # Parameters:
    #     arr1 (list of str): First array of strings
    #     arr2 (list of str): Second array of strings
    # Returns:
    #     bool: Computed result based on the problem statement
   # Placeholder return value
    st1=""
    st2=""
    for i in arr1:
        st1+=i
    for j in arr2:
        st2+=j
    if st1==st2:
        return True
    else:
        return False
    """st1=''.join(arr1)
    st2=''.join(arr2)
    return st1==st2"""
  
if __name__ == '__main__':
    n = int(input())
    arr1 =input().split()
    m = int(input())
    arr2 = input().split()

    result = user_logic(arr1, arr2)
    print('true' if result else 'false')