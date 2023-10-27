f = open('12x12x10.txt', 'r')
o = open('12x12x10_changed.txt', 'w')

for line in f:
  print(line)

  newLine = line.replace(',', '.')

  o.write(newLine)

f.close()
o.close()