#-------------------------------------------------------------------------------#
# Ola,                                                                          #
# Eu sou Faruk, e esse eh o codigo do UTkeys                                    #
# Um software feito para gestao de emprestimos de chaves na UTFPR               #
# A praticidade dele se baseia a utilizacao de QRcodes nos crachas e nas chaves #
#-------------------------------------------------------------------------------#
# Versao: 0.3 (21/01/2017) . Por Faruk Hammoud, 2016.                           #
# Compilado em Processing 3.2.3 (by Processing Foundation) - Python Mode        #
# Distribuicao Livre                                                            #
# Suporte 24/7 : farukhammoud@gmail.com                                         #
#-------------------------------------------------------------------------------#
#Importa bibliotecas 
add_library('video')
add_library('qrcodeprocessing')
add_library('net')
add_library('serial')
#Importa demais modulos do programa
from index import *
from interface import *

web_cam = Camera() 
decoder = Decoder(this)
UTCliente = 0 #chuncho
UTServidor = 0 #chuncho
dados_de_comunicacao = 0 #chuncho
def stop():
    Interface().MudaString('Salvando dados ...')
    Frames().Mostrar()
    Data().SalvaDadosDeComunicacao()
def setup():
    fullScreen()
    frameRate(20)
    Data().ObtemDadosDeComunicacao()
    global dados_de_comunicacao
    global UTServidor
    UTServidor = Server(this,Data().porta)
    global UTCliente
    UTCliente = Client(this,Data().ip,Data().porta) 
    
    Tarefas().Tarefa('Ativa Frame Animacao Inicial')
    #Tarefas().Tarefa('Pula Inicio')
    Tarefas().AlteraTarefaLetra('Pula Inicio',' ')
    Tarefas().AlteraTarefaCodigo('Processa Scroll Up','SCROLLUP')
    Tarefas().AlteraTarefaCodigo('Processa Scroll Down','SCROLLDOWN')
    global mus_ini
    mus_ini = SoundFile(this,"Legiao Urbana - Que pais e esse.mp3")
    global img
    cameras = Capture.list()
    if len(cameras) == 0:
        println('Nao ha cameras sendo detectadas.')
        exit()
    else:
        println('Cameras instaladas:')
        for i in range(len(cameras)):
            println(cameras[i])
    cam = Capture(this,cameras[1])
    if cam.available(): println('Disponivel')
    else: println('Nao disponivel') 
    cam.start()     
    web_cam.InstalaCamera(cam)
    web_cam.Capta()
    #mus_ini.play()
    Data().ObtemContas()
def draw():
    Frames().Mostrar()
       