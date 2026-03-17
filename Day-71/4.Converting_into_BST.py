n = int(input().strip())
arr = list(map(int, input().split()))

# build tree array
tree = arr

# inorder traversal of binary tree in array representation
inorder_vals = []

def inorder(index):
    if index >= n:
        return
    inorder(2*index + 1)
    inorder_vals.append(tree[index])
    inorder(2*index + 2)

inorder(0)

# create strictly increasing target
target = []
prev = -10**18

for x in inorder_vals:
    if x > prev:
        target.append(x)
        prev = x
    else:
        prev += 1
        target.append(prev)

# sum increments
ans = 0
for orig, tar in zip(inorder_vals, target):
    ans += tar - orig

print(ans)