from index import *

class Calculo:
    
    def Dist(self,A=[0,0],B=[0,0]):
        return sqrt(pow(A[0]-B[0],2)+pow(A[1]-B[1],2))
    def MouseIn(self,x0 = 0,y0 = 0,dx = 0,dy = 0):
        if mouseX >= x0 and mouseX <= x0+dx and mouseY >= y0 and mouseY <= y0+dy: return True 
        else: return False
    def MouseInC(self,P = [0,0],raio = 0):
        if sqrt(pow(mouseX - P[0],2) + pow(mouseY - P[1],2)) < raio : return True
        else: return False