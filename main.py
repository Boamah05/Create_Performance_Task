import functions as f



game = True
while game == True:
  f.main()
  gpa, sat, area = f.ask()
  gpa, sat, area = f.verify(gpa, sat, area)
  f.fetch_college(area, gpa, sat)
  game = False
