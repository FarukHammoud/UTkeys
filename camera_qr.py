add_library('qrcodeprocessing')
add_library('video')
import __main__
class QR:
    em_execucao = False
    codigo_lido = 'none'
    def RetornaEstado(self): return QR.em_execucao    
    def Decodifica(self,img = loadImage('FARUK HAMMOUD.png')):
        if not QR.em_execucao:
            QR.em_execucao = True
            __main__.decoder.decodeImage(img)
    def MudaCodigoLido(self,novo_codigo_lido):
        QR.codigo_lido = novo_codigo_lido
    def RetornaCodigoLido(self): return QR.codigo_lido
    def DesativaExecucao(self): QR.em_execucao = False   
    def CaptaCodigo(self):
        statusMsg = __main__.decoder.getDecodedString() 
        QR().DesativaExecucao()
        QR().MudaCodigoLido(statusMsg)
        println('.'+statusMsg+'.')       
class Camera:
    #Criando Objetos 
    def InstalaCamera(self,cam):
        self.cam = cam
        self.img = PImage()
    def Capta(self):
        if self.cam.available(): 
            self.cam.read()
            self.img = self.cam
        else:
            print('nao disponivel')    
    def Imagem(self): return self.img     
            
        
    
        
  