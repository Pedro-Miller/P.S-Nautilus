import pandas as pd #importa a biblioteca do pandas para fazer as tabelas
indice = ["thrusters", "sensores", "ano de criação", "numero de cameras"]



class AUV: #cria a classe dos AUVs com os atributos: nome, numero de thrusters e cameras, e lista de sensores
    def __init__(self, nome:str, thrusters: int, sensores: list, ano:int, n_cams:int):
        self.nome = nome
        self.thrusters = thrusters
        self.sensores = sensores
        self.ano = ano
        self.numero_cameras = n_cams

    #cria dois getters, um para o ano e outro para o numero de cameras
    def get_ano(self):
        return self.ano
    
    def get_cams(self):
        return self.numero_cameras
    
    #permite que o nome dos AUVs seja printado como string, e não como referência de memória
    def __repr__(self): 
        return "%s" % (self.nome)

#cria a classe com as funções de exibição dos AUVs
class descritor:
    def __init__(self):
        pass

#método que rankeia do mais novo para o mais velho
    def ranking(self, auvs:list):
        rank= sorted(auvs, key= AUV.get_ano, reverse=True)
        print("Os AUVs do mais novo para o mais antigo são:", rank)

#método que permite escolher apenas um AUV para ser exibido individualmente
    def mostra_um(self):
        aux = input("Qual AUV você deseja ver? \n")
        auv_escolhido = aux.upper()

        if auv_escolhido == 'LUA':
            nome = ["Lua"]
            atributos = [Lua.thrusters, Lua.sensores, Lua.ano, Lua.numero_cameras] 
            mostrou= pd.DataFrame(atributos, columns= nome, index= indice)
            print(mostrou)

        elif auv_escolhido == 'BRHUE':
            nome = ["BrHUE"]
            atributos = [BrHUE.thrusters, BrHUE.sensores, BrHUE.ano, BrHUE.numero_cameras]
            mostrou= pd.DataFrame(atributos, columns= nome, index= indice)
            
            print(mostrou)
        else:
            print("O nome digitado não existe")
    

#método que exibe todos os AUVs juntos em tabela
    def mostra_todos(self):
        atributos = [[BrHUE.thrusters, Lua.thrusters],
            [BrHUE.sensores, Lua.sensores],
            [BrHUE.ano, Lua.ano],[BrHUE.numero_cameras,Lua.numero_cameras]]
        df = pd.DataFrame(atributos, columns=['BrHUE', 'Lua'], index= ["thrusters","sensores", "ano de criação","numero de cameras"])
        print(df)

#método que ordena os AUVs daquele com maior numero de cameras até o menor
    def decrescente_cams(self, auvs:list):
        decres= sorted(auvs, key= AUV.get_cams, reverse=True)
        print("Os AUVs com mais cameras até os com menos são:", decres)


        
#criando os objetos com as informações dos papers          
BrHUE = AUV(nome='BrHUE', thrusters= 6, sensores= ['sensor de pressão e profundidade'], ano=2020, n_cams= 3)
Lua = AUV(nome='LUA', thrusters= 8, sensores= ['BAR30: Sensor de pressão externa', 'BMP180: Sensor de pressão inerna', "Sensor de vazamento"], ano=2022, n_cams= 4)

auvs = [BrHUE, Lua]

manager = descritor()

#mostra todos os AUVs em tabela
#manager.mostra_todos()

#escolhe um para mostrar individualmente
#manager.mostra_um() 

#rankeia do mais novo ao mais antigo
#manager.ranking(auvs)

#livre escolha: rankeia do com mais cameras ate o com menos
#manager.decrescente_cams(auvs)



