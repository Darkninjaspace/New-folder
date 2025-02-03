"""
Answer:
1. A E
2. B F
3. C D G

1. A B C
2. B D E
3. C E F
4. E F G

def backtrack (assigment,csp):
   if assigment complete:
      return Assignment
   var = SELECTUNASSIGNEDVARIABLE(Assignment,csp)
   for value in DOMAINVALUES:
      if value consistent with Assignment:
         add var = value to Assignment
         result = backtrack(Assignment, csp)
         if result != failure:
            return result
            remove(var = value from Assignment)
   return failure

"""
variables = ["A", "B", "C", "D", "E", "F", "G"]
days = ["Monday","Tuesday","Wednesday"]

Assignment = {}
Assignment["A"] = "unassigned"
Assignment["B"] = "unassigned"
Assignment["C"] = "unassigned"
Assignment["D"] = "unassigned"
Assignment["E"] = "unassigned"
Assignment["F"] = "unassigned"
Assignment["G"] = "unassigned"
csp = [("A","B"),("A","C"),("B","C"),("B","D"),("B","E"),("D","E"),("C","E"),("C","F"),("E","F"),("E","G"),("F","G")]

def backtrack(Assignment,csp):
   flag = True
   for blah in Assignment:
      if Assignment[blah] == "unassigned": #if assignment has no unassigned variable change to have no result and seperate assignment (done)        
         flag = False
   if flag == True:
      print(Assignment)
      return Assignment

   unassigned_var = select_unassigned_var(Assignment)
   
   for value in days:
      if consistent (value, csp, unassigned_var) == True: #this STILL dont make no sense 
         Assignment[unassigned_var] = value
         (Assignment[unassigned_var],"what")
         result = backtrack(Assignment,csp)
         if result != None:
            return result
   return None

def select_unassigned_var (Assignment):
   for var in Assignment:
      if Assignment[var] == "unassigned":
         return var

def consistent (value, csp, unassigned_var):
   for i in csp:
      if (unassigned_var) in i:
         if Assignment[i[0]] == value:
            return False
   return True

backtrack(Assignment,csp,)
