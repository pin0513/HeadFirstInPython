movies = ['The Holy Grail', 1975, "Terry Jones & Terry Gilliam", 91,    #電影名稱
          ["Graham Chapman",                                           #主角清單
          ["Michael Palin" , "John Cleese" , "Terry Gilliam" , "Eric Idle" , "Terry Jones"]]] #配角清單
#print(movies[4][1][3])

#print(movies)

for item in movies:
    if (isinstance(item, list)):
        for nested_item in item:
            if (isinstance(nested_item, list)):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(item)

print("================================================")

def PrintList(listData):
    for item in listData:
        if (isinstance(item, list)):
            PrintList(item)
        else:
            print(item)
pass

PrintList(movies)

try:
    print(str(1024/0))
except Exception as e:
    print("Error:{}".format(e))
pass


    




