def distance(coor1,coor2):
        return (((coor2[0]-coor1[0])**2)+((coor2[1]-coor1[1])**2))**0.5

def perfectsquare(n):
    c=n//2 + 1
    for i in range(1,c):
        if ((n % i == 0) and (n / i == i)): 
            return True
    return False

def isPerfectSquare(n) : 
  
    i = 1
    while(i * i<= n): 
          
        # If (i * i = n) 
        if ((n % i == 0) and (n / i == i)): 
            return True
              
        i = i + 1
    return False

while True:
    s=int(input('please enter number'))
    m=perfectsquare(s)
    #m=perfectsquare(s)   23232323232222
    print(m)
    

#coordinate1 = (-3,-2)
coordinate2 = (-1,-2)
coordinate1 = (2,-2)

li = distance(coordinate1,coordinate2)
#print(li)
    