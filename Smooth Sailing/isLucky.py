def isLucky(n):
    
    n1 = str(n)
    lenght = len(n1)
    nsplit = [int(i) for i in n1]

    first_half = 0
    second_half = 0
    for i in range(lenght):
        if (i // 2):
            first_half += nsplit[i]
        else:
            second_half += nsplit[i]

    if first_half == second_half:
        return True
    else:
        return False
        
### 4 Test Failed 


# method 2 
def isLucky(n):

    n1 = str(n)

    n2 = n1[0:len(n1)//2]
    n3 = n1[len(n1)//2:]

    first_half = 0
    second_half = 0
    for i in n2:
        first_half += int(i)
    for i in n3:
        second_half += int(i)
    if first_half == second_half:
        return True
    else:
        return False
# all test passed
