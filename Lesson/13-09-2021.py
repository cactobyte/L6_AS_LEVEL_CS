while True:
  length = float(input())
  width = float(input())

  if(width > 4):
      print("The room size is too big")
  else:
      print("The cost of carpeting a {}x{} room is {} pounds".format(length,width,length*width*10))
