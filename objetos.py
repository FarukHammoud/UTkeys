from index import *

class Projeto:
    def __init__(self):
        #variaveis do projeto
        self.nome = 'null_project'
        self.autor = ''
        self.data_de_criacao = 'dd/mm/aaaa'
        self.data_ultima_modificacao = 'dd/mm/aaaa'
        self.versao = 0
        self.sub_versao = 0
        self.variaveis = 0
        self.codigo = []
    
    #metodos de comunicacao do projeto
    def ImportaProjeto(self):
        pass
    def ExportaProjeto(self):
        pass    
    def MudaNome(self,nome):
        self.nome = nome
    def IncluiVariavel(self):
        pass
    
    #metodos de simulacao                
    #
class Papel:
    def __init__(self):
        self.x = width*3/10+5 
        self.y = 100   
    def MudaXY(self,x,y):
        self.x = x
        self.y = y    
    def Mostrar(self):
        fill(Cores().branco)
        stroke(Cores().cinza)
        strokeWeight(1)
        rect(width*3/10+10,self.y,width*7/8-width*3/10-20,height)
        stroke(Cores().cinza_claro)
        line(width*3/10+40,self.y,width*3/10+40,height)
        i = self.y+25
        while i < height:
            line(width*3/10+10,i,width*7/8-10,i)
            i+=25 
                