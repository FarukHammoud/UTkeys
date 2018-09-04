from index import *
class AnimacaoDeEspera:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.etapa = 1
        self.tempo_inicial = millis()
    def Mostrar(self):
        x_ini = self.x - height/50
        y_ini = self.y - height/50
        tam = height/25
        tempo = millis() - self.tempo_inicial 
        fill(255,0,0)
        #rect(x_ini,y_ini,tam,tam)
        if tempo > 500:
            tempo = 500
            self.etapa+=1
            self.tempo_inicial = millis()
            if self.etapa >= 5: 
                self.etapa = 1
               
        if self.etapa == 1:
            fill(255,255,0,255*(float(tempo)/500))
            beginShape()
            vertex(x_ini,y_ini+tam)
            vertex(x_ini,y_ini+tam*(1-float(tempo)/500))
            vertex(x_ini+tam*(float(tempo)/500),y_ini)
            vertex(x_ini+tam,y_ini)
            vertex(x_ini+tam,y_ini+tam)
            endShape(CLOSE)
        elif self.etapa == 2:
            fill(255,255,0,255*(1-float(tempo)/500))
            beginShape()
            vertex(x_ini+tam,y_ini+tam)
            vertex(x_ini,y_ini+tam)
            vertex(x_ini,y_ini)
            vertex(x_ini+tam*(float(tempo)/500),y_ini)
            vertex(x_ini+tam,y_ini+tam*(float(tempo)/500))
            endShape(CLOSE)
        elif self.etapa == 3:
            fill(100,100,100,255*(float(tempo)/500))
            beginShape()
            vertex(x_ini,y_ini+tam)
            vertex(x_ini,y_ini)
            vertex(x_ini+tam,y_ini)
            vertex(x_ini+tam,y_ini+tam*(float(tempo)/500))
            vertex(x_ini+tam*(1-float(tempo)/500),y_ini+tam)
            endShape(CLOSE)
        elif self.etapa == 4:
            fill(100,100,100,255*(1-float(tempo)/500))
            beginShape()
            vertex(x_ini,y_ini)
            vertex(x_ini+tam,y_ini)
            vertex(x_ini+tam,y_ini+tam)
            vertex(x_ini+tam*(1-float(tempo)/500),y_ini+tam)
            vertex(x_ini,y_ini+tam*(1-float(tempo)/500))
            endShape(CLOSE)       
                
            
            
            
        
        
        
class Cores:

  branco = color(255)
  preto = color(0)
  vermelho = color(255, 0, 0)
  verde = color(0, 255, 0)
  verde_real = color(60, 255, 0)
  azul = color(0, 0, 255)
  azul_claro = color(0, 230, 250)
  verde_claro = color(50, 250, 0)
  rosa = color(250, 100, 200)
  amarelo = color(250, 250, 0)
  cinza_escuro = color(50, 50, 50)
  cinza = color(150, 150, 150)
  cinza_claro = color(200, 200, 200)
  cinza_muito_claro = color(225, 225, 225)
  cinza_azulado = color(60, 100, 130)

class Ponto3D:
    def __init__(self,lista = [0,0,0]):
        self.x=lista[0]
        self.y=lista[1]
        self.z=lista[2]
    def MudaPontos(self,lista = [0,0,0]):
        self.x=lista[0]
        self.y=lista[1]
        self.z=lista[2]
        
class TextBox:

  def Limpar(self): self.texto = ''
  
  def __init__ (self,x,y):
    self.x = x
    self.y = y
    self.texto = ''
    self.sufixo = ''
    self.txt_vazio = ''
    self.habilitado = False
    self.mouse_em_cima = False
    self.pressionado = False
    
  def MudaTexto(self,texto): self.texto = texto
  def MudaSufixo(self,sufixo): self.sufixo = sufixo
  def MudaTXTVazio(self,txt_vazio): self.txt_vazio = txt_vazio
  def MudaXY(self,x,y):
    self.x = x
    self.y = y
  def Texto(self): return self.texto
  def Mostrar(self):
    fill(Cores().branco)
    stroke(200, 200, 200)
    rect(self.x, self.y, 150, 20)
    textSize(14)
    fill(100, 100, 100)
    if (self.texto == ''):
      text(self.txt_vazio, self.x+10, self.y+17)
    else:
      text(self.texto+' '+self.sufixo, self.x+10, self.y+17)
    if Calculo().MouseIn(self.x,self.y,150,20):  
      self.mouse_em_cima = True;
    else:
      self.mouse_em_cima = False
      self.habilitado = False
    if self.mouse_em_cima and mousePressed:
      self.pressionado = True;
    elif self.pressionado:
      self.pressionado = False
      self.habilitado = True
      self.texto = ''
      Interface().DeletaString()
    if self.habilitado:
      self.texto = Interface().RetornaString()
    if self.mouse_em_cima: 
      fill(Cores().branco)
      stroke(0, 200, 0)
      rect(self.x, self.y, 150, 20)
      textSize(14)
      fill(Cores().preto)
      if self.texto != '':
        text(self.texto+' '+self.sufixo, self.x+10, self.y+17)
      elif self.habilitado:
        if (millis()/500)%2 == 0:
          text('_', self.x+10, self.y+17)
class LeitorQR:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.codigo = ''
        self.disponivel = False
        self.procurando = False
        self.img = PImage()
        self.tempo = 9999999
    def Disponivel(self): return self.disponivel
    def Reset(self): 
        self.disponivel = False
        self.procurando = False
    def Codigo(self): return self.codigo
    def MudaXY(self,x,y):
        self.x = x
        self.y = y
    def AtualizaImagem(self): 
        import __main__
        __main__.web_cam.Capta()
        self.img = __main__.web_cam.Imagem()
    def LeQRcode(self):
        #QR().Decodifica(self.img)
        QR().Decodifica(loadImage('FARUK HAMMOUD.png'))
        self.procurando = True        
        self.tempo = millis()
    def Layout(self):   
        tint(100)
        fill(150,150,150)
        noStroke()
        rect(self.x,self.y,610,200,20)
        if self.disponivel: stroke(0,255,0)
        elif self.procurando: stroke(255,255,0)
        else: stroke(255,0,0)
        tint(255)
        rect(self.x+20,self.y+20,217,162)
        image(self.img,self.x+21,self.y+21,215,160)
        stroke(150,150,150,150)
        for i in range(self.x+21,self.x+236,20): line(i,self.y+21,i,self.y+181)
        for j in range(self.y+21,self.y+180,20): line(self.x+21,j,self.x+236,j)
        fill(255,255,255)
        textSize(18)
        text('- Pressione espaco para ler o QR code -',self.x+250,self.y+40)   
    def Mostrar(self):
        Tarefas().AlteraTarefaLetra('Identifica QRcode',' ')
        if self.procurando:
            if(millis() > self.tempo + 500):
                QR().CaptaCodigo()
                self.procurando = False
                if not QR().RetornaCodigoLido() == 'NO QRcode image found':
                    self.disponivel = True
                    Tarefas().AlteraTarefaLetra('',' ')
                    self.codigo = QR().RetornaCodigoLido()
                    print(self.codigo)
        self.AtualizaImagem()
        self.Layout()
        if Interface().RetornaEspacoPressionado():
            Interface().DesativaEspacoPressionado()
            self.LeQRcode()     
                        
class ListaLateral:

  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.inicial = ''
    self.atual = ''
    self.lista = []
    self.n = 0
    
    self.mouse_em_cima_1 = False
    self.mouse_em_cima_2 = False
    self.pressionado_1 = False
    self.pressionado_2 = False

    self.iniciado = False
  def MudaXY(self,x,y):
    self.x = x
    self.y = y
  
  def MudaInicial(self,inicial):

    if not self.iniciado:
      self.inicial = inicial
      for i in range(self.nOf_itens):
        if self.inicial == self.lista[a]:
          self.n = a;
      self.iniciado = True;
  def CarregaLista(self,listagem):
    self.lista = []  
    #carregar
    if listagem == 'Geral,Fluido 1,Fluido 2,Calculo': 
      pass  
      # self.nOf_itens = FRAMES.FRAME_concentrico.lista_comum.length;
      #for (int a=0; a<FRAMES.FRAME_concentrico.lista_comum.length; a++) {
      #self.lista[a] = FRAMES.FRAME_concentrico.lista_comum[a];
      #}
    
    if listagem == 'moleculas':
      pass
      #self.nOf_itens = DATA.moleculas.length;
      #for (int a=0; a<DATA.moleculas.length; a++) {
      #  self.lista[a] = DATA.moleculas[a];
      #}
    if listagem == 'usuarios':
      for i in range(len(Data().usuario)):
          self.lista.append(Data().usuario[i][1])
    if listagem == 'categorias':
      self.lista = ['Aluno','Professor','Servidor']   
    if listagem == 'salas':
      self.lista = ['N001','N002','N003','EK001','EK102']          
  def IndiceN(self): return self.n
  def Texto(self): return self.lista[self.n]
  def Mostrar(self):
    stroke(150, 150, 150)
    if Calculo().MouseInC([self.x, self.y-8],10):
      self.mouse_em_cima_1 = True
      fill(200+(mouseX%20), 200+(mouseY%20), 200+((mouseX+mouseY)%20))
    else: 
      self.mouse_em_cima_1 = False
      fill(255, 255, 255)
    if self.mouse_em_cima_1 and mousePressed:
      self.pressionado_1 = True
    elif self.pressionado_1:
      self.n-=1
      if self.n < 0:
        self.n = 0
      self.pressionado_1 = False
    ellipse(self.x, self.y-8, 20, 20)
    triangle(self.x-5, self.y-8, self.x+5, self.y-5, self.x+5, self.y-11)
    if Calculo().MouseInC([self.x+230,self.y-8],10):
      self.mouse_em_cima_2 = True
      fill(200+(mouseX%20), 200+(mouseY%20), 200+((mouseX+mouseY)%20))
    else: 
      self.mouse_em_cima_2 = False
      fill(Cores().branco)
    if self.mouse_em_cima_2 and mousePressed:
      self.pressionado_2 = True
    elif self.pressionado_2:
      self.n+=1
      if self.n > len(self.lista)-1:
        self.n = len(self.lista)-1
      self.pressionado_2 = False
    ellipse(self.x+230, self.y-8, 20, 20)
    triangle(self.x+235, self.y-8, self.x+225, self.y-5, self.x+225, self.y-11)
    fill(255, 255, 255)
    rect(self.x+15, self.y-18, 200, 20, 10)
    fill(150)
    textSize(16)
    text(str(self.lista[self.n]), float(self.x+20),float(self.y-1))
  
class CheckBox:
  def __init__(self,x,y,texto = '',valor = False):
    self.x = x
    self.y = y
    self.texto = texto
    self.valor = valor
    
    self.mouse_em_cima = False
    self.pressionado = False
  def RetornaValor(self): return self.valor
  def MudaTexto(self,texto): self.texto = texto
  def MudaXY(self,x,y):
    self.x = x
    self.y = y
  def Mostrar(self,):
    fill(Cores().braco)
    stroke(200, 200, 200)
    rect(self.x, self.y, 10, 10)
    textSize(10)
    fill(Cores().preto)
    text(self.texto, self.x+20, self.y+10);
    if self.valor:
      fill(Cores().verde) 
      ellipse(self.x+5, self.y+5, 4, 4)
    if Calculo().MouseIn(self.x,self.y,10,10):
      self.mouse_em_cima = True
    else:
      self.mouse_em_cima = False
    if self.mouse_em_cima and mousePressed:
      self.pressionado = True
    elif self.pressionado:
      if self.valor:
        self.valor = False
      else :
        self.valor = True
      self.pressionado = False
    if self.mouse_em_cima:
      fill(0, 100, 0) 
      ellipse(self.x+5, self.y+5, 4, 4)
class Botao:
  def __init__(self,tipo,x,y,link_tarefa_a,link_tarefa_b):
    self.tipo = tipo
    self.x = x
    self.y = y
    self.link_tarefa_a = link_tarefa_a
    self.link_tarefa_b = link_tarefa_b
    self.tam_x = 10
    self.tam_y = 10
    self.tam_text = 16
    self.texto = ''
    self.numero_de_letras = 0
    self.mouse_em_cima = False
    self.clicado = False
    self.pressionado = False
    self.habilitado = False
  def MudaXY(self,x,y):
    self.x = x
    self.y = y
  def MudaTexto(self,texto): self.texto = texto
  def RetornaValor(self):
    if self.pressionado: return True
    else: return False
  def MudaTamanho(self,tam_x,tam_y):
    self.tam_x = tam_x
    self.tam_y = tam_y  
  def MudaTamanhoTexto(self,tam):
    self.tam_text = tam
  def Habilita(self): self.habilitado = True
  def Desabilita(self): self.habilitado = False  
  def Mostrar(self):
    if self.tipo == 'habilitavel':
        stroke(Cores().cinza)
        strokeWeight(1)
        if self.habilitado:
            if Calculo().MouseIn(self.x,self.y-18,self.tam_x,self.tam_y):
                self.mouse_em_cima = True
                Tarefas().Tarefa(self.link_tarefa_a)
                fill(200+(mouseX%20), 200+(mouseY%20), 200+((mouseX+mouseY)%20))
                if mousePressed:
                    self.pressionado = True
                elif self.pressionado:  
                    self.pressionado = False  
                    Tarefas().Tarefa(self.link_tarefa_b)
            else: 
                self.mouse_em_cima = False
                fill(Cores().branco)
            
            rect(self.x, self.y-18, self.tam_x,self.tam_y, 20)
            fill(Cores().cinza)
            textSize(self.tam_text)
            text(self.texto, self.x+5, self.y-1)   
        else:
            fill(Cores().cinza_escuro)
            rect(self.x, self.y-18, self.tam_x,self.tam_y, 20)
            fill(Cores().cinza)
            textSize(self.tam_text)
            text(self.texto, self.x+5, self.y-1)        
    if self.tipo == 'dinamico':
        stroke(Cores().cinza)
        strokeWeight(1)
        if Calculo().MouseIn(self.x,self.y-18,self.tam_x,self.tam_y):
            self.mouse_em_cima = True
            Tarefas().Tarefa(self.link_tarefa_a)
            fill(200+(mouseX%20), 200+(mouseY%20), 200+((mouseX+mouseY)%20))
            if mousePressed:
                self.pressionado = True
            elif self.pressionado:    
                Tarefas().Tarefa(self.link_tarefa_b)
        else: 
            self.mouse_em_cima = False
            fill(Cores().branco)
        
        rect(self.x, self.y-18, self.tam_x,self.tam_y, 20)
        fill(Cores().cinza)
        textSize(16)
        text(self.texto, self.x+5, self.y-1)
    if self.tipo == 'quadrado arredondado dinamico':
        stroke(Cores().cinza)
        if Calculo().MouseIn(self.x,self.y,self.tam_x,self.tam_y):
            self.mouse_em_cima = True
            Tarefas().Tarefa(self.link_tarefa_a)
            fill(200+(mouseX%20), 200+(mouseY%20), 200+((mouseX+mouseY)%20))
        else: 
            self.mouse_em_cima = False
            fill(Cores().branco)
        if self.mouse_em_cima and mousePressed:
            self.pressionado = True
            Tarefas().Tarefa(self.link_tarefa_b)
            stroke(200,200,200)     
        rect(self.x, self.y, self.tam_x, self.tam_y, 20)
        fill(Cores().cinza)
        textSize(16)
        text(self.texto, self.x+8, self.y+self.tam_y - 5)  
            
    
    
    
  
       