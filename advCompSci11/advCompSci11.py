import pandas as pd
import random
import math

df_new = pd.read_csv(r"C:\Users\ander\OneDrive\Desktop\New folder\advCompSci11\Test Data.csv")
df_old = pd.read_csv(r"C:\Users\ander\OneDrive\Desktop\New folder\advCompSci11\Updated Lakers Spreadsheet - Games.csv")
df_new = df_new.rename(columns={
   'Opposing Def Rtg': 'defensive',
   'Opposing Off Rtg': 'offensive',
   'W/L': 'W/L'})
df_old = df_old.rename(columns={
   'Defensive': 'defensive',
   'Offensive': 'offensive',
   'W/L': 'W/L'})



df_new = df_new[['defensive', 'offensive', 'W/L']]
df_old = df_old[['defensive', 'offensive', 'W/L']]

print(df_new.to_string,df_old.to_string)

end_result = []

def find_distance(x, y, x1, y1):
   return ((x - x1)**2 + (y - y1)**2)**(1/2)

def find_likelihood(df_old, new_game):
   possible_wins = []
   win_likelihood = 0
   loss_likelihood = 0
   won_games = 0
   lost_games = 0      

   for i in range(0, len(df_old),1):
      new_game_x = new_game[0]
      new_game_y = new_game[1]
      dist_val = find_distance(new_game_x, new_game_y, float(df_old['defensive'][i]), float(df_old['offensive'][i]))
      
      if dist_val <= 2.5:
         possible_wins.append((float(df_old['defensive'][i]), float(df_old['offensive'][i]), df_old['W/L'][i],dist_val))

   for i in possible_wins:
      if i[2] == "L":
         lost_games += 1
         loss_likelihood += 1/i[3]
      else:
         won_games += 1
         win_likelihood += 1/i[3]
   
   print("Possible win: ", possible_wins)    
   print("Win likelihood: ", win_likelihood, "won games:", won_games, "Loss likelihood: ", loss_likelihood, "lost games:", lost_games)
   print("New game: ", new_game)  
   
   if win_likelihood > loss_likelihood:
      return f"Win {win_likelihood*100/(win_likelihood + loss_likelihood)}%"
   elif win_likelihood == loss_likelihood:
      return random.choice(["Win 50%", "Loss 50%"])
   else:
      return f"Loss {loss_likelihood*100/(win_likelihood + loss_likelihood)}%"

"""data = {
   'defensive' : [-0.9, 1.3, -0.4, 4.4, -2.2, 2.2, -1.7, -1.7, 2.2, -8.2, -4.7, -0.9, 0.8, 2, -1.2, -1.1, -5.3, -2.9, -8.3, 5.6],
   'offensive' : [-2.9, 2.5, -3, -3.8, 1.8, 0.2, -0.8, -1.5, 0.2, -3.9, 2.9, -2.9, -5, -1, 0.3, -1.6, 2.6, -6, 5.8, -3.5],
   'win/loss' : ["L", "W", "L", "W", "W", "W", "L", "W", "W", "L", "W", "W", "L", "L", "L", "W", "W", "L", "W", "W"]

}

df = pd.DataFrame(data)  
   
   frontier.append(possible_wins[0])
   for i in possible_wins:
      if find_distance(new_game[0],new_game[1],frontier[0][0], frontier[0][1]) >= find_distance(new_game[0],new_game[1], i[0], i[1]):
         frontier.clear()
         frontier.append(i)
         closest_win = i
         

   

   if closest_win[0] - new_game[0] and closest_win[1] - new_game[1] <= closest_loss[0] - new_game[0] and closest_loss[1] - new_game[1]: 
      return "Win"
   else:
      return "Loss"""
for i in range(1,len(df_new)):
   new_game = (df_new['defensive'][i], df_new['offensive'][i])
   end_result.append(f"{find_likelihood(df_old, new_game)} game ({i})")
   print(find_likelihood(df_old, new_game))

print(end_result)

"""
game_result = [(defensive, offensive)]
possible_wins = []
possible_losses = []
win_likelihood = 0
loss_likelihood = 0
new_game = (0, 0)

def find_distance(x, y, x1, y1):
   return ((x - y)**2 + (x1 - y1)**2)**(1/2)
 

for i in range(1, len(defensive)):
   selected = 0
   if find_distance(defensive[selected], offensive[selected], defensive[i], offensive[i]) <= 2:
      possible_wins.append((defensive[selected], offensive[selected]))
      selected += 1
   else:-
      possible_losses.append((defensive[selected], offensive[selected]))
      selected += 1

for i in possible_wins:
   if find_distance(new_game[0], new_game[1], i[0], i[1]):
      
   """