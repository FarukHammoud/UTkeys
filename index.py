#CARREGA MODULOS ESTATICOS
from math import *
add_library('sound')


#CARREGA MODULOS DINAMICOS
def Calculo():
    import calculo
    return calculo.Calculo()
def Data():
    import data_
    return data_.Data()
def Tarefas():
    import tarefas
    return tarefas.Tarefas()
def Frames():
    import frames
    return frames.Frames()
def Interface():
    import interface
    return interface.Interface()
def Papel():
    import objetos
    return objetos.Papel()
def Ponto3D():
    import biblioteca
    return biblioteca.Ponto3D()    
def Cores():
    import biblioteca
    return biblioteca.Cores()
def TextBox(x,y):
    import biblioteca
    return biblioteca.TextBox(x,y)
def ListaLateral(x,y):
    import biblioteca
    return biblioteca.ListaLateral(x,y)
def AnimacaoDeEspera(x,y):
    import biblioteca
    return biblioteca.AnimacaoDeEspera(x,y)
def CheckBox(x,y,texto = '',valor = False):
    import biblioteca
    return biblioteca.CheckBox(x,y,texto,valor)
def Botao(tipo,x,y,link_tarefa_a,link_tarefa_b):
    import biblioteca
    return biblioteca.Botao(tipo,x,y,link_tarefa_a,link_tarefa_b)
def Projeto():
    import objetos
    return objetos.Projeto()
def Camera():
    import camera_qr
    return camera_qr.Camera()
def QR():
    import camera_qr
    return camera_qr.QR()
def LeitorQR(x,y):
    import biblioteca
    return biblioteca.LeitorQR(x,y)
def Comunicacao():
    import comunicacao
    return comunicacao.Comunicacao()    

    
    
    
    