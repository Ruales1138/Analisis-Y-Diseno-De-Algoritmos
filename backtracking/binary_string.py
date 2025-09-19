def binary_string(num, current_branch=[], branches=[]):
    if len(current_branch) == num:
        copy = current_branch.copy()
        branches.append(copy)
        return branches
    for i in range(0,2):
        #if current_branch == []
        if current_branch[-1] != 0:
            current_branch.append(i)
            binary_string(num, current_branch)
            current_branch.pop()

    return branches
    

print(binary_string(3))