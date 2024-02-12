"""
This program will manipulate the images given in HW4. 
Author: Daniel Aleksyevich Oukolov
""" 
from csc121.image import get_channel, write_jpg

def gradient_blend():
  ric_red = get_channel('rick.jpg','red')
  ric_green = get_channel('rick.jpg', 'green')
  ric_blue = get_channel('rick.jpg', 'blue')

  ils_red = get_channel('ilsa.jpg', 'red')
  ils_blue = get_channel('ilsa.jpg', 'blue')
  ils_green = get_channel('ilsa.jpg', 'green')
  

  height = len(ils_red)
  width = len(ils_red[0])


  for i in range(height):
    for j in range(width):
      x = i/height 
      y = j/width
      z = (max(x,y))
      

      ric_green[i][j] = int((z * ric_green[i][j] + (1 - z) * ils_green[i][j]))

      ric_red[i][j] = int((z * ric_red[i][j] + (1 - z) * ils_red[i][j]))

      ric_blue[i][j] = int((z * ric_blue[i][j] + (1 - z) * ils_blue[i][j]))
  write_jpg(ric_red, ric_green, ric_blue, 'blended.jpg')

def mirror():
  """
  This function produces a mirror image of the original picture
  """
  file = input("Enter the name of the file: ")
  red = get_channel(file, 'red')
  green = get_channel(file, 'green')
  blue = get_channel(file, 'blue')

  height = len(red)
  width = len(red[0])

  cent = width//2

  for j in range(height):
    for i in range(cent):
      red[j][-i-1] = red[j][i]
      green[j][-i-1] = green[j][i]
      blue[j][-i-1] = blue[j][i]
 
  write_jpg(red, green, blue, 'mirrored.jpg')
  
def pencil_sketch():
  """
  This function creates a picture that looks like if it was sketched with a pencil
  """
  file = input("Enter the name of the file: ")

  red = get_channel(file, 'red')
  green = get_channel(file, 'green')
  blue = get_channel(file, 'blue')

  height = len(red)
  width = len(red[0])
 
  gray = 0

  sum_one = 0
  sum_two = 0

  for j in range(height-1):
    for i in range(width-1):
      gray_one = (red[j][i] + green[j][i] + blue[j][i]) // 3
      gray_two = (red[j][i+1] + green[j][i+1] + blue[j][i+1]) // 3

      gray_three = (red[j+1][i] + green[j+1][i] + blue[j+1][i]) // 3

      sum_one = abs(gray_one - gray_two)
      sum_two = abs(gray_one - gray_three)
 
      if (sum_one > 8) and (sum_two > 8):
        red[j][i] = 0
        green[j][i] = 0
        blue[j][i] = 0
      else:
        red[j][i] = 255
        green[j][i] = 255
        blue[j][i] = 255

  write_jpg(red, green, blue, 'sketched.jpg')
