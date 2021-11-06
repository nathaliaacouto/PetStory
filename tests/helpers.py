from app.controllers import ClienteController, PetController

def cadastrar_cliente_pet():
    cliente_controller = ClienteController()
    pet_controller = PetController()
    cliente = cliente_controller.create_cliente({
        "nome": "Lucas",
        "telefone": "12345678",
        "cpf": "14785236987",
        "cep": "32147896", 
        "endereco": "Rua Exemplo, 123",
        "email": "lucas@gmail.com"
    })
    cliente_controller.add_cliente(cliente)

    pet = pet_controller.create_pet({
        "nome": "Aylla",
        "raca": "Shihtzu",
        "pelagem": "Branca com marrom",
        "obito": False,
    })
    pet_controller.add_pet(pet, cliente)
    return cliente, pet
