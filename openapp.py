import os

print("Enter 1 to open notepad")
print("Enter 2 to open windows media player")
print("Enter 3 to open google chrome")

inp=int(input("Enter final choice")

if inp==1:
  os.system('notepad')

if inp==2:
  os.system('wmplayer')

if inp==3:
  os.system('chrome')

else:
  print("choose from the given choices")
