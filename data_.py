from index import *

class Data:
  
  contas_linhas = list()
  contas_string = ''
  dados_de_comunicacao = ''
  acess_key = ''
  ip = ''
  porta = 0
  
  #contas: file
  usuario = []
  senha_cripto = []

  def __init__(self):
    pass  
    #Data.saida = createWriter('contas.txt')
    #Data.entrada = createReader('contas.txt')
  def RetornaStr(self,arquivo):
    linhas = list()
    linhas = loadStrings(arquivo)  
    return join(linhas,' ')
  def ImprimeContas(self):
    println('contas string: '+ Data().RetornaStr('contas.txt')) 
    for i in range(len(Data.usuario)):
        println(str(Data.usuario[i][1]))
        println(str(Data.senha_cripto[i][1]))
  def SalvaDadosDeComunicacao(self):
      import __main__
      #__main__.dados_de_comunicacao.println("Favor nao alterar esses dados manualmente, eles estao criptografados. Altere via software.")  
      #__main__.dados_de_comunicacao.println("acess_key = \""+str(Data.acess_key)+"\";")  
      #__main__.dados_de_comunicacao.println("versao = \"0.3\";")  
      #__main__.dados_de_comunicacao.println("ip = \""+str(Data.ip)+"\";")  
      #__main__.dados_de_comunicacao.println("porta = \""+str(Data.porta)+"\";") 
      #__main__.dados_de_comunicacao.flush()
      #__main__.dados_de_comunicacao.close()  
      linhas = []
      
      linhas.append("Favor nao alterar esses dados manualmente, eles estao criptografados. Altere via software.")
      linhas.append("acess_key = \""+str(Data.acess_key)+"\";")
      linhas.append("versao = \"0.3\";")
      linhas.append("ip = \""+str(Data.ip)+"\";")
      linhas.append("porta = \""+str(Data.porta)+"\";")
      linhas.append("Alterado via software em "+str(day())+"/"+str(month())+"/"+str(year())+".")
      print(linhas)
      saveStrings('/data/dados_de_comunicacao.txt',linhas)
  def ObtemDadosDeComunicacao(self):  
    Data.dados_de_comunicacao_string = Data().RetornaStr('dados_de_comunicacao.txt') 
    Data.acess_key = str(matchAll(Data.dados_de_comunicacao_string,'acess_key = \"(.*?)\";')[0][1])
    Data.ip = str(matchAll(Data.dados_de_comunicacao_string,'ip = \"(.*?)\";')[0][1])
    Data.porta = int(str(matchAll(Data.dados_de_comunicacao_string,'porta = \"(.*?)\";')[0][1])) 
  def ObtemContas(self):
    Data.contas_string = Data().RetornaStr('contas.txt')
    Data.usuario = matchAll(Data.contas_string,'usuario = \"(.*?)\";')
    Data.senha_cripto = matchAll(Data.contas_string,'senha_cripto = \"(.*?)\";')
  