class AUV:
    def __init__(self, nome:str, thrusters: int, sensores: list, ano:int):
        self.nome = nome
        self.thrusters = thrusters
        self.sensores = sensores
        self.ano = ano
        
    def get_ano(self):
        return self.ano
    
    def __repr__(self): 
        return "%s" % (self.nome)
    
class descritor:
    def __init__(self):
        pass

    def ranking(self, auvs:list):
        rank= sorted(auvs, key= AUV.get_ano, reverse=True)
        print("Os AUVs do mais novo para o mais antigo são:", rank)
           
BrHUE = AUV(nome='BrHUE', thrusters= 4, sensores= ['temperatura', 'pressão'], ano=2018)
Lua = AUV(nome='LUA', thrusters= 6, sensores= ['temperatura', 'pressão'], ano=2020)

auvs = [BrHUE, Lua]

manager = descritor()
manager.ranking(auvs)
