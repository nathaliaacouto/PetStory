from app import create_app, db
from app.models import Cliente, Pet, Atendimento, Servico, atendimento_servico

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Cliente': Cliente,
        'Pet': Pet,
        'Atendimento': Atendimento,
        'Servico': Servico,
        'atendimento_servico': atendimento_servico
    }