"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr
class blk(gr.sync_block ):
	def __init__( self ) : # only default arguments here
		gr.sync_block.__init__ (
			self ,
			name ="e_Diff2" , # will show up in GRC
			in_sig =[ np.float32 ],
			out_sig =[ np.float32 ]
		)
		self.anterior = 0
	def work(self , input_items , output_items ):
		x = input_items[0]  # Senal de entrada
		y = output_items[0]  # Senal diferenciada
		N = len(x)

        # Calcular la diferencia entre valores consecutivos
		y[0] = x[0] - self.anterior  # Diferencia con el valor anterior
		y[1:] = np.diff(x)  # Diferencia entre valores consecutivos de la senal

        # Actualizar el valor anterior para el siguiente bloque de procesamiento
		self.anterior = x[-1]
		
		return len(y)
