def eliminar_mayor(nums: list[int], i: int = 0, mayor: int = None) -> int:
    if i == len(nums):
        nums.remove(mayor)
        return nums, mayor
    if mayor is None:
        mayor = nums[i]
    if nums[i] > mayor:
        mayor = nums[i]
    return eliminar_mayor(nums, i+1, mayor)

def k_esimo(nums: list[int], k: int, i: int = 0, mayor = None):
    if i == k:
        return mayor
    nums, mayor = eliminar_mayor(nums)
    return k_esimo(nums, k, i+1, mayor)


print(k_esimo([3,2,1,5,6,4], 2))
print(k_esimo([3,2,3,1,2,4,5,5,6], 4))

