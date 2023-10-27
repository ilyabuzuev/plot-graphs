import matplotlib.pyplot as plt



file = open('12x12x10_changed.txt', 'r')

x = []
y = []

symbol = 'X'

for line in file:
  if not symbol in line:
    continue
  else:
    print(line)

    splittedLine = line.split(' ')

  x.append(float(splittedLine[1].replace('X', '')))
  y.append(float(splittedLine[2].replace('Y', '')))

file.close()

print(x)
print(y)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
