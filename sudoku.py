def nextOne(arr,i=0,j=0):
	for l in range(i,9):
		for k in range(j,9):
			if arr[l][k] == 0:
				return l,k
	for l in range(9):
		for k in range(9):
			if arr[l][k]==0:
				return l,k
	return -1,-1


def r_check(arr,i,value):
	for k in range(9):
		if arr[i][k]==value:
			return True
	return False

def col_check(arr,j,value):
	for k in range(9):
		if arr[k][j]==value:
			return True
	return False

def box_check(arr,i,j,value):
	m = i -i%3
	n = j - j%3
	for k in range(m,m+3):
		for o in range(n,n+3):
			if arr[k][o]== value:
				return True
	return False

def possible(arr,i,j,value):
	return not r_check(arr,i,value) and not col_check(arr,j,value) and not box_check(arr,i,j,value)

def solve(arr,i=0,j=0):
	i,j = nextOne(arr,i,j)
	if i == -1:
		return True
	for m in range(1,10):
		if possible(arr,i,j,m):
			arr[i][j]=m
			if solve(arr,i,j):
				return True
			arr[i][j]=0
	return False
def display(arr):
	for i in range(9):
		for j in range(9):
			arr[i][j]=str(arr[i][j])
	for i in range(0,9):
		print(" ".join(arr[i]))
arr =[]
print("Enter the Grid")
for i in range(0,9):
	temp = input().split()
	for i in range(9):
		temp[i]=int(temp[i])
	arr.append(temp)
solve(arr)
display(arr)

