import importlib
import modulo2


resultado_soma = modulo2.soma(8, 8)
for i in range(5):
    importlib.reload(modulo2)
