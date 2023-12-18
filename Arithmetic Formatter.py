def arithmetic_arranger(problems, T = None):
  arranged_problems = ""
  ans = list(); op1 = list(); op2 = list(); d = list()

  a = problems

  for i in range(len(a)):
    op1.append("  " + a[i].split()[0])
    op2.append(a[i].split()[1] + " " + a[i].split()[2])

    while len(op1[i]) != len(op2[i]):
      if len(op1[i]) > len(op2[i]):
        op2[i] = op2[i][0] + " " + op2[i][1:]
      elif len(op2[i]) > len(op1[i]):
        op1[i] = " " + op1[i]
      
    d.append(len(op1[i])*"-")

    try:
      ans.append((len(op1[i]) - len(str(eval(a[i])))) * " " + str(eval(a[i])))
    except:
      arranged_problems = "Error: Numbers must only contain digits."
      break

  if arranged_problems == "Error: Numbers must only contain digits.":
    pass

  elif len(a) > 5:
    arranged_problems = "Error: Too many problems."
  
  else:
    for i in range(len(a)):
      if op2[i][0] == "*" or op2[i][0] == "/":
        arranged_problems = "Error: Operator must be '+' or '-'."
        break
  
      if len(op1[i]) > 6 or len(op2[i]) > 6:
        arranged_problems = "Error: Numbers cannot be more than four digits."
        break
    
    if arranged_problems == "Error: Numbers cannot be more than four digits." or arranged_problems == "Error: Operator must be '+' or '-'.":
      pass
    
    else:
      if T == True:
        arranged_problems = "    ".join(op1) + "\n" + "    ".join(op2) + "\n" + "    ".join(d) + "\n" + "    ".join(ans)
      else:
        arranged_problems = "    ".join(op1) + "\n" + "    ".join(op2) + "\n" + "    ".join(d)
  
  return arranged_problems