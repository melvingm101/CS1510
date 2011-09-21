n = 5
A = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
R = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
p = [0, 0.05, 0.1, 0.2, 0.25, 0.5]

for i in range(1,n+1):
	A[i][i-1] = 0
	A[i][i] = p[i]
	R[i][i] = i
	R[i][i-1] = 0;

for d in range(1,n):
	for i in range(1,n-d+1):
		j = i+d
		w = 1000
		wk = 1000
		for k in range(i,j+1):
			print i, j, k
			if A[i][k-1]+A[k+1][j] < w:
				w = A[i][k-1]+A[k+1][j]
				wk = k
			A[i][j] += p[k]
		A[i][j] += w
		R[i][j] = wk

print A

print R
		
