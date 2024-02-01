
import random
import os
import json


class Player:
    def __init__(self,id) -> None:
        self.id=id
        self.data=self.dataload()
        self.sx=self.player_init()

    def dataload(self):
        j={
            "gold":100,
            "win":0,
            "loss":0,
            "total":0
        }
        if not os.path.exists('data'):
            os.mkdir('data')

       
        filename = f'data/{self.id}.json'
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump(j, f, indent=4)
            return j
        else:
            with open(filename, 'r') as f:
                return json.load(f)
            
        
        
    def player_init(self):

        return{
            "hp":4,
            "pass":True,
            "res":{
                "1":0,
                "2":0,
                "3":0,
                "4":0,
                "5":0
            }
        }
    def save(self):
        if not os.path.exists('data'):
            os.mkdir('data')

            
        with open(f'data/{self.id}.json', 'w') as f:
            json.dump(self.data, f, indent=4)




class Game:

    def __init__(self,player1:Player,player2:Player) -> None:
        self.player1=Player(player1)
        self.player2=Player(player2)
        self.winer=None
        
    
    def game_init(self):
        
        self.generate_random_clip_init()
        self.ammo=random.choice([self.player1,self.player2])
        self.gone_atk=1
        for i in [random.randint(1, 5) for _ in range(3)]:
            self.player1.sx["res"][str(i)]+=1
        for i in [random.randint(1, 5) for _ in range(3)]:
            self.player2.sx["res"][str(i)]+=1



    def generate_random_clip_init(self):
        total_ammo = random.randint(1, 6)
        self.ammo_list = [0]+[random.randint(0, 1) for _ in range(total_ammo)]+[1]

        random.shuffle(self.ammo_list)

        self.true_ammo = self.ammo_list.count(1)
        self.false_ammo = self.ammo_list.count(0)
        
        return self.true_ammo, self.false_ammo
    
    def shoot(self,gj,bgj):
        
        t=self.ammo_list.pop()
        if t:
            if gj.id==bgj.id:
                bgj.sx["hp"]-=self.gone_atk
                self.ammo=self.rival()
                return 0,self.gone_atk
            else:
                bgj.sx["hp"]-=self.gone_atk
                
                self.ammo=self.rival()
                
                return 1,self.gone_atk
            
        else:
            if gj.id==bgj.id:
                self.ammo=gj
                return 2,0
            else:
                self.ammo=self.rival()
                return 3,0
                
    def get_res(self):
        j={}
        for i in range(3):
            r=str(random.choice([5,3,2,4,1]))
            self.player1.sx["res"][r]+=1
            if j.get(self.player1.id):
                j[self.player1.id].append(r)
            else:
                j[self.player1.id]=[r]
        for i in range(3):
            r=str(random.choice([5,1,4,3,2]))
            self.player2.sx["res"][r]+=1
            if j.get(self.player2.id):
                j[self.player2.id].append(r)
            else:
                j[self.player2.id]=[r]
        return j
            
    def rival(self)->Player:
        return self.player2 if self.ammo.id==self.player1.id else self.player1
