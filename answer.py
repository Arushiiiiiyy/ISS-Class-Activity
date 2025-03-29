def find_cube_pairs(targ):      #The variable should be targ and there should be a colon    
    sol = []                     #solutions converted to sol 
    max_num = round(targ ** (1/3))  #only 2 * (power)

    for a in range(1, max_num + 1):     #ranges=range and colon
        for b in range(a, max_num + 1): #ranges=range and colon
            if a**3 + b**3 == targ:     #colon at the end of if and only 2 stars for power
                sol.append((a, b))
    return sol

pairs = find_cube_pairs(1729)      
print("Valid cube pairs for 1729:")    #printf converted to print and 1728 converted to 1729
for a, b in pairs:               #pair = pairs and colon
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")    #printf=print and a**2 converted to a**3 and 1728 converted to 1729
