import os
import shutil
version = "a1.0.0"
class debug():
  def crash():
    exit()
  def overload():
    return basic.hextate(100, 100)
  def uninstall():
    os.remove("bettermath.py")
  def fullwipe():
    x = input("Please, PLEASE make sure you mean to do this. Fullwipe will wipe EVERYTHING from main.py, this package, and the readme!!!!!!! If you are sure, please enter the phrase 'bettermath.py' into the input.")
    if x == "bettermath.py":
      os.remove("bettermath.py")
      os.remove("main.py")
      os.remove("readme.readme")
  def version():
    return version

class stats():
  def weightedmean(*weightnum: tuple):
    result = 0
    for i in weightnum:
      result += i[0]*i[1]
    result /= len(weightnum)
    return result
  def amean(*numbers: float):
    x = 0.0
    for i in range (len(numbers)):
      x += numbers[i]
    x /= len(numbers)
    return x
  def gmean(*numbers: float):
    x = 1.0
    for i in range(len(numbers)):
      x *= numbers[i]
    length = float(len(numbers))
    x = x**(1/length)
    return x
  def hmean(*numbers: float):
    x = 0.0
    for i in range(len(numbers)):
      x += 1/numbers[i]
    x /= len(numbers)
    x **= -1
    return x
  def agmean(a0, g0, tolerance=1e-10):
    an, gn = (a0 + g0) / 2.0, (a0 * g0)**0.5
    while abs(an - gn) > tolerance:
        an, gn = (an + gn) / 2.0, (an * gn)**0.5
    return an
  def median(*numbers):
    y = numbers
    lst = []
    for i in y:
      lst.append(i)

    medInd = int(len(lst)/2)

    if len(lst)%2!=0:
      med = lst[medInd]
    else:
      med = (lst[medInd] + lst[medInd-1])/2
    
    return med
  def mode(*numbers):
    currentrecord = 0
    numberofnumbers = {}
    for i in numbers:
      if str(i) in numberofnumbers.keys():
        numberofnumbers[str(i)] += 1
      else:
        numberofnumbers[str(i)] = 1
      if numberofnumbers[str(i)] > currentrecord:
        currentrecord = numberofnumbers[str(i)]
    modes = []
    for x in numberofnumbers.keys():
      if numberofnumbers[x] >= currentrecord:
        modes.append(x)
    return str(modes)
  def corr(*data: tuple):
    n = len(data)
    sumofx = 0
    sumofy = 0
    sumofxy = 0
    sumofx2 = 0
    sumofy2 = 0
    for i in data:
      sumofx += i[0]
      sumofy += i[1]
      sumofxy += i[0]*i[1]
      sumofx2 += i[0]**2
      sumofy2 += i[1]**2
    corr = ((n*sumofxy)-(sumofx*sumofy))/(((n*sumofx2-(sumofx)**2)*(n*sumofy2-(sumofy)**2))**0.5)
    return corr
  def stddev(*data):
    mean = 0
    dmean = 0
    distancesfrommean = []
    for i in data:
      mean += i
    mean /= len(data)
    for i in data:
      distancesfrommean.append((i-mean)**2)
    for i in distancesfrommean:
      dmean += i
    dmean /= len(data)
    dmean **= 0.5
    return dmean
  def sum(*data: int):
    sum = 0
    for i in data:
      sum += i
    return sum
  
    
    
    
    



class constants():
  def e():
    return 2.718281828
  def pi():
    return 3.1415926536
  def tau():
    return constants.pi()*2
  def phi():
    return (1+5**0.5)/2
  def gamma():
    return 0.577215664902
class basic():
  def sum(*numbers):
    result = 0
    for x in numbers:
      result += x
    return result
  def natlog(value, accuracy=1000):
    result = (accuracy+1)*(value**(1/(accuracy))-1)
    return result
  def log(base, value, accuracy=1000):
    result = basic.natlog(value, accuracy)/basic.natlog(base, accuracy)
    return result
  def root(root, number):
    return number**(1/root)
  def tetrate(number, power):
    result = number
    for x in range(power):
      result = result**number
    return result
  def pentate(number, power):
    result = number
    for x in range(power):
      result = basic.tetrate(result, number)
    return result
  def hextate(number, power):
    result = number
    for x in range(power):
      result = basic.pentate(result, number)
    return result
  def factorial(number):
    number = int(number)
    result = 1
    if number == 0:
      result = 1
    else:
      result = basic.factorial(number-1)*number
    return result
  def choose (first, second):
    if first >= second:
      result = (basic.factorial(first))/basic.factorial(second)*basic.factorial(first-second)
      return result
    else:
      raise ValueError("The first number must be greater than or equal to the second!")
  def digits(number):
    tracker = number
    result = 1
    while (tracker >= 10):
      tracker /= 10
      result += 1
    return result
  def abs(number):
    if number >= 0:
      return number
    else:
      return 0-number
  
class help():
  def help():
    print("help here")  

  
    
