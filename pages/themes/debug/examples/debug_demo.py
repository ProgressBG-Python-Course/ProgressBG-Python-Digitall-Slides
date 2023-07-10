def sum_numbers(num_range):
  suma = 0
  for i in num_range:
    suma =+ i
    import pdb; pdb.set_trace()

  return suma

def main():
  print( sum_numbers(range(1,10)) )

if __name__ == '__main__':
  main()
