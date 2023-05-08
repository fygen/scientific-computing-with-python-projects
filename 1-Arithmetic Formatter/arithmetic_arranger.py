def maxlen(operation):
  return len(max(operation.split(" "),key=len))

def arithmetic_arranger(problems,calc=False):
#   print(problems, calc)
#   print(len(problems[0].split(" ")[0]))
  for problem in problems:   
    #print(maxlen(problem), end=" ")
    print(problem.split(" ")[0].rjust(maxlen(problem)+2), end="    ")
  print()  
  for problem in problems: 
    print(problem.split(" ")[1],problem.split(" ")[2].rjust(maxlen(problem)), end="    ")
  print()
  for problem in problems:
    print("-"*(maxlen(problem)+2),end="    ")
  print()
  if calc == True:
    for problem in problems:
      print(str(eval(problem)).rjust(len(str(eval(problem)))+2), end="    ")
  arranged_problems = 1
  return arranged_problems 