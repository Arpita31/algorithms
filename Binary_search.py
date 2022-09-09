_input = [2, 5, 34, 58, 89, 144, 296, 980]

def binary_search(inp: list[int], target):
    '''
        Binary search using iteration.
        Args: 
            inp : Input Array
            target : The element to be found
        Return:
            The position of the Target element in Array.
    '''
    left, right = 0, len(inp) - 1

    while left <= right:
        mid = left + (right - left)//2

        if inp[mid] == target:
            return mid
        elif inp[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1    # If target is not found.

def binary_search_recursion(inp: list[int], target, left , right):
    '''
        Binary search using Recursion.
        Args: 
            inp : Input Array
            target : The element to be found
            left: left index of search space
            right: right index of search space
        Return:
            The position of the Target element in Array.
    '''
    if left > right:
        return -1
    mid = left + (right - left)//2

    if inp[mid] == target:
        return mid
    elif inp[mid] > target:
        return binary_search_recursion(inp, target, left, mid - 1)
    else:
        return binary_search_recursion(inp, target, mid + 1, right)
        
if __name__ == "__main__":
    print(f"Target found on position: {binary_search(_input, 144)} ")
    print(f"Target found on position: {binary_search_recursion(_input, 144, 0, 8)}")

