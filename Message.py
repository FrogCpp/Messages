i = 0
a = []
global Work
while True:
  a.append(i)
  i += 1
  print(a)
  if i >= 100:
    Work = False
    break
