
from index import *

#Frames do Programa
class FrameServidor:
    #Objetos do Frame
  
    #Variaveis do Frame
    vetor_mouse_em_cima = [False,False,False,False,False,False]
    vetor_pressionado = [False,False,False,False,False,False]
    flag = False
    n_flag = False #reciclavel
    logado = False
    text_box_1 = TextBox(0,0)
    text_box_2 = TextBox(0,0)
    lista_lateral_1 = ListaLateral(0,0)
    lista_lateral_2 = ListaLateral(0,0)
    lista_lateral_3 = ListaLateral(0,0)
    leitor_qr = LeitorQR(0,0)
    botao_avancar = Botao('habilitavel',0,0,'','Estado +=1')
    botao_concluir = Botao('habilitavel',0,0,'','Estado +=1')
    estado = 0
    one_time = True
    #Funcoes do Frame
    def IniciaImagens(self):
        FrameServidor.foto_utfpr = loadImage('foto_utfpr.jpg')
        FrameServidor.utkeys = loadImage('UTkeys.png')
    def IniciaObjetos(self):
        if FrameServidor.one_time:
            FrameServidor().IniciaImagens()
            FrameServidor.one_time = False
    def DesenhaLayout(self):
        noStroke()
        tint(250,250,0)
        image(FrameServidor.foto_utfpr,0,0,width,height)
        fill(250,250,250,150)#220
        rect(width/2-440,(height-50)/2-220,880,440,44) 
        fill(250,250,0)
        textSize(15)
        text('desenvolvido por Faruk Hammoud, 2016.',width - 310,height - 20)
        fill(250,250,0)
        noTint()
        image(FrameServidor.utkeys,width/2-100,height/2-245,200,80)
        fill(250,250,0,100)
        rect(width/2-430,(height-50)/2-140,860,350,40)
        fill(100,100,100,100)
        rect(width/2-420,(height-50)/2-130,200,330,30) 
    def MostraTmpText(self):
        if millis() - Interface().RetornaTempoUltimaTecla() < 2000:
            fill(Cores().preto,(2000 - (millis() - Interface().RetornaTempoUltimaTecla()))/3)
            textSize(20)
            text('>'+Interface().RetornaString(),30,height-10)  
    def Mostrar(self):
       FrameServidor().IniciaObjetos() 
       FrameServidor().DesenhaLayout() 
       FrameServidor().MostraTmpText() 
       Comunicacao().AtendeMensagens()
       for i in range(6):
            fill(255,255,255,200)
            if FrameServidor.vetor_mouse_em_cima[i]:
                fill(200,200,200,200)
            if Calculo().MouseIn(width/2-410,(height-50)/2-120+50*i,180,40):
                FrameServidor.vetor_mouse_em_cima[i] = True
                if mousePressed:
                    FrameServidor.flag = True  
                if FrameServidor.flag and not mousePressed:
                    FrameServidor.flag = False   
                    if FrameServidor.vetor_pressionado[i]:
                        FrameServidor.vetor_pressionado[i] = False
                        
                    else:
                        FrameServidor.vetor_pressionado[0] = False
                        FrameServidor.vetor_pressionado[1] = False
                        FrameServidor.vetor_pressionado[2] = False
                        FrameServidor.vetor_pressionado[3] = False
                        FrameServidor.vetor_pressionado[4] = False
                        FrameServidor.vetor_pressionado[5] = False
                        FrameServidor.vetor_pressionado[i] = True 
                        FrameServidor.text_box_1.Limpar()
                        FrameServidor.text_box_2.Limpar()
                        FrameServidor.estado = 0   
            else:
                FrameServidor.vetor_mouse_em_cima[i] = False    
            if FrameServidor.vetor_pressionado[i]:        
                fill(50,50,50,200)   
            noStroke()    
            rect(width/2-410,(height-50)/2-120+50*i,180,40,20)  
            if FrameServidor.vetor_pressionado[i]:        
                fill(255,255,255)
                rect(width/2-210,(height-50)/2-130,630,330,30)   
                if i == 0:
                    if FrameServidor.estado == 0:
                        textSize(20)
                        fill(150,150,150)
                        text('Passo 1: Mostre o QR Code do seu cracha.',width/2-200,(height-50)/2 -100) 
                        FrameServidor.leitor_qr.Mostrar()
                        if FrameServidor.leitor_qr.Disponivel():
                            FrameServidor.nome = FrameServidor.leitor_qr.Codigo()
                            FrameServidor.botao_avancar.Mostrar()
                    if FrameServidor.estado == 1:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 2: Mostre o QR Code da chave.',width/2-200,(height-50)/2 -100) 
                        FrameServidor.leitor_qr.Mostrar()
                        if FrameServidor.leitor_qr.Disponivel():
                            FrameServidor.chave = FrameServidor.leitor_qr.Codigo()
                            FrameServidor.botao_concluir.Mostrar()     
                            FrameServidor.n_flag = True
                    if FrameServidor.estado == 2:
                        textSize(20)
                        fill(150,150,150) 
                        if FrameServidor.n_flag:
                            Comunicacao().ComunicaEmprestimo(FrameServidor.nome,FrameServidor.chave)
                            FrameServidor.n_flag = False      
                        text('Emprestimo concluido!',width/2-200,(height-50)/2 -100)                
                elif i == 1:
                    if FrameServidor.estado == 0:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 1: Mostre o QR Code da chave.',width/2-200,(height-50)/2 -100) 
                        FrameServidor.leitor_qr.Mostrar()
                        if FrameServidor.leitor_qr.Disponivel():
                            FrameServidor.chave = FrameServidor.leitor_qr.Codigo()
                            FrameServidor.botao_avancar.Mostrar() 
                            FrameServidor.n_flag = True
                    if FrameServidor.estado == 1:
                        textSize(20)
                        fill(150,150,150)   
                        if FrameServidor.n_flag:
                            Comunicacao().ComunicaDevolucao(FrameServidor.chave)
                            FrameServidor.n_flag = False
                        text('Devolucao Concluida!',width/2-200,(height-50)/2 -100)     
                elif i == 2:
                    if FrameServidor.estado == 0:
                        textSize(20)
                        fill(150,150,150)
                        text('Passo 1: Digite abaixo o seu nome e seleciona a categoria:',width/2-200,(height-50)/2 -100)
                        FrameServidor.text_box_1.Mostrar()
                        FrameServidor.lista_lateral_2.Mostrar()
                        FrameServidor.nome = FrameServidor.text_box_1.Texto()
                        FrameServidor.categoria = FrameServidor.lista_lateral_2.Texto()
                        FrameServidor.botao_avancar.Mostrar()
                    if FrameServidor.estado == 1:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 2: Mostre o QR Code do seu cracha.',width/2-200,(height-50)/2 -100) 
                        FrameServidor.leitor_qr.Mostrar()
                        if FrameServidor.leitor_qr.Disponivel():
                            FrameServidor.qr = FrameServidor.leitor_qr.Codigo()
                            FrameServidor.n_flag = True
                            FrameServidor.botao_concluir.Mostrar()      
                    if FrameServidor.estado == 2:
                        textSize(20)
                        fill(150,150,150)  
                        if FrameServidor.n_flag:
                            Comunicacao().ComunicaCadastro(FrameServidor.nome,FrameServidor.categoria,FrameServidor.qr)
                            FrameServidor.n_flag = False 
                        text('Cadastro Concluido!',width/2-200,(height-50)/2 -100)    
                elif i == 3:
                    if FrameServidor.estado == 0:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 1: Mostre o QR Code da chave que gostaria de autorizar.',width/2-200,(height-50)/2 -100) 
                        FrameServidor.leitor_qr.Mostrar()
                        if FrameServidor.leitor_qr.Disponivel():
                            FrameServidor.botao_avancar.Mostrar()
                    if FrameServidor.estado == 1:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 2: Mostre o QR Code do responsavel pela chave.',width/2-200,(height-50)/2 -100) 
                        FrameServidor.leitor_qr.Mostrar()
                        if FrameServidor.leitor_qr.Disponivel():
                            FrameServidor.botao_avancar.Mostrar()  
                    if FrameServidor.estado == 2:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 3: Mostre o QR Code do novo autorizado.',width/2-200,(height-50)/2 -100) 
                        FrameServidor.leitor_qr.Mostrar()
                        if FrameServidor.leitor_qr.Disponivel():
                            FrameServidor.botao_concluir.Mostrar()
                    if FrameServidor.estado == 3:
                        textSize(20)
                        fill(150,150,150)   
                        if FrameServidor.n_flag:
                            Comunicacao().ComunicaAutorizacao(FrameServidor.nome,FrameServidor.categoria,FrameServidor.qr)
                            FrameServidor.n_flag = False 
                        text('Autorizacao Concluida!',width/2-200,(height-50)/2 -100)                         
                elif i == 4:
                    if FrameServidor.estado == 0:
                        textSize(20)
                        fill(150,150,150)
                        text('Passo 1: Selecione a sala que gostaria de vincular:',width/2-200,(height-50)/2 -100)         
                        FrameServidor.lista_lateral_3.Mostrar()
                        FrameServidor.botao_avancar.Mostrar()
                    if FrameServidor.estado == 1: 
                        textSize(20)
                        fill(150,150,150)
                        text('Passo 2: Mostre o QR Code do seu cracha:',width/2-200,(height-50)/2 -100)  
                        FrameServidor.leitor_qr.Mostrar()
                        if FrameServidor.leitor_qr.Disponivel():
                            FrameServidor.botao_concluir.Mostrar()
                    if FrameServidor.estado == 2:
                        textSize(20)
                        fill(150,150,150)   
                        text('Solicitacao de vinculo enviada!',width/2-200,(height-50)/2 -100)         
                elif i == 5:
                    textSize(20)
                    fill(150,150,150)
                    text('Passo 1: Selecione a sala que gostaria de visualizar o historico:',width/2-200,(height-50)/2 -100)       
                    FrameServidor.lista_lateral_3.Mostrar()
                    FrameServidor.botao_avancar.Mostrar()    
       textSize(25)
       fill(0)
       text('PROMP-UT',width/2-400,(height-50)/2-90)
       text('Cadastrar',width/2-400,(height-50)/2-90+50)
       text('Vincular',width/2-400,(height-50)/2-90+100)
       text('Autorizar',width/2-395,(height-50)/2-90+150)
       text('Historico',width/2-395,(height-50)/2-90+200)
       text('Relatorio',width/2-395,(height-50)/2-90+250)                        
class FrameCliente:
    
    #Objetos do Frame
  
    #Variaveis do Frame
    vetor_mouse_em_cima = [False,False,False,False,False,False]
    vetor_pressionado = [False,False,False,False,False,False]
    flag = False
    n_flag = False #reciclavel
    logado = False
    text_box_1 = TextBox(0,0)
    text_box_2 = TextBox(0,0)
    lista_lateral_1 = ListaLateral(0,0)
    lista_lateral_2 = ListaLateral(0,0)
    lista_lateral_3 = ListaLateral(0,0)
    leitor_qr = LeitorQR(0,0)
    botao_avancar = Botao('habilitavel',0,0,'','Estado +=1')
    botao_concluir = Botao('habilitavel',0,0,'','Estado +=1')
    estado = 0
    one_time = True
    carregador = AnimacaoDeEspera(width/2+390,height/2+145)
    #Funcoes do Frame
    def EstadoAdd(self): 
        FrameCliente.estado+=1
        FrameCliente.leitor_qr.Reset()
    def IniciaImagens(self):
        FrameCliente.foto_utfpr = loadImage('foto_utfpr.jpg')
        FrameCliente.utkeys = loadImage('UTkeys.png')
    def DesenhaLayout(self):
        noStroke()
        tint(250,250,0)
        image(FrameCliente.foto_utfpr,0,0,width,height)
        fill(250,250,250,150)#220
        rect(width/2-440,(height-50)/2-220,880,440,44) 
        fill(250,250,0)
        textSize(15)
        text('desenvolvido por Faruk Hammoud, 2016.',width - 310,height - 20)
        fill(250,250,0)
        noTint()
        image(FrameCliente.utkeys,width/2-100,height/2-245,200,80)
        fill(250,250,0,100)
        rect(width/2-430,(height-50)/2-140,860,350,40)
        fill(100,100,100,100)
        rect(width/2-420,(height-50)/2-130,200,330,30)  
    def IniciaObjetos(self):
        #inicializacao das imagens
        if FrameCliente.one_time:
            FrameCliente().IniciaImagens()
            FrameCliente.one_time = False
        #textbox
        FrameCliente.text_box_1.MudaXY(width/2-180,(height-50)/2 -90)
        FrameCliente.text_box_2.MudaXY(width/2-180,(height-50)/2 -40)
        #listas laterais
        FrameCliente.lista_lateral_1.CarregaLista('usuarios')
        FrameCliente.lista_lateral_1.MudaXY(width/2-170,(height-50)/2-75)
        FrameCliente.lista_lateral_2.CarregaLista('categorias')
        FrameCliente.lista_lateral_2.MudaXY(width/2 ,(height-50)/2-72)
        FrameCliente.lista_lateral_3.CarregaLista('salas')
        FrameCliente.lista_lateral_3.MudaXY(width/2-170,(height-50)/2-75)
        #leitor qr
        FrameCliente.leitor_qr.MudaXY(width/2-200,height/2 - 110)
        #boato avancar
        FrameCliente.botao_avancar.MudaXY(width/2+210,height/2 + 120)
        FrameCliente.botao_avancar.MudaTamanho(200,60)
        FrameCliente.botao_avancar.Habilita()
        FrameCliente.botao_avancar.MudaTexto('Avancar')
        #boato concluir
        FrameCliente.botao_concluir.MudaXY(width/2+210,height/2 + 120)
        FrameCliente.botao_concluir.MudaTamanho(200,60)
        FrameCliente.botao_concluir.Habilita()
        FrameCliente.botao_concluir.MudaTexto('Concluir')  
    def MostraTmpText(self):
        if millis() - Interface().RetornaTempoUltimaTecla() < 2000:
            fill(Cores().preto,(2000 - (millis() - Interface().RetornaTempoUltimaTecla()))/3)
            textSize(20)
            text('>'+Interface().RetornaString(),30,height-10)    
  #Visualizacao
    def Mostrar(self): 
        FrameCliente().IniciaObjetos()   
        FrameCliente().DesenhaLayout()
        FrameCliente().MostraTmpText()
        Comunicacao().Mostrar()
        for i in range(6):
            fill(255,255,255,200)
            if FrameCliente.vetor_mouse_em_cima[i]:
                fill(200,200,200,200)
            if Calculo().MouseIn(width/2-410,(height-50)/2-120+50*i,180,40):
                FrameCliente.vetor_mouse_em_cima[i] = True
                if mousePressed:
                    FrameCliente.flag = True  
                if FrameCliente.flag and not mousePressed:
                    FrameCliente.flag = False   
                    if FrameCliente.vetor_pressionado[i]:
                        FrameCliente.vetor_pressionado[i] = False
                        
                    else:
                        FrameCliente.vetor_pressionado[0] = False
                        FrameCliente.vetor_pressionado[1] = False
                        FrameCliente.vetor_pressionado[2] = False
                        FrameCliente.vetor_pressionado[3] = False
                        FrameCliente.vetor_pressionado[4] = False
                        FrameCliente.vetor_pressionado[5] = False
                        FrameCliente.vetor_pressionado[i] = True 
                        FrameCliente.text_box_1.Limpar()
                        FrameCliente.text_box_2.Limpar()
                        FrameCliente.estado = 0   
            else:
                FrameCliente.vetor_mouse_em_cima[i] = False    
            if FrameCliente.vetor_pressionado[i]:        
                fill(50,50,50,200)   
            noStroke()    
            rect(width/2-410,(height-50)/2-120+50*i,180,40,20)  
            if FrameCliente.vetor_pressionado[i]:        
                fill(255,255,255)
                rect(width/2-210,(height-50)/2-130,630,330,30)   
                if i == 0:
                    if FrameCliente.estado == 0:
                        textSize(20)
                        fill(150,150,150)
                        text('Passo 1: Mostre o QR Code do seu cracha.',width/2-200,(height-50)/2 -100) 
                        FrameCliente.leitor_qr.Mostrar()
                        if FrameCliente.leitor_qr.Disponivel():
                            FrameCliente.nome = FrameCliente.leitor_qr.Codigo()
                            FrameCliente.botao_avancar.Mostrar()
                    if FrameCliente.estado == 1:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 2: Mostre o QR Code da chave.',width/2-200,(height-50)/2 -100) 
                        FrameCliente.leitor_qr.Mostrar()
                        if FrameCliente.leitor_qr.Disponivel():
                            FrameCliente.chave = FrameCliente.leitor_qr.Codigo()
                            FrameCliente.botao_concluir.Mostrar()     
                            FrameCliente.n_flag = True
                    if FrameCliente.estado == 2:
                        textSize(20)
                        fill(150,150,150) 
                        if FrameCliente.n_flag:
                            Comunicacao().ComunicaEmprestimo(FrameCliente.nome,FrameCliente.chave)
                            FrameCliente.n_flag = False      
                        text('Aguardando resposta do servidor ...',width/2-200,(height-50)/2 -100) 
                        FrameCliente.carregador.Mostrar() 
                    if FrameCliente.estado == 3:
                        textSize(20)
                        fill(150,150,150)  
                        text('Emprestimo concluido!',width/2-200,(height-50)/2 -100)                   
                elif i == 1:
                    if FrameCliente.estado == 0:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 1: Mostre o QR Code da chave.',width/2-200,(height-50)/2 -100) 
                        FrameCliente.leitor_qr.Mostrar()
                        if FrameCliente.leitor_qr.Disponivel():
                            FrameCliente.chave = FrameCliente.leitor_qr.Codigo()
                            FrameCliente.botao_avancar.Mostrar() 
                            FrameCliente.n_flag = True
                    if FrameCliente.estado == 1:
                        textSize(20)
                        fill(150,150,150)   
                        if FrameCliente.n_flag:
                            Comunicacao().ComunicaDevolucao(FrameCliente.chave)
                            FrameCliente.n_flag = False
                        text('Aguardando resposta do servidor ...',width/2-200,(height-50)/2 -100) 
                        FrameCliente.carregador.Mostrar() 
                    if FrameCliente.estado == 2:    
                        textSize(20)
                        fill(150,150,150) 
                        text('Devolucao Concluida!',width/2-200,(height-50)/2 -100)    
                elif i == 2:
                    if FrameCliente.estado == 0:
                        textSize(20)
                        fill(150,150,150)
                        text('Passo 1: Digite abaixo o seu nome e seleciona a categoria:',width/2-200,(height-50)/2 -100)
                        FrameCliente.text_box_1.Mostrar()
                        FrameCliente.lista_lateral_2.Mostrar()
                        FrameCliente.nome = FrameCliente.text_box_1.Texto()
                        FrameCliente.categoria = FrameCliente.lista_lateral_2.Texto()
                        FrameCliente.botao_avancar.Mostrar()
                    if FrameCliente.estado == 1:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 2: Mostre o QR Code do seu cracha.',width/2-200,(height-50)/2 -100) 
                        FrameCliente.leitor_qr.Mostrar()
                        if FrameCliente.leitor_qr.Disponivel():
                            FrameCliente.qr = FrameCliente.leitor_qr.Codigo()
                            FrameCliente.n_flag = True
                            FrameCliente.botao_concluir.Mostrar()      
                    if FrameCliente.estado == 2:
                        textSize(20)
                        fill(150,150,150)  
                        if FrameCliente.n_flag:
                            Comunicacao().ComunicaCadastro(FrameCliente.nome,FrameCliente.categoria,FrameCliente.qr)
                            FrameCliente.n_flag = False 
                        text('Aguardando resposta do servidor ...',width/2-200,(height-50)/2 -100) 
                        FrameCliente.carregador.Mostrar()   
                    if FrameCliente.estado == 3:
                        textSize(20)
                        fill(150,150,150) 
                        text('Cadastro Concluido!',width/2-200,(height-50)/2 -100)      
                elif i == 3:
                    if FrameCliente.estado == 0:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 1: Mostre o QR Code da chave que gostaria de autorizar.',width/2-200,(height-50)/2 -100) 
                        FrameCliente.leitor_qr.Mostrar()
                        if FrameCliente.leitor_qr.Disponivel():
                            FrameCliente.chave = FrameCliente.leitor_qr.Codigo()
                            FrameCliente.botao_avancar.Mostrar()
                    if FrameCliente.estado == 1:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 2: Mostre o QR Code do responsavel pela chave.',width/2-200,(height-50)/2 -100) 
                        FrameCliente.leitor_qr.Mostrar()
                        if FrameCliente.leitor_qr.Disponivel():
                            FrameCliente.cracha_autorizado = FrameCliente.leitor_qr.Codigo()
                            FrameCliente.botao_avancar.Mostrar()  
                    if FrameCliente.estado == 2:
                        textSize(20)
                        fill(150,150,150)   
                        text('Passo 3: Mostre o QR Code do novo autorizado.',width/2-200,(height-50)/2 -100) 
                        FrameCliente.leitor_qr.Mostrar()
                        if FrameCliente.leitor_qr.Disponivel():
                            FrameCliente.n_flag = True
                            FrameCliente.cracha_autorizando = FrameCliente.leitor_qr.Codigo()
                            FrameCliente.botao_concluir.Mostrar()
                    if FrameCliente.estado == 3:
                        textSize(20)
                        fill(150,150,150)  
                        if FrameCliente.n_flag:
                            Comunicacao().ComunicaAutorizacao(FrameCliente.chave,FrameCliente.cracha_autorizado,FrameCliente.cracha_autorizando)
                            FrameCliente.n_flag = False  
                        text('Aguardando resposta do servidor ...',width/2-200,(height-50)/2 -100)  
                        FrameCliente.carregador.Mostrar() 
                    if FrameCliente.estado == 4:  
                        textSize(20)
                        fill(150,150,150)       
                        text('Autorizacao Concluida!',width/2-200,(height-50)/2 -100)                      
                elif i == 4:
                    if FrameCliente.estado == 0:
                        textSize(20)
                        fill(150,150,150)
                        text('Passo 1: Selecione a sala que gostaria de vincular:',width/2-200,(height-50)/2 -100)         
                        FrameCliente.lista_lateral_3.Mostrar()
                        FrameCliente.botao_avancar.Mostrar()
                        FrameCliente.sala = FrameCliente.lista_lateral_3.Texto()
                    if FrameCliente.estado == 1: 
                        textSize(20)
                        fill(150,150,150)
                        text('Passo 2: Mostre o QR Code do seu cracha:',width/2-200,(height-50)/2 -100)  
                        FrameCliente.leitor_qr.Mostrar()
                        if FrameCliente.leitor_qr.Disponivel():
                            FrameCliente.n_flag = True
                            FrameCliente.cracha = FrameCliente.leitor_qr.Codigo()
                            FrameCliente.botao_concluir.Mostrar()
                    if FrameCliente.estado == 2:
                        textSize(20)
                        fill(150,150,150)   
                        if FrameCliente.n_flag:
                            Comunicacao().ComunicaVinculo(FrameCliente.sala,FrameCliente.cracha)
                            FrameCliente.n_flag = False  
                        text('Aguardando resposta do servidor ...',width/2-200,(height-50)/2 -100) 
                        FrameCliente.carregador.Mostrar()   
                    if FrameCliente.estado == 3:
                        textSize(20)
                        fill(150,150,150) 
                        text('Solicitacao de vinculo enviada!',width/2-200,(height-50)/2 -100)         
                elif i == 5:
                    if FrameCliente.estado == 0:
                        textSize(20)
                        fill(150,150,150)
                        text('Passo 1: Selecione a sala que gostaria de visualizar o historico:',width/2-200,(height-50)/2 -100)       
                        FrameCliente.lista_lateral_3.Mostrar()
                        FrameCliente.sala = FrameCliente.lista_lateral_3.Texto()
                        FrameCliente.botao_avancar.Mostrar()  
                        FrameCliente.n_flag = True
                    if FrameCliente.estado == 1:  
                        textSize(20)
                        fill(150,150,150)  
                        if FrameCliente.n_flag:
                            Comunicacao().ComunicaHistorico(FrameCliente.sala)
                            FrameCliente.n_flag = False       
                        text('Carregando Historico...',width/2-200,(height-50)/2 -100) 
                        FrameCliente.carregador.Mostrar()   
                        
        textSize(25)
        fill(0)
        text('Emprestar',width/2-400,(height-50)/2-90)
        text('Devolver',width/2-400,(height-50)/2-90+50)
        text('Cadastrar',width/2-400,(height-50)/2-90+100)
        text('Autorizar',width/2-395,(height-50)/2-90+150)
        text('Vincular',width/2-395,(height-50)/2-90+200)
        text('Historico',width/2-395,(height-50)/2-90+250)
class FrameAnimacaoInicial:
  
  #Objetos do Frame
  one_time = True   
  tempo_inicial = 0
  #Funcoes do Frame
  def __init__(self):
      pass
    #Variaveis do Frame
    
  def IniciaImagens(self):
      #mus_ini = soundfile()
      #mus_ini = SoundFile(self,"Muse - Undisclosed Desires.mp3")
      #mus_ini.play()
      FrameAnimacaoInicial.foto_utfpr = loadImage('foto_utfpr.jpg')
      FrameAnimacaoInicial.logo_utfpr = loadImage('UTkeys.png')
  #Visualizacao
  def Mostrar(self):
      #inicializacao das imagens
      if FrameAnimacaoInicial.one_time:
        FrameAnimacaoInicial().IniciaImagens()
        FrameAnimacaoInicial.tempo_inicial = millis()
        FrameAnimacaoInicial.one_time = False
      background(255,255,255)
      tint(250,250,0,(millis()-FrameAnimacaoInicial.tempo_inicial)/25)
      image(FrameAnimacaoInicial.foto_utfpr,0,0,width,height)
      noTint()
      image(FrameAnimacaoInicial.logo_utfpr,width/2-400,(height-50)/2-225,800,450)  
      #animacao fechamento
      if (millis()-FrameAnimacaoInicial.tempo_inicial) > width*5 :
         par = ((millis()-FrameAnimacaoInicial.tempo_inicial)-width*5)/10 
         if par > 220:
             par = 220
             Tarefas().Tarefa('Desativa Frame Animacao Inicial')
             Tarefas().Tarefa('Ativa Frame Cliente')
         fill(250,250,250,par*150/220)
         rect(width/2-par*2,(height-50)/2-par,par*4,par*2,par/5) 
        
      
      #barra de carregamento
      fill(250,250,0,(millis()-FrameAnimacaoInicial.tempo_inicial)/25)
      noStroke()
      rect(0,height-50,(millis()-FrameAnimacaoInicial.tempo_inicial)/5,5)

class Frames:

  #Lista de Controle
  frame = []

  #Declaracao de Frames
  frame_animacao_inicial = FrameAnimacaoInicial()
  frame_cliente = FrameCliente()
  frame_servidor = FrameServidor()
  
  #Metodos
  def __init__(self):
    for i in range(0,20):
      Frames.frame.append(False)
  def AtivaFrame(self,numero): Frames.frame[numero] = True 
  def AtivaFrames(self,lista): 
    for i in lista:
        Frames.frame[i] = True 
  def DesativaFrame(self,numero): Frames.frame[numero] = False
  def DesativaFrames(self,lista): 
    for i in lista:
        Frames.frame[i] = False
  def EstadoFrame(self,numero): return Frames.frame[numero]
  def MouseDentro(self,frame):
      if frame == 0 and Frames().EstadoFrame(0): return True
      elif frame == 1 and Frames().EstadoFrame(1) and Calculo().MouseIn(width/2-440,(height-50)/2-220,880,440): return True
      
  #Funcao Visualizacao
  def Mostrar(self):
    background(0,0,0)
    if Frames.frame[0]: Frames.frame_animacao_inicial.Mostrar()
    if Frames.frame[1]: Frames.frame_cliente.Mostrar()
    if Frames.frame[2]: Frames.frame_servidor.Mostrar()
      