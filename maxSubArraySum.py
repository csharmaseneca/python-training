"""Q1 - Find out the max sum of the longest continues subarray. Kadane's Algo. Expected time complexity O(N), Space complexity O(1) or constant"""
"""The time complexity of kadane’s algorithm for an array containing n integer element is O(n) as only one for loop is to be executed throughout the program. Similarly, the auxiliary space complexity of the algorithm is O(1)."""
def maxSubArraySum(arr,size):
    
    max_till_now = arr[0]
    max_ending = 0
    
    for i in range(0, size):
        max_ending = max_ending + arr[i]
        if max_ending < 0:
            max_ending = 0
        
        
        elif (max_till_now < max_ending):
            max_till_now = max_ending
            
    return max_till_now

arr = [-20, -30, 4, -10, -2, 5, -3]
print("Maximum Sub Array Sum Is" , maxSubArraySum(arr,len(arr)))
