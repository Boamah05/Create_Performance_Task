import college_lists as l



def main():
  print('Welcome to the OMEGA Future, a program that will help you plan your future. This program will aid you in deciding which college you should attend based on your high school merits. This program is only for students who reside in Texas.\n')

def ask():
  global area
  gpa = float(input('\nEnter your Final highschool GPA (Weigthed): '))
  for i in l.locations:
    print(i, end=' \n')
  area = str(input('\nEnter your desired location of study '))
  q = str(input('\nDo you have you taken the SAT yet? (y/n): '))
  if q == 'y':
    sat = int(input('\nEnter your SAT score: '))
  else:
    sat = 0
  return gpa, sat, area
    
def verify(gpa, sat, area):
  if gpa > 4.0 or gpa < 0:
    print('\nInvalid GPA')
    while gpa > 4.0 or gpa < 0:
        gpa = float(input('Enter your Final highschool GPA (Weigthed): '))
  elif gpa <= 4.0 and gpa >= 0:
    print('\nGPA Accepted')
    pass
  if sat > 1600 or sat < 0:
    print('\nInvalid SAT score')
    while sat > 1600 or sat < 0:
      sat = int(input('Enter your SAT score: '))
  elif sat <= 1600:
    print('\nSAT score Accepted')
    pass
  if area not in l.locations:
    print('Invalid location of study. Please try again. Here are the list of college locations to choose from:')
    for i in l.locations:
      print(i, end=' \n')
    while area not in l.locations:
      area = str(input('Enter your desired location of study: '))
  elif area in l.locations:
    print('\nArea location Accepted')
    pass
  return gpa, sat, area
  

def fetch_college(area, gpa, sat):
  global choices
  choices = []
  if area == 'Austin':
    for i in l.austin:
      choices.append(i)
  elif area == 'Houston':
    for i in l.houston:
      choices.append(i)
  elif area == 'Dallas' or area == 'Fort Worth':
    for i in l.dallas_fort:
      choices.append(i)
  elif area == 'Destin':
    for i in l.destin:
      choices.append(i)
  elif area == 'San Antonio':
    for i in l.san_antonio:
      choices.append(i)
  elif area == 'Corpus Christi':
    for i in l.corpus_christi:
      choices.append(i)
  elif area == 'Waco' or area == 'Kileen':
    for i in l.waco_kileen:
      choices.append(i)

  print('\nHere are your availabile college choices in your selected area: ')
  for choice in choices:
    print(choice['name'], end=' \n')
  college(gpa, sat)

def college(gpa, sat):
  ask = str(input('\nWould you like to base this college selection on GPA or SAT? (g/s): '))
  if ask == 'g':
    print('These collleges would be the best for you based on your final high school GPA:\n')
    for x in choices:
      if x['average_GPA'] < gpa or x['average_GPA'] == 0:
        name = x['name']
        location = x['location']
        score = x['SAT_range']
        point = x['average_GPA']
        print(f'\n{name} , {location}\nAdmissions: GPA {point} SAT: {score}' , end=' \n')
        
      elif x['average_GPA'] < gpa:
        pass
        choices.remove(x)
        
  if ask == 's':
    print('These collleges would be the best for you based on your SAT score:\n')
    for x in choices:
      if x['SAT_range'] < sat or x['SAT_range'] == 0:
        name = x['name']
        location = x['location']
        score = x['SAT_range']
        point = x['average_GPA']
        print(f'\n{name} , {location}\nAdmissions: GPA {point} SAT: {score}' , end=' \n')

      elif x['SAT_range'] < sat:
        pass
        choices.remove(x)
