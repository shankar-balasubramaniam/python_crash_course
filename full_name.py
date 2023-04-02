first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'

print(full_name)

message = f'Hello, {full_name.title()}!'
print(message)

# f-strings are only available from Python 3.6 and above
# for older versions of Python 3, use the format method
full_name = '{} {}'.format(first_name, last_name)
print(full_name)

print('Python')
print('\tPython')

print('Languages:\n\tPython\n\tC\n\tJavaScript')
