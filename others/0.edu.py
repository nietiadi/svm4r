import random

def get_operator() -> str:
  if random.randint(0,1):
    return '+'
  else:
    return '-' 

print(get_operator())
