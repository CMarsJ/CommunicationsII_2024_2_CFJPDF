import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a CE VCO or baseband VCO and works as following: ….."""

    def __init__(self,):  #Declaracion del bloque
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32], #Entradas
            out_sig=[np.complex64] #Salidas
        )
        
    def work(self, input_items, output_items):
        A=input_items[0] #Amplitud
        Q=input_items[1] #Fase
        y=output_items[0] #Salida
        N=len(A) #Tamaño amplitud
        y[:]=A*np.exp(1j*Q) #Envolvente compleja
        return len(output_items[0])
