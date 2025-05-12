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
      return "W"
   #f"Win {win_likelihood*100/(win_likelihood + loss_likelihood)}%"
   elif win_likelihood == loss_likelihood:
      return random.choice(["L", "W"])
   else:
      return "L"
   #f"Loss {loss_likelihood*100/(win_likelihood + loss_likelihood)}%"

def find_accuracy(end_result, df_new):
   correct = 0
   incorrect = 0
   for i in range(0, len(end_result)):
      if end_result[i] == df_new['W/L'][i]:
         correct += 1
      else:
         incorrect += 1
   print("Correct: ", correct, "Incorrect: ", incorrect)
   return correct/(correct + incorrect)

for i in range(1,len(df_new)):
   new_game = (df_new['defensive'][i], df_new['offensive'][i])
   end_result.append(find_likelihood(df_old, new_game))
   print(find_likelihood(df_old, new_game))

print(find_accuracy(end_result, df_new))

