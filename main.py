
def findDifferentBinaryString(nums):
    result = ""

    for i in range(len(nums)):
        if nums[i][i] == '0':
            result += '1'
        else:
            result += '0'

    return result


# Example
nums = ["110", "011", "001"]

answer = findDifferentBinaryString(nums)

print("Input:", nums)
print("Output:", answer)
