from collections import deque
import random
import copy
q=deque()
visited=set()
n=int(input())
def ra():
    for i in range(0,n):
        row=[]
        for j in range(0,n):
            row.append(random.randint(1,4))
        t.append(row)    
    return t
def swapup(front,index1,index2):
	g=copy.deepcopy(front)
	g[index1][index2],g[index1-1][index2]=g[index1-1][index2],g[index1][index2]
	nw=tuple(sum(g,[]))
	if(nw not in visited):
		q.append(g)
		#print("g is printed")
		#print(g)
		visited.add(nw)
def swapdown(front,index1,index2):
	f=copy.deepcopy(front)
	f[index1][index2],f[index1+1][index2]=f[index1+1][index2],f[index1][index2]
	nw1=tuple(sum(f,[]))
	#print(type(f))
	#print nw1
	if(nw1 not in visited):
		#print("f is printed")
		q.append(f)
		visited.add(nw1)
def swapright(front,index1,index2):
	h=copy.deepcopy(front)
	h[index1][index2],h[index1][index2+1]=h[index1][index2+1],h[index1][index2]
	nw2=tuple(sum(h,[]))
	if(nw2 not in visited):
		#print("h is printed")
		q.append(h)
		visited.add(nw2)
def swapleft(front,index1,index2):
	m=copy.deepcopy(front)
	m[index1][index2],m[index1][index2-1]=m[index1][index2-1],m[index1][index2]
	nw3=tuple(sum(m,[]))
	if(nw3 not in visited):
		#print("m is printed")
		q.append(m)
		visited.add(nw3)
def goal(t):
	for i in range(0,n):
		for j in range(0,n): 
			if(j>=1 and t[i][j]==t[i][j-1]):
				return 0
			if(j<n-1 and t[i][j]==t[i][j+1]):
				return 0
			if(i<n-1 and t[i][j]==t[i+1][j]):
				return 0
			if(i>=1 and t[i][j]==t[i-1][j]):
				return 0
			
	return 1
t=[]
t=ra()
print(t)
if(goal(t)==1):
    print("Goal Reached")
    print("Seriously???")
else:
    q.append(t)
    c=0
    #print(q.popleft())
    while(len(q)!=0):
    	c+=1
    	front=q.popleft()
    	nw=sum(front,[])
    	visited.add(tuple(nw))
    	#print(c)
    	#print("front is printed")        
    	#print(front)
    	if(goal(front)==1):
    		print("So easily?")
    		print("Goal Reached")
    		print(front)
    		exit()
    	else:
    		i=0
    		
    		for i in range(0,n):
    			for j in range(0,n):
    			
    				#print(i,j)
    				#print "inside"
    				if(j>=1 and front[i][j]==front[i][j-1]):
    					if(i>=1 and front[i-1][j]!=front[i][j]):
    						swapup(front,i,j)
            			if(i<n-1 and front[i][j]!=front[i+1][j]):
            				swapdown(front,i,j)
            			if(j<n-1 and front[i][j]!=front[i][j+1]):
            				swapright(front,i,j)
            		if(j<n-1 and front[i][j]==front[i][j+1]):
            			#print("right")
            			if(i>=1 and front[i-1][j]!=front[i][j]):
            				swapup(front,i,j)
            			if(i<n-1 and front[i][j]!=front[i+1][j]):
            				swapdown(front,i,j)
            			if(j>=1 and front[i][j]!=front[i][j-1]):
            				swapleft(front,i,j)
            		
            		if(i<n-1 and front[i][j]==front[i+1][j]):
            			#print("down")
            			if(i>=1 and front[i-1][j]!=front[i][j]):
            				swapup(front,i,j)
            			if(j<n-1 and front[i][j]!=front[i][j+1]):
            				swapright(front,i,j)
            			if(j>=1 and front[i][j]!=front[i][j-1]):
            				swapleft(front,i,j)
            		
            		if(i>=1 and front[i][j]==front[i-1][j]):
            			#print("up")
            			if(i<n-1 and front[i][j]!=front[i+1][j]):
            				swapdown(front,i,j)
            			if(j<n-1 and front[i][j]!=front[i][j+1]):
            				swapright(front,i,j)
            			if(j>=1 and front[i][j]!=front[i][j-1]):
            				swapleft(front,i,j)
            		
    				

    		
    print(c)        
            

