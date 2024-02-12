""" 
This program is coded to analyze the connotation a certain subject matter on twitter. 

In more depth: 
If the tweets have bad words, it will return a score that is negative. If the tweets about the subject are good overall, the function will return a positive valence score. 

Author: Daniel Alekseyevich Oukolov
"""
def analyze_tweets(query_term):
  """
  This function will give you a sentiment score based on the valence of the tweets about a certain subject.
  Parameters -- 
  query_term  - the subject/ search that the tweets are referring t 

  Return -
  the valence score of that subject = score/num_words
  """
  from csc121.twitter import get_tweets
  
  
  try: 
    with open("AFINN-111.txt","r") as input_file:
      affin = {}
      for line in input_file:
        fields = line.split() #["A","0","0"]
        affin[fields[0]] = (int(fields[-1]))
      tweets = get_tweets(query_term)
      if len(tweets["statuses"]) == 0:
        return 0
      score = 0 
      for i in range(len(tweets["statuses"])):
        tweet = tweets["statuses"][i]["text"].lower()
        tweet = tweet.split()
        score += score_tweet(tweet,affin)
          
      return (score/len(tweets["statuses"]))
  except IOError: 
    return 0


def score_tweet(tweet,affin):
  score = 0
  for i in range(len(tweet)):
    if tweet[i] not in affin:
      affin[tweet[i]] = 0
    if tweet[i] in affin:
      score += affin[tweet[i]]

  return score
    
    

  
    
        
        
      
      