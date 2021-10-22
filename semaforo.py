import threading
import time

class TenedorFilosofo(threading.Thread):
    def __init__(self, tenedores, filosofosNum):
        threading.Thread.__init__(self)
        self.tenedores = tenedores
        self.filosofosNum = filosofosNum
        self.datoTemporal =  self.filosofosNum  % 5
   
    def hilosFilosofos(self):
        while True:
            print("Filosofo iniciando", self.filosofosNum)
            time.sleep(2)
            print("Filosofo ", self.filosofosNum, "pasando tenedor del lado izquierdo")
            self.tenedores[self.filosofosNum].acquire()
            time.sleep(2)
            self.tenedores[self.datoTemporal].release()
            print("Filosofo ", self.filosofosNum, "recoge tenedor del lado derecho", "mostrando dato temporal : ", self.datoTemporal)
            self.tenedores[self.datoTemporal].acquire()
            time.sleep(2)
            self.tenedores[self.datoTemporal].release()
            print("Filosofo ", self.filosofosNum, "libre derecho")
            self.tenedores[self.datoTemporal].acquire()
            time.sleep(2)
            self.tenedores[self.datoTemporal].release()
            print("Filosofo ", self.filosofosNum, "libre izquierdo")
            self.tenedores[self.filosofosNum].acquire()
            time.sleep(2)
            self.tenedores[self.datoTemporal].release()
            
   
    def run(self):
        self.hilosFilosofos()


tenedorArray = [1,1,1,1,1]

for i in range(0,5):
    print("for uno: ", i)
    tenedorArray[i] = threading.BoundedSemaphore(1)

for i in range(0,5):
    print("for dos: ", i)
    total = TenedorFilosofo(tenedorArray, i)
    total.start()