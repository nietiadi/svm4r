from random import randint


def get_operator() -> str:
  if randint(0,1):
    return '+'
  else:
    return '-' 


def get_question(operator:str, lower_limit:int, upper_limit:int) -> (str, int):
  num1 = randint(lower_limit,upper_limit)
  num2 = randint(lower_limit,upper_limit)
  if operator == "+":
    return (""+str(num1)+operator+str(num2)+"=", num1+num2)
  elif operator == "-":
    if num1>num2:
      return (""+str(num1)+operator+str(num2)+"=", num1-num2)
    else:
      return (""+str(num2)+operator+str(num1)+"=", num2-num1)
  else:
    return "Not supported"
    

#version 1
def input_an_integer1(prompt:str) -> int:
  while True:
    res = input(prompt)
    try:
      res_int = int(res.strip())
    except:
      print("Not a number. Try again.")
      continue
    return res_int


#version 2
def input_an_integer2(prompt:str) -> int:
  while True:
    res = input(prompt)
    if not res.strip().isdigit():
      print("Not a number. Try again.")
      continue
    else:
      return int(res.strip())
  

#==== main ====
MAX = 2
lower_limit = 5
upper_limit = 20
wrong = 0
for i in range(1,MAX+1):
  op = get_operator();
  ques = get_question(op, lower_limit, upper_limit);
  res = input_an_integer2("("+str(i)+") "+ques[0])
  if res != ques[1]:
    wrong += 1
    #print("Wrong!")
print("Wrong answers:"+str(wrong))    
