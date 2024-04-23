import college_lists as l



#Display message for user
def main():
  print('Welcome to the OMEGA Future, a program that will help you plan your future. \nThis program will aid you in deciding which college you should attend based on your high school merits. This program is only for students who reside in Texas.\n')

#Ask user for high school GPA, SAT score, and desired area of college study

def ask():
  global area
  gpa = float(input('\nEnter your Final highschool GPA (Weigthed out of 4.0): '))
  print('These are the locations to choose from: \n')
  for i in l.locations:
    print(i, end=' \n')
  area = str(input('\nEnter your desired location of study '))
  q = str(input('\nHave you taken the SAT yet? (y/n): '))
  if q == 'y':
    sat = int(input('\nEnter your SAT score: '))
  else:
    sat = 0
  return gpa, sat, area

#Verification function for valdating gpa, sat score, and desired area of college study

def verify(gpa, sat, area):
  if gpa > 4.0 or gpa < 0: #If GPA is greater than 4 and less than 0, ask user to re-enter GPA until valid GPA is acccepted
    print('\nInvalid GPA')
    while gpa > 4.0 or gpa < 0:
        gpa = float(input('Enter your Final highschool GPA (Weigthed): '))
  elif gpa <= 4.0 and gpa >= 0:
    print('\nGPA Accepted')
    pass
  if sat > 1600 or sat < 0: #If SAT is greater than 1600 and less than 0, ask user to re-enter SAT until valid GPA is acccepted
    print('\nInvalid SAT score')
    while sat > 1600 or sat < 0:
      sat = int(input('Enter your SAT score: '))
  elif sat <= 1600:
    print('\nSAT score Accepted')
    pass
  if area not in l.locations: #If location is not within the locations list, ask user to re-enter location until valid location is acccepted
    print('Invalid location of study. Please try again. Here are the list of college locations to choose from:')
    for i in l.locations:
      print(i, end=' \n')
    while area not in l.locations:
      area = str(input('Enter your desired location of study: '))
  elif area in l.locations:
    print('\nArea location Accepted')
    pass
  return gpa, sat, area #return gpa, sat, and area to main function



#Function to fetch college based on user input in desired area of study

def fetch_college(area, gpa, sat):
  global choices
  choices = []
  if area == 'Austin': #if user selects Austin, fetch Austin colleges
    for i in l.austin:
      choices.append(i)
  elif area == 'Houston': #if user selects Houston, fetch Houston colleges
    for i in l.houston:
      choices.append(i)
  elif area == 'Dallas' or area == 'Fort Worth': #if user selects Dallas or Fort Worth, fetch Dallas/Fort Worth colleges
    for i in l.dallas_fort:
      choices.append(i)
  elif area == 'Destin': #if user selects Destin, fetch Destin colleges
    for i in l.destin:
      choices.append(i)
  elif area == 'San Antonio': #if user selects San Antonio, fetch San Antonio colleges
    for i in l.san_antonio:
      choices.append(i)
  elif area == 'Corpus Christi': #if user selects Corpus Christi, fetch Corpus Christi colleges
    for i in l.corpus_christi:
      choices.append(i)
  elif area == 'Waco' or area == 'Kileen': #if user selects Waco or Kileen, fetch Waco/Kileen colleges
    for i in l.waco_kileen:
      choices.append(i)

  print('\nHere are your availabile college choices in your selected area: ') #Presents available colleges for the user based on their input of location
  for choice in choices:
    print(choice['name'], end=' \n')
  college(gpa, sat) #starts the college selection process

def college(gpa, sat):
  ask = str(input('\nWould you like to base this college selection on GPA or SAT? (g/s): ')) #Asks if the user wants to base selection on gpa or sat
  if ask == 'g':
    print('These collleges would be the best for you based on your final high school GPA:\n')
    for x in choices: #for each college in the choices list, if the college's gpa is greater than the user's gpa, it will add the college to the list of colleges that the user would be able to attend temporarily
      if x['average_GPA'] < gpa or x['average_GPA'] == 0:
        name = x['name']
        location = x['location']
        score = x['SAT_range']
        point = x['average_GPA']
        print(f'\n{name} , {location}\nAdmissions \nExpected GPA: {point} \nExpected SAT score: {score}' , end=' \n')
        
      elif x['average_GPA'] < gpa:
        pass
        choices.remove(x)
        
  if ask == 's':
    print('These collleges would be the best for you based on your SAT score:\n')
    for x in choices: #for each college in the choices list, if the college's sat is greater than the user's sat, it will add the college to the list of colleges that the user would be able to attend temporarily
      if x['SAT_range'] < sat or x['SAT_range'] == 0:
        name = x['name']
        location = x['location']
        score = x['SAT_range']
        point = x['average_GPA']
        print(f'\n{name} , {location}\nAdmissions \nExpected GPA: {point} \nExpected SAT score: {score}' , end=' \n')

      elif x['SAT_range'] < sat:
        pass
        choices.remove(x)
