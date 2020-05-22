# Implementation of the natural logarithm function using the series expansion 2 * Sigma[ (1/(2i-1) * [(x-1)/(x+1)]^(2i-1) ] 
# for i = 1 to n
# @param x the number whose natural logarithm is to be approximated 
# @param n the number of terms in the series, i.e. the required level of precision 
# @return the approximated ln(x) value using the first n terms
# Note that each value is generated from its predecessor value
# Explicitly specifying n for now because defining it as some constant results in precision dropping off for larger values

def log(x, n):

    x = float(x) 
    n = int(n)

    if x <= 0:
        print("Error: Illegal argument. Value not in domain") # Domain restricted to positive reals
        return None

    # Declaring the releveant variables for the series
    alpha = (x-1)/(x+1)
    sigma = 0 

    # Evaluating ln(x) up to our specified precision level n using the series expansion 
    for odd in range(1, n, 2): 
        sigma += alpha/odd
        alpha *= ( (x-1)/(x+1) ) * ( (x-1)/(x+1) )
    result = 2 * sigma  
    return result 


x = input("Enter x: ")
n = input("Enter n: ")

print(log(x,n))

