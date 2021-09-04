from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade, soma, num1, num2):
    velho=(idade+40)
    nasc=(2021-idade)
    contanome=(len(nome))
    add=num1+num2
    mult=num1*num2
    div=num1/num2
    subt=num1-num2
    return HttpResponse('<body BGCOLOR="#000000" text="#ffff00">'
                        '<h1>Olá {} com {} anos, você nasceu em {}? <br><br>'
                        'Se sim você já fez aniversário, se não você então '
                        'nasceu em {} e ainda vai fazer aniversário este ano '
                        'não é mesmo? <br><br>Oba não esqueça de me convidar '
                        'para a próxima festa! </h1><br><p><h2>Seu nome '
                        'tem {} letras?</h2></p> <hr size=5 width=100% align=center>'
                        '<br>A Soma de {} + {} = {}<br>'
                        '<br>A Subtração de {} - {} = {}<br>'
                        '<br>A Multiplicação de {} x {} = {}<br>'
                        '<br>A Divisão de {} / {} = {}'
                        '<br> '
                        '<hr width=100% noshade>'
                        '<br><a href="http://www.usp.br/">Universidade de São Paulo</a>'
                        '<br><IMG WIDTH=900 HEIGHT=600 SRC="http://www.fundosanimais.com/Imagens/imagens-lobos.jpg">'
                        '</body>'.format(nome, idade, nasc, nasc-1, contanome, num1, num2, add, num1, num2,subt,num1,num2,mult,num1,num2,div))
