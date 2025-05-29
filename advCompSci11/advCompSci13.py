"""
Solution: give a set of data/sentences with both positive and negative ansewrs, intially randomly get to the answer yes or no
then compare final answer to the objective answer provided by us. adjust values of every word based on whether it matches or not
if yes then +1 to desire value for each word, or if no then -1 for each word. run through other data points/sentences and 
continue evaluating the desire value for each word and use the total desire value of a sentence to evalueate yes or no
"""

import random

data = []
question_log = []
scanned_words = []

def ask_question():
   print("input question:")
   input_question = input()
   if check_formating(input_question) == True:
      question_log.append(input_question)
      print("give answer: ")
      answer = input()
      while answer.lower() != "yes" and answer.lower() != "no":
         print("Please answer with yes or no.")
         answer = input()
      if answer.lower() == "yes":
         question_log.append("Y")
      elif answer.lower() == "no":
         question_log.append("N")
   return input_question

def check_formating(input_question):
   if input_question[-1] == "." or input_question[-1] == "," or input_question[-1] == "!" or input_question[-1] == "?":
      return True
   else:
      return False

def scan_question(input_question,scanned_words):
   word = ""
   if check_formating(input_question) == False:
      print("Please end your question with a punctuation mark.")
      return
   print("scanning question...")
   for i in input_question:
      if i != " " and i != "," and i != "." and i != "!" and i != "?":
         word = word + i
      else:
         if word not in scanned_words:
            data.append((word,0))
            scanned_words.append(word)
            print(data)
         word = ""
         continue

def evaluate_statements():
   moral_value = 0
   selected_sentence = 0
   decision = None
   for i in data:
      if i[0] in question_log[selected_sentence]:   
         if i[1] <= 1 and i[1] >= -1:
            print(data,"data")
            tuple_change = list(i)
            print(tuple_change)
            data.remove(i)
            tuple_change[1] += random.randint(-1,1)
            print(tuple_change)
            data.append(tuple(tuple_change))
            print(data,"data")
            moral_value += random.randint(-1,1)
         if i[1] > 1:
            i[1] += 1
            moral_value += 1
         if i[1] < -1:
            i[1] -= 1
            moral_value -= 1
   if moral_value > 0:
      decision = "yes"
   elif moral_value <= 0:
      decision = "no"
   if decision == "yes" and decision == question_log[selected_sentence + 1]:
      for i in data:
         if i[0] in question_log[selected_sentence]:
            i[1] += 2
   elif decision == "no" and decision == question_log[selected_sentence + 1]:
      for i in data:
         if i[0] in question_log[selected_sentence]:
            i[1] -= 2

def ask_final_question():
   print("ask final question:")
   input_question = input()
   if check_formating(input_question) == True:
      return input_question

def evaluate_final_question(input_question):
   moral_value = 0
   for i in data:
      if i[0] in input_question:
         if i[1] <= 1 and i[1] >= -1:
            moral_value += random.randint(-1,1)
         if i[1] > 1:
            moral_value += 1
         if i[1] < -1:
            moral_value -= 1
   if moral_value > 0:
      return "yes"
   else:
      return "no" 

def main ():
   final_answer = ""
   condition = True
   while condition:
      print("ask or stop")
      if input() == "ask":
         input_question = ask_question()
         scan_question(input_question, scanned_words)
         print("data: ", data)
         print("question log: ", question_log)
      else:
         evaluate_statements()
         print(data)
         
         input_question = ask_final_question()
         final_answer = evaluate_final_question(input_question)
         condition = False
   print("final answer: ", final_answer)
   return final_answer

main()