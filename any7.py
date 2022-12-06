def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE
    if 7 in nums:
        return True
    else:
        return False

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

print(any7([1,2,3,4,5,6,8,9]))
print(any7([1,2,3,4,5,6,7,8,9]))