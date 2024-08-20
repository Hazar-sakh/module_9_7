def is_prime(func):
  def wrapper(*args):
      result = func(*args)
      prime = False
      for i in range(0, result + 1):
          if i > 1:
              if result != i and result % i == 0:
                  prime = False
                  break
              else:
                  prime = True
                  break
      if prime:
          print('Простое')
          return result
      else:
          print('Составное')
          return result
  return wrapper

@is_prime
def sum_three(*args):
  s = sum(args)
  return s

result = sum_three(2, 3, 6)
print(result)