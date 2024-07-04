text = '100%'
try:
    number = int(text)
except ValueError:
    print(f'{text}는 숫자가 아니네요.')
