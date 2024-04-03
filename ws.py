BLANK = "   "
class Q_Node:
  def __init__(self):
    self.BuyerID = BLANK
    self.WaitingTime = 0
    self.ItemsInBasket = 0

BuyerQ = [Q_Node() for i in range(30)]

print(len(BuyerQ))

BuyerQ.remove(BuyerQ[3])

print(len(BuyerQ))
