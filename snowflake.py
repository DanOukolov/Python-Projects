"""
This program is a series of functions designed to recurseively delete characters in a string, countdown and back up, and draw a snowflake. 

Author: Daniel Aleksyevich Oukolov
"""

def recursive_delete(string,character):
  """
  This program will recursively delete the character that is in a string. 

Parameters - 
  string - the string that we wish to delete some of the characters in 

  character -- 
  this parameter is technically a string so we can delete multiple consecutive characters if we wish 

returns:
string that has the desired character deleted
  """
  if len(string) == 0:
    return ""
  if string[0] == character:
    rest = string[1:]
    return recursive_delete(rest, character)
  rest = string[1:]
  return (string[0]+recursive_delete(rest, character))
  
  
def double_countdown(n):
  """
  This program is designed to countdown from a number and then back up again.

parameters: 
  n = number where we countdown from and back up to

return: 
  string that has n counted down and back up from 0. 
  """
  string = ''
  if n <1: 
    string = "0"
    return string
  string += str(n)
  space = " "
  string += space + double_countdown(n-1) + space + str(n)
  return string
  
  
def draw_koch_snowflake(length, level):
  """
  This program will draw a koch snowflake using turtle graphics.  

Parameters - 
  length - the length of the split sides of the snow flake 

  level -- 
  the level of intricacy that the snowflake will resemble. IE how many flakes that each side will feature. 
  """
  TURTLE_HARD = 120
  SNOWBASE = 3
  
  import turtle 
  
  if level <1:
    return 
  else: 
    for i in range(SNOWBASE):
      draw_flakes(length, level)
      turtle.left(TURTLE_HARD)
      
def draw_flakes(length, level):
  """
  This program will draw the side flakes of the snowflake.

  Parameters - 

  length - 
  this length is just the original parameter but here in the flake drawing process, we divide it by 3 everytime so that the sides get smaller and smaller as the recursion progresses. 

  level - 
  Again this is the additional intricacies of the flakes. Here we reduce it by 1 everytime as we continue through the regression. 
  """
  TURTLE_HARD = 120
  TURTLE_SOFT = 60
  
  import turtle
  if level <2:
    turtle.back(length)
    return 


    
  else: 
    
    draw_flakes(length/3, level-1)
    turtle.right(TURTLE_SOFT)
    draw_flakes(length/3, level -1)
    turtle.left(TURTLE_HARD)
    draw_flakes(length/3, level -1)
    turtle.right(TURTLE_SOFT)
    draw_flakes(length/3, level -1)
    return  
