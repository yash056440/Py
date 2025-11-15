num = (-523, 842, -193, 756, -999, 315, 420, -88, 602, -731, 
458, 214, -310, 789, -62, -875, 990, 111, -404, 703, 
-241, 569, 0, -782, 998, -65, 327, -493, 81, 932, 
-847, -621, 479, 333, -412, 155, 886, -900, 290, -107, 
515, -681, 903, -234, 611, -972, 450, -189, 318, 707, 
-54, -330, 95, 820, -476, 129, -915, 628, -205, 941, 
-749, 377, -63, 88, -556, 712, -800, 553, -411, 642, 
-32, -593, 744, -109, 872, -271, 600, -458, 315, 997, 
-683, 59, -370, 875, -295, 441, -752, 143, 867, -607, 
391, -911, 236, 702, -152, 429, -869, 508, -12, 650)


ttl_ten = 0
ttl_odd = 0  
ttl_even = 0  
ttl_p = 0 
ttl_n = 0
ttl_z = 0
ttl = 0
n_ten =0
n_odd = 0
n_even =0
n_p =0
n_n =0
n_z = 0

for c in num:

    if c > 0:
        ttl_p += c
        n_p += 1
    elif c < 0:
        ttl_n += c
        n_n += 1
    else:
        ttl_z += 1
        n_z += 1

  
    if c % 2 == 0:
        ttl_even += c
        n_even += 1
    else:
        ttl_odd += c
        n_odd += 1

  
    if c % 10 == 0:
        ttl_ten += c
        n_ten += 1

  
    ttl += c

print("Positive sum & count :", ttl_p, n_p)
print("Negative sum & count :", ttl_n, n_n)
print("Zero count           :", n_z)
print("Divisible by 10 sum & count :", ttl_ten, n_ten)
print("Odd sum & count :", ttl_odd, n_odd)
print("Even sum & count:", ttl_even, n_even)
print("Total sum :", ttl)



    

