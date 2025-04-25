import pandas as pd

"""data = {
   'defensive' : [-0.9, 1.3, -0.4, 4.4, -2.2, 2.2, -1.7, -1.7, 2.2, -8.2, -4.7, -0.9, 0.8, 2, -1.2, -1.1, -5.3, -2.9, -8.3, 5.6],
   'offensive' : [-2.9, 2.5, -3, -3.8, 1.8, 0.2, -0.8, -1.5, 0.2, -3.9, 2.9, -2.9, -5, -1, 0.3, -1.6, 2.6, -6, 5.8, -3.5],
   'win/loss' : ["L", "W", "L", "W", "W", "W", "L", "W", "W", "L", "W", "W", "L", "L", "L", "W", "W", "L", "W", "W"]

}

df = pd.DataFrame(data)"""

df.read_csv("game_results.csv")

new_game = (0, 0)

def find_distance(x, y, x1, y1):
   return ((x - y)**2 + (x1 - y1)**2)**(1/2)

def find_likelihood(new_game, df):
   possible_wins = []
   win_likelihood = 0
   loss_likelihood = 0

   for i in range(1, len(df)):
      new_game_x = new_game[0]
      new_game_y = new_game[1]
      if find_distance(new_game_x,new_game_y, int(df['defensive'][i]), int(df['offensive'][i])) <= 2:
         possible_wins.append((int(df['defensive'][i]), int(df['offensive'][i]), df['win/loss'][i]))
         
   for i in possible_wins:
      if i[2] == "L":
         loss_likelihood += 1
      else:
         win_likelihood += 1
   
   print("Possible win: ", possible_wins)    
   print("Win likelihood: ", win_likelihood, "Loss likelihood: ", loss_likelihood)
   print("New game: ", new_game)  
   if win_likelihood > loss_likelihood:
      return "Win"
   else:
      return "Loss"


   """ 
         
   
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
   

print(find_likelihood(new_game, df))

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