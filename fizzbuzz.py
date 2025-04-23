for i in range(1, 13+1):
    if i % 3 == 0:
        print('fizzbuzz')
    elif i % 15 == 0:
        print('fizz')
    else:
        print(f'{i}')
