## List comprehension is way of construct list in small code

ls = [x for x in range(10)]
print(ls)

##condition for even number in list comprehension
ls1 = [x for x in range(2,101) if x%2==0]
print("even numbers are:",ls1)

## prime numbers in 1 to 100

prime_numbers = [x for x in range(1,101) if all(x%i !=0 for i in range(2,x))]
print("primes numbers are :", prime_numbers)
