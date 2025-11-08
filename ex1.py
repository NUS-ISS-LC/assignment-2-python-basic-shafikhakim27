def find(s, n):
    # Search for n in the list s
    for i in range(len(s)):
        if s[i] == n:
            return i
    return None

# Produce an integer array
nums = [10, 20, 30, 40, 50]

# Test the function
print("Array:", nums)
print("Find 30:", find(nums, 30))   # Output: 2
print("Find 100:", find(nums, 100)) # Output: None