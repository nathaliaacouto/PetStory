from ctypes import CDLL, create_string_buffer


class GeradorNfe():
    # servicos: array de strings 
    def gerar_nfe(servico):
        desc_buffer = create_string_buffer(servico[0].encode())
        valor_buffer = create_string_buffer(servico[1].encode())
        python_c_create_nfe(desc_buffer, valor_buffer)

lib_c = 'nfe.so'
try:
    c_functions = CDLL(lib_c)
except:
    print("Ocorreu um erro")

python_c_create_nfe = c_functions.create_nfe
python_c_create_nfe.restype = None