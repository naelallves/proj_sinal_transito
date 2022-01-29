from math import floor
import math
from os import truncate
from pdb import post_mortem
from random import shuffle
from tabnanny import check
from django.shortcuts import redirect, render
from django.http import HttpResponse

from app_quis.models import Alternativa, Pergunta, RelPerguntaAlternativa

def view_obj(obj):
    strObj = ""
    for i in obj:
        strObj += str(i).replace(", '", ", <br>'")
        strObj += "<br><br>"
    # return str(obj).replace('}, {', '}, <br>{')
    return strObj

def index(request):
    data = dict()
    list_perg = list()
    perguntas = Pergunta.objects.all()
    perguntas_ids = list(map(lambda x: x.id, perguntas))
    shuffle(perguntas_ids)
    perguntas_ids = perguntas_ids[0:10]
    count = 1
    for idx, id_p in enumerate(perguntas_ids):
        perg = perguntas.get(pk=id_p)
        alterns_ids = list(RelPerguntaAlternativa.objects.filter(id_pergunta=perg.id).values_list('id_alternativa', flat=True))
        alterns = list(Alternativa.objects.filter(id__in=alterns_ids))
        shuffle(alterns)
        if len(alterns_ids)>0:
            obj = {
                'pergunta': perg,
                'alternativas': alterns,
                'index': count
            }
            list_perg.append(obj)
            count += 1
    data['questoes'] = list_perg[0:30]
    
    # return HttpResponse(view_obj(list_perg))

    return render(request, 'app_quis/index.html', data)

def enviaSimulado(request):
    if request.method == 'POST':
        '''if request.POST.get('name') != "" and request.POST.get('email') != "" and request.POST.get('subject') != "" and request.POST.get('message') != "":
            blog = Blog.objects.filter(id=request.POST.get('id_blog')).first()
            contact = Contact()
            contact.blog_id = blog
            contact.name = request.POST.get('name')
            contact.email = request.POST.get('email')
            contact.subject = request.POST.get('subject')
            contact.message = request.POST.get('message')
            contact.save()

            return redirect('blog_index')
        return HttpResponse("Você não preencheu algum campo 🤔")'''
        data = dict()
        list_keys = list(request.POST.dict().keys())
        list_vals = list(request.POST.dict().values())
        qst_resp = []
        gabarito = []

        for i, key in enumerate(list_keys):
            if('perg' in key):
                qst_resp.append({'id_pergunta': str(list_vals[i])})
            elif('resp' in key):
                qst_resp[int(key[-1])-1]['id_alternativa'] = list_vals[i]
        
        count = 1
        resultado = {'certas': 0, 'erradas': 0}
        for resposta in qst_resp:
            relPerg = RelPerguntaAlternativa.objects.filter(id_pergunta=resposta['id_pergunta'])
            relAltern = relPerg.get(id_alternativa=resposta['id_alternativa'])
            relAltCerta = relPerg.get(certa=True)

            pergunta = relPerg.first().id_pergunta
            alternativa = relAltern.id_alternativa
            alt_certa = relAltCerta.id_alternativa
            gabarito.append({
                'pergunta': pergunta.enunciado,
                'alternativa': alternativa.conteudo,
                'alter_certa': alt_certa.conteudo,
                'check': relAltern.certa,
                'index': count
            })
            count += 1

            if relAltern.certa:
                resultado['certas'] += 1
                continue
            resultado['erradas'] += 1
        
        resultado['porcento'] = math.trunc(resultado['certas'] * 100 / len(qst_resp))
        
        data['gabarito'] = gabarito
        data['resultado'] = resultado
        # return HttpResponse(view_obj(data['resultado']['porcento']))
        
        return render(request, 'app_quis/resultado.html', data)
    return HttpResponse("Não é métofo post.")
