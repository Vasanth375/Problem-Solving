# def check(arr: list):
#     k = False
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if 0 <= abs(arr[i] - arr[j]) and abs(arr[i] - arr[j]) <= 2:
#                 k = True
#             else:
#                 return False

#     if k:
#         if 0<=abs(arr[0]-arr[-1]) and abs(arr[0]-arr[-1])<=2:
#             return True
#     return False

# nums = [5,4,2,4]
# nums = [1,2,3]
# count = len(nums)
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if check(nums[i:j+1]):
#             count += 1
# print(count)

from collections import deque
nums = [5,4,2,4]

count = 0
left = 0  # Start of the sliding window
min_deque, max_deque = deque(), deque()

for right in range(len(nums)):
    # Add the current element to the deques
    while min_deque and nums[min_deque[-1]] > nums[right]:
        min_deque.pop()
    while max_deque and nums[max_deque[-1]] < nums[right]:
        max_deque.pop()
    min_deque.append(right)
    max_deque.append(right)

    #Everytime we check the min and max value in current window
    # Shrink the window from the left if it's invalid
    while nums[max_deque[0]] - nums[min_deque[0]] > 2:
        left += 1
        # Remove elements outside the window
        if min_deque[0] < left:
            min_deque.popleft()
        if max_deque[0] < left:
            max_deque.popleft()

    # Count all valid subarrays ending at `right`
    count += (right - left + 1)

print(count)