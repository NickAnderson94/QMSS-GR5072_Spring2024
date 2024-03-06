

# Create function for the fibonacci sequence 
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# # Quick test function
# fib(1)
# fib(2)
# fib(-1)  # Function only exists for the set of zero and all positive integers
# fib(1.2)
# 
# # Print the first 10 fibonacci numbers
# for i in range(11):
#   print( "Fib(" + str(i) + ") = " + str(fib(i)))


