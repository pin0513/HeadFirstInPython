import nester

#電影名稱
#主角清單
#配角清單

movies = ['The Holy Grail', 1975, "Terry Jones & Terry Gilliam", 91,    
          ["Graham Chapman",                                           
          ["Michael Palin" , "John Cleese" , "Terry Gilliam" , "Eric Idle" , "Terry Jones"]]]

#using Namespace
nester.print_lol(movies)

#Same as 
from nester import print_lol
print_lol(movies)