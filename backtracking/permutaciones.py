def permutaciones(nums, current_branch=[], branches=[]):
    if len(current_branch) == len(nums):
        copy = current_branch.copy()
        branches.append(copy)
        return branches
    for num in nums:
        if num not in current_branch:
            current_branch.append(num)
            permutaciones(nums, current_branch)
            current_branch.pop()
    return branches

print(permutaciones([1,2,3]))