from main import Player
player1=Player('Lionel Messi',38,'Inter Miami','Argeninean','False')
#print(type(player1))
#print(player1.age)
#print(player1.name)
#print(player1.nationality)
#print(player1.team)
#print(player1.injured)
player1.get_information()
player1.get_health_status()
player1.age_at(1987)
player1.age=40
player1.team='Barcelona'
#del player1.age
player1.get_information()


