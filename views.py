from django.http import JsonResponse
from.models import Visitante, Entrada, Usuario, Departamento

def salvar_visitante(request):
    if request.method == 'POST':
        nome = request.POST.get('nomeVisitante')
        email = request.POST.get('emailVisitante')
        visitante = Visitante.objects.create(nome=nome, email=email)
        return JsonResponse({'message': 'Visitante salvo com sucesso!'})

def salvar_entrada(request):
    if request.method == 'POST':
        nome = request.POST.get('nomeEntrada')
        hora = request.POST.get('horaEntrada')
        entrada = Entrada.objects.create(nome=nome, hora=hora)
        return JsonResponse({'message': 'Entrada salva com sucesso!'})

def salvar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nomeUsuario')
        email = request.POST.get('emailUsuario')
        usuario = Usuario.objects.create(nome=nome, email=email)
        return JsonResponse({'message': 'Usuário salvo com sucesso!'})

def salvar_departamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nomeDepartamento')
        descricao = request.POST.get('descricaoDepartamento')
        departamento = Departamento.objects.create(nome=nome, descricao=descricao)
        return JsonResponse({'message': 'Departamento salvo com sucesso!'})