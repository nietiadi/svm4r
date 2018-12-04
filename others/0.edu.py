from random import randint

def get_operator() -> str:
  if randint(0,1):
    return '+'
  else:
    return '-' 


def get_question(operator:str) -> (str, int):
  num1 = randint(0,20)
  num2 = randint(0,20)
  if operator == "+":
    return (""+str(num1)+operator+str(num2)+"=", num1+num2)
  elif operator == "-":
    if num1>num2:
      return (""+str(num1)+operator+str(num2)+"=", num1-num2)
    else:
      return (""+str(num2)+operator+str(num1)+"=", num2-num1)
  else:
    return "Not supported"
    

#print(get_operator())
MAX = 10
wrong = 0
for i in range(1,MAX+1):
  op = get_operator();
  ques = get_question(op);
  res = input(ques[0])
  if int(res.strip()) != ques[1]:
    wrong += 1
print("Wrong answer:"+str(wrong))    
