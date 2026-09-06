from main import Player
player2=Player('Neymar',30,'Paris Saint_Germain','Brazilian','True')
#print(hasattr(player2,'age'))
print(hasattr(player2,'Age'))
print(getattr(player2,'nationality'))
print(player2.__dict__)
print(player2.__module__)
