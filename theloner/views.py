from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import choices, SecretUrl, additionalHtml
from http import HTTPStatus
from copy import deepcopy
from json import dumps

urls=SecretUrl.objects.all()

class HttpResponseNoContent(HttpResponse):
    status_code= HTTPStatus.NO_CONTENT

#///////////////UTILITY FUNCTIONS///////////////#
def wordExist(word, checked=False):
    for url in urls:
            if url.secretWord.lower() in word.lower():
                if checked==False:
                    return True
                else:
                    return url.secretWord
    return False


def constructAdditionalHtml(additionalHtmls):
    additionalHtml=[]
    for j in range(len(additionalHtmls)):
        html={
        'tagType':additionalHtmls[j].tagType,
        'tagClasses':additionalHtmls[j].tagClasses,
        'contentInside':additionalHtmls[j].contentInside,
        'insertBefore':additionalHtmls[j].insertBefore,
        }
        additionalHtml.append(html)
    return additionalHtml

def constructContext(secret):
    modelo=SecretUrl.objects.get(secretWord=secret)
    choices=modelo.choices_set.all()
    context={}
    context['timeReveals']=[]
    context['additionalCss']=modelo.additionalCss
    if modelo.cssIsInternalLink==True:
        context['additionalCss']='/static/theloner/css/'+modelo.additionalCss
    context['word']=modelo.secretWord
    if len(choices)>1: 
        context['multiplechoices']= True
    else:
        context['multiplechoices']= False

    #huge adding for additional HTML content

    if modelo.additionalhtml_set.exists():
        additionalHtmls=modelo.additionalhtml_set.all()
        context['additionalHtml']=constructAdditionalHtml(additionalHtmls)


    for i in range(len(choices)):
        context['c'+str(i)]={           #stands for choice[Number]
        'headerCssUrl':choices[i].headerCssUrl,
        'headerClass':choices[i].headerClass,
        'iconClass':choices[i].iconClass,
        'iconSrc':choices[i].iconSrc,
        'realwolfClass':choices[i].realwolfClass,
        'wolfClass':choices[i].wolfClass,
        'wolfText':choices[i].wolfText,
        'choicesClass':choices[i].choicesClass,
        'tellstoryClass':choices[i].tellstoryClass,
        'tellstoryText':choices[i].tellstoryText,
        'choicesClass':choices[i].choicesClass,
        
        }
        context['timeReveals'].append(
            {
            'timeoptionClass':choices[i].timeoptionClass,
            'timeoptionText':choices[i].timeoptionText,
            'timeoptionAnimation':choices[i].timeoptionAnimation,
            })
        if choices[i].headerIsInternalLink==True:
            context['c'+str(i)]['headerCssUrl']= '/static/theloner/header/'+context['c'+str(i)]['headerCssUrl']
        if choices[i].iconIsInternalLink==True:
            context['c'+str(i)]['iconSrc']= '/static/theloner/icon/'+context['c'+str(i)]['iconSrc']

        #this one is going to be large, oh boy...
        if choices[i].additionalhtml_set.exists():
            additionalHtmls=choices[i].additionalhtml_set.all()
            context['c'+str(i)]['additionalHtml']=constructAdditionalHtml(additionalHtmls)
        #didn't end up so large after all


    deepCopy={}
    deepCopy['deepCopy']=dumps(deepcopy(context))
    context.update(deepCopy)
    return context

#///////////////End of Utility Functions///////////////#

# Create your views here.
def index(anything):
    return HttpResponse('hi, I may be testing somethings, dont mind it.')


def searching(request):
    if 'lonerguess' in request.headers:
        word=request.headers.get('lonerguess')
        if wordExist(word):
            word=wordExist(word, checked=True)
            context= constructContext(word)
            return JsonResponse(context)
            #IT WORKS!!
        else:
            return HttpResponseNoContent()

#need to write the context to test my The Loner website            
#done ^^

def loner(request, secret='theloner'):
    context= constructContext(secret)
    return render(request, 'base.html', context=context)