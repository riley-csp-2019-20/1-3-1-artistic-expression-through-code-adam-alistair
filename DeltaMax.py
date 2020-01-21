import turtle
import time
import random
#name = {"ATTACK","DEFENSE","SPEED","HEALTH","TURTLE"}
sprites = {"Bob":"playerstanding.gif","Billy":"playerstanding.gif","John":"enemystanding.gif","Joey":"enemystanding.gif"}
Bob = {"Name":"Bob","ATK":10,"DEF":6,"SP":7,"HP":100,"TRTL":turtle.Turtle()}
Billy = {"Name":"Billy","ATK":10,"DEF":6,"SP":7,"HP":100,"TRTL":turtle.Turtle()}
John = {"Name":"John","ATK":1,"DEF":8,"SP":5,"HP":100,"TRTL":turtle.Turtle()}
Joey = {"Name":"Joey","ATK":1,"DEF":8,"SP":5,"HP":100,"TRTL":turtle.Turtle()}

wn = turtle.Screen()

all_characters = [Bob, Billy, John, Joey]
player_team = [Bob, Billy]
enemy_team = [John, Joey]

for people in all_characters:
  wn.addshape(sprites[people["Name"]])

for b in all_characters:
  b["TRTL"].pu()
  b["TRTL"].speed(0)
  b["TRTL"].shape(sprites[str(b["Name"])])


Bob["TRTL"].goto( -200,-150)
John["TRTL"].goto(200,-150)
Joey["TRTL"].goto(200, 150)
Billy["TRTL"].goto(-200, 150)

for a in enemy_team:
  a["TRTL"].setheading(180)
  a["TRTL"].speed(2)
for b in player_team:
  b["TRTL"].speed(3)

base_damage = 20
choice = "blank"

def damage_calc(damage,attacker,defender): #used to register an attack
  print("\n" + attacker["Name"] + " attacks " + defender["Name"] + "!")
  if attacker["HP"] == 0:
    print(attacker["Name"] + " is dead.")
  #Calculates speed percentage
  percent = round((attacker["SP"]/defender["SP"])*100)
  if percent > 95:
    percent = 95
  elif percent < 20:
    percent = 20
  print(str(percent) + "% to hit")
  if random.randint(0,100) < percent: #Runs percent check
    attack_animation(attacker["TRTL"],defender["TRTL"])# activates attack animation

    #Calculates damage
    if(attacker["ATK"]<defender["DEF"]): #Applies a debuff if defender has a higher defense than attackers attack
      damage = damage-((damage*defender["DEF"])/100)

    damage = damage+(damage*attacker["ATK"])/100 #Applies attack buff

    if((defender["HP"]-damage) < 0): #checks to see if enemy is dead
      defender["HP"] = 0 #Add victory check
      defender["TRTL"].ht()
      print(defender["Name"] + " is dead.")
    else: #Applies damage
      defender["HP"] = defender["HP"]-round(damage)
    #print(damage)
  else:
    print("miss")
  print("\n")
  for p in all_characters:
    print(p["Name"]+ " "+str(p["HP"]))

def enemyai(): #used to decide the enemy's action
  enemy_choice = random.randint(1,4)
  time.sleep(1)
  if enemy_choice == 1:
    damage_calc(base_damage,enemy_team[0],player_team[0])
  elif enemy_choice == 2:
    damage_calc(base_damage,enemy_team[0],player_team[1])
  elif enemy_choice == 3:
    damage_calc(base_damage,enemy_team[1],player_team[0])
  elif enemy_choice == 4:
    damage_calc(base_damage,enemy_team[1],player_team[1])
  else:
    print("The enemy waits")

def attack_animation(attacker,defender): #function to run attack animation
  oldxcor = attacker.xcor()
  oldycor = attacker.ycor()
  if defender.xcor() >0:
    attacker.goto((defender.xcor()-15),defender.ycor())
  elif defender.xcor() == 0:
    if defender.ycor() >0:
      attacker.goto(defender.xcor(),defender.ycor()-15)
    else:
      attacker.goto(defender.xcor(),defender.ycor()+15)
  else:
    attacker.goto((defender.xcor()+15),defender.ycor())
  defender.backward(5)
  time.sleep(.3)
  defender.forward(5)
  attacker.goto(oldxcor,oldycor)

print("You encounter " + enemy_team[0]["Name"] + ", destroyer of worlds!")

while ((Bob["HP"] > 0) or (Billy["HP"] > 0)) and ((John["HP"] > 0) or (Joey["HP"] > 0)): #keeps battle running if both players are alive
  choice = "blank"
  choice = input("Choose your action.\n (Type ATK or RUN)")
  if choice == "ATK":
      attacker_choice = int(input("Which charactor do you want to be the attacker?(1 for " + player_team[0]["Name"] + ", 2 for " + player_team[1]["Name"] + ")"))
      if (attacker_choice <= len(player_team)) and (attacker_choice >=1):
        defender_choice = int(input("Which charactor is going to be attacked?(1 for " + enemy_team[0]["Name"] + ", 2 for " + enemy_team[1]["Name"] + ")"))
        if (defender_choice <= len(enemy_team)) and (defender_choice >=1):
          attacker_choice -=1
          defender_choice -=1
          damage_calc(base_damage,player_team[attacker_choice],enemy_team[defender_choice])
        else:
          print("That number isn't an option")
      else:
        print("That number isn't an option")
      
  elif choice == "RUN":
      print("You are a weakling")
      break
  else:
    print("READ THE COMMANDS!!!")
  enemyai()
  #print( "\n" + Bob["Name"]+ " "+str(Bob["HP"]))
  #print(John["Name"]+ " "+str(John["HP"]))
  print("------------Next Turn!------------")
print("------------GAME OVER!------------")
wn.bye()