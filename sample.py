/////////    
t=int(input())
for i in range(t):
    d,x,y,z=map(int,input().split())
    way1=x*7
    way2=y*d+z*(7-d)
    ma=max(way1,way2)
    print(ma)
    
# cook your dish here
t=int(input())
for i in range(t):
    N,X,Y,A,B=map(int,input().split())
    pc=(X/A)*N
    dc=(Y/B)*N
    if pc < dc:
        print("petrol")
    elif dc< pc:
        print("diesel")
    else:
        print("any")
        
        
        ////////////
n=int(input())
i=1
count=0
while (i<=n):
	if (n%i==0):
		count=count+1
	i=i+1
if (count==2):
	print("yes")
else:
	print("no")
	
	////////////
t = int(input())
for i in range(t):
    x = int(input())
    d=0
    if (x%4==0):
        d=int(x/4)
    else:
        d=int(x/4)+1
    print(d)
    
 ///////////////
t=int(input())
for i in range(t):
    a,b=list(map(int,input().split()))
    c,d=list(map(int,input().split()))
    if(a+c ==180):
        print("yes")
    elif (b+d ==180):
        print("yes")
    else:
        print("no")
        
        
        
        
        
t=int(input())
for i in range(t):
	x=int(input())
	z=x//4
	print((z)+1)
	
	
	
for i in range(int(input())):
    n=int(input())
    s=input()
    c1=s.count("1")
    if c1+(120-n)>=90:
        print("YES")
    else:
        print("NO")
        

### ap free squence
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        for j in range(i+1,n-1):
            for k in range(i+1,n):
            
                if a[j]-a[i]==a[k]-a[j]:
                    ans=1
                    break
    if ans==0:
        print("yes")
    else:
        print("no")
            
    
    
##print binary array    
t = int(input())
while (t > 0):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    t -= 1

