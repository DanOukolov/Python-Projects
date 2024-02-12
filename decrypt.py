"""
This program is designed to break the caesar's cipher with some cool coding stuff.

Author: Daniel Alekseyevich Oukolov


"""
def crack_cipher(filename):

  """
This function will crack the caesar's cipher with ease


Parameters
file name -- name of the file 


Returns: 
final_answer which is the correct decrypted version of the text

  """
  cipher = []
  try: 
    with open(filename,"r") as input_file: 
      text = input_file.read()
      for ch in text:
        cipher.append(ord(ch))     
  except IOError: 
    print("Sorry bro, no file found.")
    return []
  final_answer = shift_function(cipher)
  return final_answer


  
def score(frequencies):

  """
This function will score each list of freqeuncies for each shift.

Parameters: 
Freqeuncies - the list of frequencies for each a subsequent shift


Returns:
score -- the score of how different each list is from the english language averages
  """ 

  score = 0
  alphabet = 26
  english = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.09, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.06]
  for i in range(alphabet):
    diff = 0 
    diff = (frequencies[i]-english[i])
    diff = abs(diff)
    score += diff

  return score
  
def shift_function(cipher):

  """

  Simple: This function will take the cipher and spit out the final decoded text. 

  Complicated explanation:
  This function bascially iterates through each of the varied lists, and then calls on some of the other functions to find each frequency those lists produce. Based on these frequencies, it will then score the difference and find the index of the list with the lowest difference to the english language. 

  Parameters -- 
  cipher - list of unicode numbers based on the letters of the original cipher 


  Returns -- 
  final_answer - the decoded text

  Note: This code does employ some helper functions

  """
 
  shifted_cipher =[]
  alphabet = 26
  a_unicode = 97
  z_unicode = 122
  transpose = []
  list_scores = []

  for shift in range(0,alphabet):
    shifted_cipher =[]
    for unicode_position in range(len(cipher)):
      if a_unicode > cipher[unicode_position]:
        new_ch = cipher[unicode_position]
      else: new_ch = cipher[unicode_position]
      if a_unicode<=cipher[unicode_position]<=z_unicode:
        new_ch = cipher[unicode_position]+ shift + 1
      else: 
        new_ch = cipher[unicode_position]
      if  new_ch > z_unicode:
          new_ch = new_ch - z_unicode + 96
          shifted_cipher.append(new_ch)
      else: 
        shifted_cipher.append(new_ch)


        
    transpose.append(shifted_cipher)
    frequencies = frequency(shifted_cipher)
    list_scores.append(score(frequencies))
    mini = min(list_scores)
    
  best_index = list_scores.index(mini)

  best_list = transpose[best_index]
  cracked_cipher = []
  cracked_cipher_string = ''
  for i in range(len(best_list)):
    best_list[i]= chr(best_list[i])
    cracked_cipher.append(best_list[i])

    
  for i in best_list:
    cracked_cipher_string += i

  final_answer = cracked_cipher_string
    
  return final_answer

  
def frequency(shifted_cipher):

  """
  This function will make a list of letter frequencies based on each shift.

  Parameters: 
  shifted_cipher - the cipher that has a certain shift

  returns: 
  frequency list - the specific frequency of each letter produced by that shift
  """

  
  alphabet = 26
  a_unicode = 97
  z_unicode = 122
  counting_list = [0]*26
  frequency_list = []
  
  for uni in shifted_cipher:
    if (a_unicode <= uni <= z_unicode):
      counting_list[uni-97] = counting_list[uni-97] + 1

  for x in range(alphabet):
    percentage = (counting_list[x]/len(shifted_cipher))
    percentage *= 100
    frequency_list.append(percentage)

  return frequency_list
