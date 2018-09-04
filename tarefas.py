from index import *

class Tarefas:

  #Vetor Tarefa por Letra e Codigo
  tarefa_letra = []
  tarefa_codigo = []
  codigo = []
  indice_codigo = 0
  
  #Inicializacao
  def __init__(self):
    for i in range(512):
      Tarefas.tarefa_letra.append('')
      Tarefas.tarefa_codigo.append('')
      Tarefas.codigo.append('')
    
  #Funcao Tarefa
  def AlteraTarefaLetra(self,tarefa,letra): Tarefas.tarefa_letra[int(ord(letra))] = tarefa
  def AlteraTarefaCodigo(self,tarefa,codigo):
    Tarefas.tarefa_codigo[Tarefas.indice_codigo] = tarefa
    Tarefas.codigo[Tarefas.indice_codigo] = codigo
    Tarefas.indice_codigo+=1
  def Tarefa(self,tarefa):
    #print(tarefa)  
    if tarefa == '':
        pass
    if tarefa == 'Ativa Frame Animacao Inicial':
        Frames().AtivaFrame(0)
    if tarefa == 'Desativa Frame Animacao Inicial':
        Frames().DesativaFrame(0)
    if tarefa == 'Ativa Frame Cliente':
        Frames().AtivaFrame(1)
    if tarefa == 'Desativa Frame Cliente':
        Frames().DesativaFrame(1)
    if tarefa == 'Ativa Frame Servidor':
        Frames().AtivaFrame(2)
    if tarefa == 'Desativa Frame Servidor':
        Frames().DesativaFrame(2)
    if tarefa == 'Pula Inicio':
        Frames().DesativaFrame(0)
        Frames().AtivaFrame(1)
    if tarefa == 'Pula para Criador':
        Frames().DesativaFrames([0,1])
        Frames().AtivaFrames([2,3,4])
    if tarefa == 'Identifica QRcode':
        Interface().EspacoPressionado()    
    if tarefa == 'Estabelece Referencia':
        INTERFACE.x_ref = mouseX
        INTERFACE.y_ref = mouseY
    if tarefa == 'Calcula Arraste Mouse':
        INTERFACE.x_relativo += mouseX - INTERFACE.x_ref
        INTERFACE.y_relativo += mouseY - INTERFACE.y_ref
        INTERFACE.x_ref = mouseX
        INTERFACE.y_rea = mouseY 
    if tarefa == 'Processa Scroll Up':
        if Frames().MouseDentro(2):
            Interface().ScrollPlus(2)
        if Frames().MouseDentro(3):
            Interface().ScrollPlus(3)
        if Frames().MouseDentro(4):
            Interface().ScrollPlus(4)
    if tarefa == 'Processa Scroll Down':  
        if Frames().MouseDentro(2):
            Interface().ScrollMinus(2)
        if Frames().MouseDentro(3):
            Interface().ScrollMinus(3)
        if Frames().MouseDentro(4):
            Interface().ScrollMinus(4)
    if tarefa == 'Estado +=1':  
        Frames().frame_cliente.EstadoAdd()     
  def TarefaLetra(self,letra):
    Tarefas().Tarefa(Tarefas.tarefa_letra[ord(letra)])
  def TarefaCodigo(self,texto):
    for i in range(256):
      if Tarefas.codigo[i] == texto:
        Tarefas().Tarefa(Tarefas.tarefa_codigo[i])
        