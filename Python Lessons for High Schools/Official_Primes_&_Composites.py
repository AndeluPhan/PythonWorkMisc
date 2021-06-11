
prime_numbers = []
composite_numbers = []

lower = int(input('Chose lower range: '))
upper = int(input('Chose upper range: '))

print('processing...')

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                composite_numbers.append(num)
                break
        else: 
            prime_numbers.append(num)

print('Finished processing.')
print('\nprime numbers are:' + str(prime_numbers))
print('Number of prime numbers: ', len(prime_numbers))
print('\ncomposite numbers are:' + str(composite_numbers))
print('Number of composite numbers: ', len(composite_numbers))
