stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()
stdform = stdform.replace('x10^', 'E')
print('This number in E notation is', stdform)
