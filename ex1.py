def find(s, n):
    """Return the index of n in list s, or None if not found."""
    try:
        return s.index(n)
    except ValueError:
        return None

def twoSum(numbers, target):
    """Find two indices in the list where values sum to target."""
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test the function
print(twoSum([2,7,11,15], 9))   # Output: [0,1]
print(twoSum([3,2,4], 6))       # Output: [1,2]
print(twoSum([3,3], 6))         # Output: [0,1]