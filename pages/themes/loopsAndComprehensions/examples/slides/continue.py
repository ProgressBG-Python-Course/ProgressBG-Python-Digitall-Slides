print("IF: print all numbers in [1..5], but skip 3, and instead of 4 print 'four'")
i = 0
while i<5:
    i += 1
    if i==3:
        pass
    else:
        if i == 4:
            print("four")
        else:
            print(i)


print("\nCONTINUE: print all numbers in [1..5], nut skip 3")
i = 0
while i < 5:
    i += 1
    if i == 3:
       continue
    if i == 4:
        print("four")
    else:
        print(i)    
