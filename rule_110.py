"""
This program runs the math studied rule set named Rule 110
Author: Dan Oukolov 
"""

def run_rule_110(number_cells, step):
  """
  This is the main function that runs the rule 110. 
  
  Basically, this function is a series of if statements that will evaluate if the parameters fit the criteria I set up. Mainly, it adds spaces where needed based on number and step and seed index and this function then employs the helper functions in order to print the designed CA. 
  
  Parameters -- 
  number_cells -- the number of cells in the elementary CA
  step -- number of simulation steps to run 

  Returns -- 
  There are no values returned by the function itself... but it does use returned values that will be explained later. 
  """

  
 
  seed_index = 1
  while ((seed_index >= 0) and (seed_index <= number_cells)):
    seed_index = (int(input("Enter seed index: ")))
    world = []
    while (seed_index >= number_cells):
      print("Error: seed index out of bounds, please try again!")
      seed_index = int(input("Enter seed index: "))
    if (seed_index < 0):
      break
    for x in range(number_cells):
      if (x != seed_index):
        world.append(" ")
      else:
        world.append("$")
    for i in range(step+1):
      print_world(world)
      world = update_state(world)






def update_state(world):
  next_world = []
  for index in range(len(world)):
    next_world.append(get_cell_next_state(world, index))  
  return next_world
  """
  Update state(world): computes the next state of the whole CA by repeatedly calling get cell next state(world, index). It takes as input world which is a list of single space characters and $ symbols. The function returns a new list containing single space characters and $ symbols, denoting the next state of the CA.

  Parameters -- world
  World is a list that contains the spaces and dollar signs needed. 

  Returns -- This function returns a new list containing spaces and dollar signs which represents the next state of the CA 
  Next_world... this is the return value 
  """




def get_cell_next_state(world, index):  
  """
  Computes the next state of one CA cell according to Rule 110. It takes as input world which is a list of single space characters and $ symbols, and an integer index that is the index of the cell whose next state we wish to compute. The function returns either a single space character or the $ symbol, denoting the next state of world[index].

  Parameters -- 
  world - List of spaces and dollar signs needed to complete a line in CA 
  index -- index of the cell who's new state we wish to compute 

  """
  
  if ((world[index % len(world)] == "$") and (world[(index-1) % len(world)] == "$") and (world[(index+1) % len(world)] == " ")):

    return ("$")
  
  elif world[index] == " " and world[(index + 1) % len(world)] == "$" and world[(index-1) % len(world)] == "$":
   
    return ("$")

  elif world[index] == "$" and world[(index + 1) % len(world)] == "$" and world[(index-1) % len(world)] == " ":

    return ("$")
  
  elif world[index] == "$" and world[(index + 1) % len(world)] == " " and world[(index-1) % len(world)] == " ":
  
    return ("$")

  elif (world[index] == " " and world[(index+1)%len(world)] == "$" and world[(index-1) % len(world)] == " "):
    return ("$")
    
  else: 
  
    return (" ") 

def print_world(world):
  '''
  Prints out the current state of the CA to the screen. It takes as input a list named world containing single space characters and $ symbols, and returns no value.

  Parameters 
  world - list of dollars and spaces

  returns 
  NA 
  '''
  for i in range(len(world)):
    print(world[i], end='')
  print()
