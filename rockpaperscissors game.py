game = "y"

while game == "y":

  x = input ("Your choice")
  y= input ("Your choice 2")

  if x == y:
    print ("draw")
    game= input ("do you want to play another?")
 

  while x or y == "Rock":
    if x or y == "Scissors":
      print("Rock smashes scissors")
      game= input ("do you want to play another?")
      
  while x or y == "Scissors":
    if x or y == "Paper":
      print("scissors cuts paper!")
    elif x or y == "Rock":
      print ("Rock smashes scissors!")

  while x or y =="Paper":
    if x or y =="Scissors":
      print("Scissors cuts paper!")
    elif x or y == "Rock":
      print("Rock breks Scissors!")
