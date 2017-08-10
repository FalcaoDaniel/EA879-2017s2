
import time

t = time.time()

import sys
import numpy as np

t0 = time.time()
A = np.random.random( (int(sys.argv[1]), int(sys.argv[1])) )
B = np.random.random( (int(sys.argv[1]), int(sys.argv[1])) )

t1 = time.time()
C = np.dot(A,B)

t2 = time.time()

print "Teste com matriz quadrada de NxN, N=", sys.argv[1]
print "Carregar bibliotecas: ", 1000*(t0-t)
print "Criar matriz: ", 1000*(t1-t0)
print "Processar: ", 1000*(t2-t1)
