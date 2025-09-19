def binary(num, current_branch=[], branches=[]):
    if len(current_branch) == num:
        copy = current_branch.copy()
        branches.append(copy)
        return branches
    for i in range(0,2):
        if i == 0 and current_branch != [] and current_branch[-1] == 0:
            continue
        current_branch.append(i)
        binary(num, current_branch, branches)
        current_branch.pop()
    return branches

print(binary(3))