class HalvingGame(object):
  def __init__(self, N):
    self.N = N

# State = (player,number)
  def Startstate(self):
    return(+1,self.N)

  def isEnd(self,state):
    player,number=state
    return number==0

  def utility(self,state):
    player,number=state
    assert number==0
    return player *float('inf')

  def actions(self,state):
    return['-', '/']

  def player(self,state):
    player,number=state
    return player

  def succ(self,state,actions):
    player,number=state
    if actions=='-':
      return (-player,number-1)
    else:
      return (-player,number//2)

  # Define humanpolicy as a method within the HalvingGame class
  def humanpolicy(self, game, state):
    while True:
      action=input('Your action:')
      if action in game.actions(state):
        return action

# Instantiate the HalvingGame class
game=HalvingGame(N=15)

# Access humanpolicy through the game object
policies={+1:game.humanpolicy, -1:game.humanpolicy}
state=game.Startstate()

while not game.isEnd(state):
  print('='*10, state)
  player=game.player(state)
  policy=policies[player]
  action=policy(game,state)
  state=game.succ(state,action)

print('utility={}'.format(game.utility(state)))