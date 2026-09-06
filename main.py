class Player:
    def __init__(self,name,age,team,nationality,injured):
        self.name=name
        self.age=age
        self.team=team
        self.nationality=nationality
        self.injured=injured
    def get_health_status(self):
        print(self.name+'\nInjured:'+str(self.injured))
        return
    def get_information(self):
        print('Name:',self.name,'\nAge:',self.age,'\nTeam:',self.team,'\nNation:',self.nationality)
        return
    def age_at(self,year):
        x=self.age-(2025-year)
        if x<0:
            print('This player was not born yet this year.')
        elif x==0:
            print('This player was born in this year.')
        else:
            print(x)
        return