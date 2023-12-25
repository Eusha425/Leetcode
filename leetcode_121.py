# 121. Best Time to Buy and Sell Stock

def best_but(prices):
    min = 9999 
    max = 0
    
    for i in range(len(prices)):
        if prices[i] < min:
            min = prices[i]
        result = prices[i] - min
        if result > max:
            max = result

        
    return max

arr = [7,1,5,3,6,4]

print(best_but(arr))
    
