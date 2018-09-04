from index import *
import __main__
class Comunicacao:
  def EscreveParaServidor(self,msg):
    __main__.UTCliente.write(msg+'\n')
  def EscreveParaCliente(self,msg):
    __main__.UTServidor.write(msg+'\n')
  def AtualizaListaMensagens(self):
    if __main__.UTCliente.available() > 0:
        mensagens = __main__.UTClient.readString()
        data_0 = split(mensagens, '\n') # Only up to the newline
        for i in range(data_0.length):
            data = split(data_0[i], " ") # Split values into an array
            # Draw line using received coords
            if data.length == 5:
                #use data[0] data[1] etc
                pass
  def AtendeMensagens(self):
      cliente = __main__.UTServidor.available()
      if cliente != None:
          mensagens = cliente.readString()
          vetor_mensagens = split(mensagens,'\n')
          for mensagem in vetor_mensagens:
              partes = matchAll(mensagem,'\[(.*?)\]')
              if partes != None:
                if partes[0][1] == 'Emprestimo':
                    println('opa! emprestimo')
                elif partes[0][1] == 'Devolucao':
                    pass
                elif partes[0][1] == 'Cadastro':
                    pass
                elif partes[0][1] == 'Autorizacao':
                    pass
                elif partes[0][1] == 'Vinculo':
                    pass    
  def ComunicaEmprestimo(self,cracha,chave):
      self.EscreveParaServidor("[Emprestimo]["+cracha+"]["+chave+"]")
      println("Enviando para Servidor: "+"[Emprestimo]["+cracha+"]["+chave+"]")
  def ComunicaDevolucao(self,chave):
      self.EscreveParaServidor("[Devolucao]["+chave+"]")
      println("Enviando para Servidor: "+"[Devolucao]["+chave+"]")
  def ComunicaCadastro(self,nome,categoria,cracha):
      self.EscreveParaServidor("[Cadastro]["+nome+"]["+categoria+"]["+cracha+"]")
      println("Enviando para Servidor: "+"[Cadastro]["+nome+"]["+categoria+"]["+cracha+"]") 
  def ComunicaAutorizacao(self,chave,cracha_autorizado,cracha_autorizando):
      self.EscreveParaServidor("[Autorizacao]["+chave+"]["+cracha_autorizado+"]["+cracha_autorizando+"]")
      println("Enviando para Servidor: [Autorizacao]["+chave+"]["+cracha_autorizado+"]["+cracha_autorizando+"]")     
  def ComunicaVinculo(self,sala,cracha):
      self.EscreveParaServidor("[Vinculo]["+sala+"]["+cracha+"]")
      println("Enviando para Servidor: [Vinculo]["+sala+"]["+cracha+"]")         
  def ComunicaHistorico(self,sala):
      self.EscreveParaServidor("[Historico]["+sala+"]")
      println("Enviando para Servidor: [Historico]["+sala+"]")                           
  def Mostrar(self):
      fill(0,0,0)
      textSize(15)
      text('Conectado a:'+Data().ip+'/'+str(Data().porta),width-250,30)              