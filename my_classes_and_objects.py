class Bird:
  age=3
  def __init__(self, type, food, color, weight):
    self.color=color
    self.type=type
    self.food=food
    self.weight=weight
    self.sold=False

  def sell(self,price):
    self.sold=True
    print("Sold for £____:",price)


birds1=Bird("green","lovebirds","fruits","40g")
print(birds1.age)
print(birds1.color)
print(birds1.type)
print(birds1.food)
print(birds1.weight)
print(birds1.sold)
birds1.sell(170)
print(birds1.sold)


birds2=Bird("blue","peacock","berries","2.7kg")
print(birds2.age)
print(birds2.color)
print(birds2.type)
print(birds2.food)
print(birds1.weight)
print(birds2.sold)

birds1=Bird("brown","eagles","fish","3.6g")
print(birds1.age)
print(birds1.color)
print(birds1.type)
print(birds1.food)
print(birds1.weight)
print(birds1.sold)
birds1.sell(1500)
print(birds1.sold)

