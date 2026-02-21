# A generator function is a special type of function that returns an iterator object
# Instead of using return to send back a single value, generator functions use yield to produce a series of results over time 
# The function pauses its execution after yield, maintaining its state between iterations
def fun(max):
   cnt = 1
   while cnt <= max:
      yield cnt
      cnt += 1

ctr = fun(5)
for n in ctr:
   print(n)

# Why Do We Need Generators?
   # Memory Efficient : Handle large or infinite data without loading everything into memory
   # No List Overhead : Yield items one by one, avoiding full list creation
   # Lazy Evaluation : Compute values only when needed, improving performance
   # Support Infinite Sequences : Ideal for generating unbounded data like Fibonacci series
   # Pipeline Processing : Chain generators to process data in stages efficiently

#  Yield vs Return
   # Yield: is used in generator functions to provide a sequence of values over time 
   # When yield is executed, it pauses the function, returns the current value and retains the state of the function
   # This allows the function to continue from same point when called again, making it ideal for generating large or complex sequences efficiently
   
   # Return: is used to exit a function and return a final value 
   # Once return is executed, function is terminated immediately and no state is retained 
   # This is suitable for cases where a single result is needed from a function

# Generator expressions are a concise way to create generators
# They are similar to list comprehensions but use parentheses instead of square brackets and are more memory efficient
sq = (x*x for x in range(1, 6))
for i in sq:
   print(i)