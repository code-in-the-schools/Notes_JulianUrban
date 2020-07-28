#function: block of code that performs an operation when called in code
#function can have arguments passed into it

class TestObject:
  x = 1
  y = 2
  z = 4

  def doMyMath(x, y, z):
   TestObject.x = x + y / z
   return x

print(TestObject.y)

class Book:
  numberOfPages = 0
  title = ""
  author = ""
  editor = ""
  illustrator = ""
  fiction = False

shelf = []
for r in range(3):
  b = Book
  b.numberOfPages = int(input("Number of pages? "))
  b.title = str(input("Name of book? "))
  b.author = str(input("Author? "))
  b.editor = str(input("Editor? "))
  b.illustrator = str(input("Illustrator? "))
  b.fiction = bool(input("Is it fiction? "))
  shelf.append(b)

for r in range(3):
  print(shelf[r].author)