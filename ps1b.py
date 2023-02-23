###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here'
    #print("Egg weight[-1]:" , egg_weights[-1])
    #base case for recursion
    #smallest egg is heavier than remaining weight

    if egg_weights == () or target_weight < egg_weights[0]: 
        #print("In base case")
        result = (0, ())
        memo[egg_weights[:], target_weight] = result
    
    try: 
        return memo[egg_weights[:], target_weight]
    
    except KeyError:
    #if largest egg is too heavy, move to second egg and only build left node 
        if egg_weights[0] > target_weight: 
            #print("In elif")
            result = dp_make_weight(egg_weights[:-1], target_weight, memo)
            memo[egg_weights[:], target_weight] = result
            
            
        
        #If heaviest egg is a valid option, build both sides
        else: 
            #print("In else")
            #build right node 
            #print("building right node")
            nextItem = egg_weights[0] 
            withVal, withToTake = dp_make_weight(egg_weights[:], target_weight - nextItem, memo)
            withVal += nextItem
            
            #build left node 
            #print("building left node")
            withoutVal, withoutToTake = dp_make_weight(egg_weights[1:], target_weight, memo)
            
            #chose the better option
            #right node better
            #print("withVal: ", withVal)
            #print("withoutVal: ", withoutVal)
            if withVal > withoutVal: 
                #print("Right node better")
                result = (withVal, withToTake + (nextItem, ))
                memo[egg_weights[:], target_weight] = result
            #left node better
            else: 
                #print("left node better")
                result = (withoutVal, withoutToTake)
                memo[egg_weights[:], target_weight] = result
    return result

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()