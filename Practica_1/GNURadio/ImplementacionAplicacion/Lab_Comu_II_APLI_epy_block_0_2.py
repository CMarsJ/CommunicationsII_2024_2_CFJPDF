"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block ):
    def __init__ ( self ) : # only default arguments here
        gr.sync_block.__init__ (
        self ,
        name ="e_Acum2", # will show up in GRC
        in_sig =[ np.float32 ],
        out_sig =[ np.float32 ])
        self.acumulado_anterior = 0  # Para almacenar el valor acumulado hasta el momento

    def work(self, input_items, output_items):
        x = input_items[0]  # Senal de entrada
        y = output_items[0]  # Senal acumulada
        N = len(x)

        # Calcular el acumulado, continuando desde el valor acumulado anterior
        y[:] = (np.cumsum(x) + self.acumulado_anterior) 
        # Guardar el valor acumulado para el siguiente bloque
        self.acumulado_anterior = y[N-1]  # El ultimo valor acumulado se guarda

        return len(y)
#    def work (self , input_items , output_items ):
#        x = input_items[0] # Senial de entrada .
#        y0 = output_items[0] # Senial acumulada
#        y0[:] = np.cumsum(x)
        #y0 [:] = len(y0)
#        return len(y0)