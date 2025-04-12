# Angel Chavez Fri April 11th, 2025 19:02
# My solution for "canplaceflower" leetcode problem
# Python 3.12.9
# I got the solution from Addison and was able to recreate it in Python.

# I had ClaudeAI explain the code again to me and then tell me what sort of algorithm is used here. Essentially it is an algorithm called the 
# "Greedy Algorithm Approach". It works here because we need a "left-to-right, make-the-best-choice-now approach" 
# Interesting stuff!

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        list_size = len(flowerbed)

        # handles special case for a single-element flowerbed
        if list_size == 1:

            if (n == 1 and flowerbed[0] == 0 or n == 0):
                return True

            return False
        
        # checks each element in the flowerbed
        for i in range(list_size):

            # checks if we can plant at position "i"
            left_check = i == 0 or flowerbed[i - 1] == 0
            right_check = i == list_size - 1 or flowerbed[i + 1] == 0

            # if both checks pass and element is empty
            if left_check and right_check and flowerbed[i] == 0:
                # plant a flower and take 1 away from "n"
                flowerbed[i] = 1
                n -= 1
        
        # checks if we have any flowers left to plant
        if n > 0:
            return False
        return True