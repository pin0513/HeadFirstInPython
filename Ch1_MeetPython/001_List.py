movies = ['''The Holy Grail''',
          """The Life of Brain""",
          "The Meaning of life",
          25]

print(movies[3])

movies.pop()

print(len(movies))

movies.insert(2, 24)

print(movies)

movies.extend(["This is Apple", 23, ["This is Book", 23.5]])

print(movies)