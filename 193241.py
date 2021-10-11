import time
import random
import threading

N = 5
TIEMPO_TOTAL = 3

class filosofo(threading.Thread):
    semaforo = threading.Lock() 
    estado_filosofo = [] 
    tenedores = [] 
    count=0

    def __init__(self):
        super().__init__()    
        self.id=filosofo.count 
        filosofo.count+=1 
        filosofo.estado_filosofo.append('PENSANDO') 
        filosofo.tenedores.append(threading.Semaphore(0))
        print("FILOSOFO {0} - PENSANDO".format(self.id))

    def __del__(self):
        print("FILOSOFO {0} - Se para de la mesa".format(self.id)) 

    def pensar(self):
        time.sleep(random.randint(0,5)) 

    def derecha(self,i):
        return (i-1)%N 

    def izquierda(self,i):
        return(i+1)%N 

    def verificar(self,i):
        if filosofo.estado_filosofo[i] == 'HAMBRIENTO' and filosofo.estado_filosofo[self.izquierda(i)] != 'COMIENDO' and filosofo.estado_filosofo[self.derecha(i)] != 'COMIENDO':
            filosofo.estado_filosofo[i]='COMIENDO'
            filosofo.tenedores[i].release()  

    def tomar(self):
        filosofo.semaforo.acquire() 
        filosofo.estado_filosofo[self.id] = 'HAMBRIENTO'
        self.verificar(self.id) 
        filosofo.semaforo.release() 
        filosofo.tenedores[self.id].acquire() 

    def soltar(self):
        filosofo.semaforo.acquire() 
        filosofo.estado_filosofo[self.id] = 'PENSANDO'
        self.verificar(self.izquierda(self.id))
        self.verificar(self.derecha(self.id))
        filosofo.semaforo.release() 

    def comer(self):
        print("FILOSOFO {} COMIENDO".format(self.id))
        time.sleep(2)
        print("FILOSOFO {} TERMINO DE COMER".format(self.id))

    def run(self):
        for i in range(TIEMPO_TOTAL):
            self.pensar() 
            self.tomar() 
            self.comer() 
            self.soltar() 

def main():
    lista=[]
    for i in range(N):
        lista.append(filosofo()) 

    for f in lista:
        f.start() 

    for f in lista:
        f.join() 

if __name__=="__main__":
    main()