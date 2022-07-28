
'''
  This program show to you given year is leap or not
'''


def isLeapYear(year):
  isLeap = False
  if year%4==0 and year%100!=0:
    isLeap = True
  elif year%100==0 and year%400==0:
    isLeap = True
  return isLeap
  
  
if __name__=='__main__':
   year = input("Enter year:")
   if isLeapYear(year):
    print "year is Leap"
   else:
    print "year is not leap"
    
