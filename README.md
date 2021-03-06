![Banner PetStory (1)](https://user-images.githubusercontent.com/79584703/134817940-5dd284f0-91ce-41e5-a89a-5316769ce6cc.png)
# Pet Story 

Criado por estudantes do CESAR School, o PetStory surgiu para auxiliar na comunicação entre as áreas de balcão e a tosa dos Pet Shops. <br>
Trabalhamos com uma loja parceira na região de Recife, PE. Atualmente, o sistema ainda está em fase de prototipação. <br>

## Como instalar o ambiente para o projeto
Clonar o repositório
```shell
git clone https://github.com/nathaliaacouto/PetStory.git
```

Criar e ativar uma virtualenv no diretório raiz da aplicação.
```shell
python -m venv venv
```

No diretorio raiz da aplicação, ativar a virtualenv (Windows Powershell)
```shell
.\venv\Scripts\Activate.ps1
```

Para o Git bash/Terminais Unix
```shell
source ./venv/bin/activate
```

:warning: Se a execução de scripts estiver desabilitada na sua máquina, deverá executar um comando no Powershell para habilitá-los
```shell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

:warning: É recomendável atualizar o pip e o setuptools da virtualenv para fazer corretamente o build das dependências
```shell
pip install --upgrade pip
pip install --upgrade setuptools
```

Instalar todas as dependências do projeto com o pip
```shell
pip install -r requirements.txt
```

## Como iniciar o servidor local
Caso for a primeira vez iniciando o servidor local para o projeto, siga os seguintes passos:
```shell
(venv) flask shell
>>> db
>>> db.create_all()
>>> exit()
```

Prossiga com a inicialização do servidor local com o seguinte comando:
```shell
(venv) flask run
```

## Página dos integrantes no github
<ul>
🔸 <a target="_blank" href="https://github.com/lucasborges">Lucas Borges</a><br>
🔸 <a target="_blank" href="https://github.com/lucasLBF">Lucas Fernandes</a><br>
🔸 <a target="_blank" href="https://github.com/Matheus-F-M">Matheus Mendonça</a><br>
🔸 <a target="_blank" href="https://github.com/nathaliaacouto">Nathália Couto</a>
</ul>
