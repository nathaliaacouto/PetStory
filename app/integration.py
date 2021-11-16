from ctypes import c_char, c_int, cdll
import os

# servicos: array de strings 
def gerar_nfe(tamanho, servicos):
    try:
        integration_dir = os.path.abspath(os.path.dirname(__file__))
        lib_path = os.path.join(integration_dir, "nfe.so")
        c_functions = cdll.LoadLibrary(lib_path)
        print("Arquivo em C carregado com sucesso")
        python_c_create_nfe = c_functions.create_nfe
        python_c_create_nfe.argtypes = [c_int, (((c_char) * 20) * tamanho)]
        python_c_create_nfe.restype = None
        tamanho_c = c_int(tamanho)
        servicos_c = (((c_char) * 20) * tamanho) ()
        i = 0
        for s in servicos:
            servicos_c[i].value = s
            i += 1
        print(servicos_c[0].value)
        print("chamando funcao em C...")
        python_c_create_nfe(tamanho_c, servicos_c)
        print("funcao em C chamada")
    except:
        print("Ocorreu um erro")
