from index import *

class Interface:
    
  tempo_ultima_tecla = 0  
  tmp_text = ''
  scroll_f2 = 0
  pedidos_scroll_f2 = []
  scroll_f3 = 0
  pedidos_scroll_f3 = []
  scroll_f4 = 0
  pedidos_scroll_f4 = []
  valor_setas = 0
  
  x_ref = 0
  y_ref = 0
  x_relativo = 0
  y_relativo = 0

  mouse_clicked = False
  espaco_pressionado = False

  def ScrollPlus(self,x): 
     if x == 2:Interface.pedidos_scroll_f2.append([1,millis()])
     elif x == 3:Interface.pedidos_scroll_f3.append([1,millis()])
     elif x == 4:Interface.pedidos_scroll_f4.append([1,millis()])
  def ScrollMinus(self,x): 
     if x == 2:Interface.pedidos_scroll_f2.append([-1,millis()])
     elif x == 3:Interface.pedidos_scroll_f3.append([-1,millis()])
     elif x == 4:Interface.pedidos_scroll_f4.append([-1,millis()])
  def MudaTempoUltimaTecla(self):
        Interface.tempo_ultima_tecla = millis()   
  def RetornaTempoUltimaTecla(self):
    return Interface.tempo_ultima_tecla   
  def GerenciaPedidosScroll(self):
     lista_pop = []
     for i in range(len(Interface.pedidos_scroll_f2)):
         if Interface.pedidos_scroll_f2[i][1] < millis()-1000:
             lista_pop.append(i)
         else:
             Interface.scroll_f2+= Interface.pedidos_scroll_f2[i][0]*(1000 + Interface.pedidos_scroll_f2[i][0] - millis())*0.00001     
     for i in lista_pop:
         Interface.pedidos_scroll_f2.pop(i)
     lista_pop = []
     for i in range(len(Interface.pedidos_scroll_f3)):
         if Interface.pedidos_scroll_f3[i][1] < millis()-1000:
             lista_pop.append(i)
         else:
             Interface.scroll_f3+= Interface.pedidos_scroll_f3[i][0]*(1000 + Interface.pedidos_scroll_f3[i][0] - millis())*0.00001    
     for i in lista_pop:
         Interface.pedidos_scroll_f3.pop(i)
     lista_pop = []
     for i in range(len(Interface.pedidos_scroll_f4)):
         if Interface.pedidos_scroll_f4[i][1] < millis()-1000:
             lista_pop.append(i)
         else:
             Interface.scroll_f4+= Interface.pedidos_scroll_f4[i][0]*(1000 + Interface.pedidos_scroll_f4[i][0] - millis())*0.00001   
     for i in lista_pop:
         Interface.pedidos_scroll_f4.pop(i)
                  
  def DeletaString(self): Interface.tmp_text = ''
  def RetornaString(self): return Interface.tmp_text
  def MudaString(self,tmp_text):Interface.tmp_text = tmp_text
  def RetornaScroll(self,x=0): 
     Interface().GerenciaPedidosScroll() 
     if x == 2:return Interface.scroll_f2
     elif x == 3:return Interface.scroll_f3
     elif x == 4:return Interface.scroll_f4
  def ZeraScroll(self): Interface.valor_scroll = 0
  def RetornaEspacoPressionado(self): return Interface.espaco_pressionado  
  def EspacoPressionado(self): 
    Interface.espaco_pressionado = True
  def DesativaEspacoPressionado(self): Interface.espaco_pressionado = False
  def PalavrasChave(self):
      if Interface.tmp_text == 'novo ip':
          Interface().MudaString('Digite o novo ip: ')
          Data().SalvaDadosDeComunicacao()
      if Interface.tmp_text == 'sair':
          Interface().MudaString('Salvando dados ...')
          exit()    
      if Interface.tmp_text == 'modo servidor':
          Tarefas().Tarefa('Desativa Frame Cliente')
          Tarefas().Tarefa('Ativa Frame Servidor')
      if Interface.tmp_text == 'modo cliente':
          Tarefas().Tarefa('Desativa Frame Servidor')
          Tarefas().Tarefa('Ativa Frame Cliente')    
def keyPressed():
  
  Interface().MudaTempoUltimaTecla()
  if key >= 'a' and key <= 'z' or key == ' ' or key == '.' or key >= 'A' and key <= 'Z' or key >= '0' and key <= '9' or key == '!' or key == '?':
    Interface.tmp_text += str(key)
    Tarefas().TarefaLetra(key)
  if keyCode == DOWN:
    Tarefas().TarefaCodigo('DOWN')
  elif keyCode == LEFT:
    Tarefas().TarefaCodigo('LEFT')
  elif keyCode == RIGHT:
    Tarefas().TarefaCodigo('RIGHT')
  elif keyCode == UP:
    Tarefas().TarefaCodigo('UP')
  elif keyCode == ENTER:
    Tarefas().TarefaCodigo('ENTER')
  if key==DELETE:
    Interface().DeletaString()
  if key==BACKSPACE:
      Interface.tmp_text = Interface.tmp_text[0:int(len(Interface.tmp_text) - 1)]
  else:
      Interface().PalavrasChave()    
#def mousePressed():
    #TAREFAS = Tarefas()
    #TAREFAS.TarefaCodigo('MOUSEPRESSED')
def mouseDragged():
    Tarefas().TarefaCodigo('MOUSEDRAGGED')
def mouseClicked():  
    Interface.mouse_clicked = True;
    Tarefas().TarefaCodigo('MOUSECLICKED')
def mouseWheel(event):
  e = event.getCount();
  if e>0:
    #println(str(mouseX)+" "+str(mouseY))
    Tarefas().TarefaCodigo('SCROLLUP')
  else:
    Tarefas().TarefaCodigo('SCROLLDOWN')
    pass
  