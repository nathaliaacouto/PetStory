from ctypes import c_char_p, c_int, POINTER, cdll
import os

# servicos: array de strings 
# def gerar_nfe(tamanho, servicos):
#     try:
#         integration_dir = os.path.abspath(os.path.dirname(__file__))
#         lib_path = os.path.join(integration_dir, "nfe.so")
#         c_functions = cdll.LoadLibrary(lib_path)
#         print("Arquivo em C carregado com sucesso")
#         python_c_create_nfe = c_functions.create_nfe
#         python_c_create_nfe.argtypes = [c_int, POINTER(c_char_p)]
#         python_c_create_nfe.restype = None
#         tamanho_c = c_int(tamanho)
#         servicos_c = (c_char_p * tamanho)(*servicos)
#         print("chamando funcao em C...")
#         python_c_create_nfe(tamanho_c, servicos_c)
#         print("funcao em C chamada")
#     except:
#         print("Ocorreu um erro")

def gerar_nfe():
    try:
        integration_dir = os.path.abspath(os.path.dirname(__file__))
        lib_path = os.path.join(integration_dir, "nfe.so")
        c_functions = cdll.LoadLibrary(lib_path)
        print("Arquivo em C carregado com sucesso")
        python_c_create_nfe = c_functions.create_nfe_2
        python_c_create_nfe.restype = None
        print("chamando funcao em C...")
        python_c_create_nfe()
        print("funcao em C chamada")
    except:
        print("Ocorreu um erro")