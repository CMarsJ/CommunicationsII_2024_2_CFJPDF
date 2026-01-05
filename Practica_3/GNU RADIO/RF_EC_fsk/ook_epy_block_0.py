import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a RF VCO and works as following: ….."""

    def __init__(self, fc=128000, samp_rate=320000):  #Declaracion del bloque
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   #Nombre del Bloque
            in_sig=[np.float32, np.float32], #Entradas
            out_sig=[np.float32] #Salidas
        )
        self.fc = fc #Frecuencia portadora defaul
        self.samp_rate = samp_rate #samp_rate defaul
        self.n_m=0 #Declaraciones iniciales

    def work(self, input_items, output_items): #Cuerpo del trabajo
        A=input_items[0] #Amplitud
        Q=input_items[1] #Fase
        y=output_items[0] #Salida
        N=len(A) #Tamano de amplitud
        n=np.linspace(self.n_m,self.n_m+N-1,N) #Creacion de puntos entre la declaraciones iniciales y las delacaraciones + el tamano menos 1 (Este es por que python empieza en 0) con un espaciado de N
        self.n_m += N #Sumatoria de N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q) #Modulacion 
        return len(output_items[0])


