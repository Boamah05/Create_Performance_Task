import functions as f



game = True
while game == True:
  f.main()
  gpa, sat, area = f.ask()
  print('___________________________________________')
  gpa, sat, area = f.verify(gpa, sat, area)
  print('___________________________________________')
  f.fetch_college(area, gpa, sat)
  game = False
