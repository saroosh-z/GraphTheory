import numpy as np
inf = 10000 	

adjacency_matrix = [
	[0,2,4,3],
	[3, 0, inf, 3],
	[5, inf, 0, 3],
	[inf, 1, 4, 0],
	]


v = 4
'''distance_matrix =  np.empty( shape = [v, v], dtype = int)
print(distance_matrix)
for i in range(v):
	print('i is:', i)
	for j in range(v):
		print('j is:', j)
		print(f'changing {i}, {j}')
		np.put(distance_matrix, [i,j], 0)'''

print('Printing current edge weights')
for i in range(v):
	print('[', end='')
	for j in range(v):
		print(f'{adjacency_matrix[i][j]} ', end='' )
	print('],')

#distance_matrix[0][1] = np.append(distance_matrix, [9][8])

distance_matrix = list(map(lambda i : list(map(lambda j : j , i)) , adjacency_matrix))
print(list(distance_matrix))
def floydsAlgorithm(matrix):
	# there are 4 virtices, k = 0,  1 < i <= v, 1 < j <= v
	global distance_matrix
	#STEP 1: K = 0:
		#	distance_matrix is the adjacency_matrix
	for k in range(v):
		for i in range(v):
			for j in range(v):
				distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
				#print(distance_matrix[i][j])
	print('printing distance_matrix')
	for i in range(v):
		print('[', end='')
		for j in range(v):
			print(f'{distance_matrix[i][j]} ', end='' )
		print('],')

	#STEP 2: K = 1

		#D(k)[i, j] = min(D(k-1)[i, j], D(k-1)[i,k]+D(k-1)[i, j])

floydsAlgorithm(adjacency_matrix)
