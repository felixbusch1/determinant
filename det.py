#!/usr/bin/env python
import numpy as np
import argparse

parser = argparse.ArgumentParser()

#Setup arguments
parser.add_argument("-m", "--matrix", action="store", type=str, dest="matrix", required=True, 
                    help="Input matrix in numpy format (e.g '1 2 3; 4 5 6; 7 8 9').")

parser.add_argument("-d", "--dimension", action="store", type=int, dest="dimension", required=True,
                    help="Set the dimension of the input matrix.")

args = parser.parse_args()

# Function name: getBestColumn() (optional in this implementation)
#
# Description: This function returns the index of the column of the input matrix
# 	       with the most number of zeros in it. If there are no zeros in the matrix,
#	       the first column (index 0) will be returned.When we calculate the determinant 
#              of the matrix, we select the column with the most number of zeros, to have
#              a zero factor in multiplication. This function is optional.
#
# Parameters: matrix, n
#
#	     matrix:= Input matrix in numpy format (e.g 2x2 numpy.matrix('1 2; 3 4'))
#	     n	   := Dimension of the input matrix. In this example abolve n=2 of a 2x2 matrix
#
# Return value: The index of the column with the most number of zeros in it.

def getBestColumn(matrix, n):
    col = currentNumberOfZeros = totalNumberOfZeros = 0

    for i in range(n):
        
        #Select the i-th column vector of the matrix
        vector = matrix[:,[i]]
	
    	#Count the zeros for every entry in the vector
        for j in range(n):
            if vector.item(j) == 0:
                currentNumberOfZeros += 1
		
		        #Refresh selected column with the most number of zeros
		        #Refresh the total number of zeros
                if currentNumberOfZeros > totalNumberOfZeros:
                    totalNumberOfZeros = currentNumberOfZeros
                    col = i
   	    
	        #Reset for next iteration
            currentNumberOfZeros = 0
	
	    #Return the index of the column. 	
        return col



# Function name: det()
#
# Description: Algorithm of the Laplace expansion to calculate the determinant of a NxN matrix.
#	       Recursive implementation.
#	       
# Parameters: matrix, n
#
#	      matrix := The input matrix in numpy format (e.g 2x2 numpy.matrix('1 2; 3 4'))
#	      n	     := The dimension of the input matrix. In this example abolve n=2
#
# Return value: The determinant of the input matrix

def det(matrix, n):
    if n == 1:
        return matrix.item(0)
    #In case the dimension of the input matrix is n=2 
    if n == 2:
        return matrix.item(0) * matrix.item(3) - matrix.item(1) * matrix.item(2)
    else:

        #Set return value of the function to zero
        res = 0
	
	    #Every second iteration the sign switches, we use a simple lambda function for this.
	    #That means, sign(1) = 1, sign(3) = 1... sign(2*k+1) = 1 and sign(2*k) = -1
        sign = lambda x: 1 if x & 1 else -1
	
	    #We use always the first column of the matrix.

        vec = matrix[:,[0]]

	    #We have to calculate n- subdeterminants
        for i in range(n):
	    
	        #Delete the column with the most number of zeros in it	
            temp = np.delete(matrix, getBestColumn(matrix, n), axis=1)
            
            #Delete the i-th row of the matrix
            submatrix = np.delete(temp, i, axis=0)
            
            #Get the value of the sub determinant recursively
            x = det(submatrix, n-1)

            #Calculate the value of the determinant
            res += vec.item(i) * x * sign(i+1)            

        return res


#Print inputs
m = np.matrix(args.matrix)
print("Input matrix:")
print(m)

detvalue = det(m, args.dimension)

print("\n")
print("Dimension: " + str(args.dimension))

print("Determinant: " + str(detvalue))
