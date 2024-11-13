def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


### Step-by-Step Execution for `factorial(5)`

# 1. **Initial Call:** `factorial(5)`
#     - Since n is not 0, it goes to the `else` block.
        
#         nn
        
#     - It returns 5×factorial(5−1), which simplifies to 5×factorial(4).
        
#         5×factorial(5−1)5 \times \text{factorial}(5 - 1)
        
#         5×factorial(4)5 \times \text{factorial}(4)
        
# 2. **Next Call:** `factorial(4)`
#     - Again, n is not 0, so it calculates 4×factorial(4−1), which is 4×factorial(3).
        
#         nn
        
#         4×factorial(4−1)4 \times \text{factorial}(4 - 1)
        
#         4×factorial(3)4 \times \text{factorial}(3)
        
# 3. **Next Call:** `factorial(3)`
#     - Similarly, it calculates 3×factorial(3−1), which is 3×factorial(2).
        
#         3×factorial(3−1)3 \times \text{factorial}(3 - 1)
        
#         3×factorial(2)3 \times \text{factorial}(2)
        
# 4. **Next Call:** `factorial(2)`
#     - This results in 2×factorial(2−1), which is 2×factorial(1).
        
#         2×factorial(2−1)2 \times \text{factorial}(2 - 1)
        
#         2×factorial(1)2 \times \text{factorial}(1)
        
# 5. **Next Call:** `factorial(1)`
#     - Now, it calculates 1×factorial(1−1), which is 1×factorial(0).
        
#         1×factorial(1−1)1 \times \text{factorial}(1 - 1)
        
#         1×factorial(0)1 \times \text{factorial}(0)
        
# 6. **Base Case:** `factorial(0)`
#     - Here, n=0, so the function returns 1, as per the base case `if n == 0`.
        
#         n=0n = 0
        

### Resolving the Recursive Calls

# Now that we have reached the base case, we can work back up the recursive chain:

# - `factorial(1)` returns 1×1=1.
    
#     1×1=11 \times 1 = 1
    
# - `factorial(2)` returns 2×1=2.
    
#     2×1=22 \times 1 = 2
    
# - `factorial(3)` returns 3×2=6.
    
#     3×2=63 \times 2 = 6
    
# - `factorial(4)` returns 4×6=24.
    
#     4×6=244 \times 6 = 24
    
# - `factorial(5)` returns 5×24=120.
    
#     5×24=1205 \times 24 = 120
    

# ### Final Result

# So, `factorial(5)` ultimately returns **120**.