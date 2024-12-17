def F(a):
  if a == 1:
    return 1
  else:
    return F(a - 1) + F(a - 2)
print(F(5))
