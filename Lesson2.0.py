sec = int(input('Enter seconds: '))
a = ((sec // 3600)) % 24
b = (sec // 60) % 60
c = sec % 60

print('%d:%02d:%02d' % (a, b, c))