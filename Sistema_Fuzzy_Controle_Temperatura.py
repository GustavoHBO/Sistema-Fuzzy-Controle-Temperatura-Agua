#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

GRAVIDADE = 10
RAIO = 2
TEMPERATURA_INICIAL_AGUA = 35
TEMPERATURA_AGUA_QUENTE = 40
TEMPERATURA_AGUA_FRIA = 10
TEMPERATURA_DESEJADA = 25
ALTURA_MAXIMA_AGUA = 2
ALTURA_INICIAL_AGUA = 1
VAZAO_MAXIMA_AGUA_QUENTE = 1
VAZAO_MAXIMA_AGUA_FRIA = 1


def temp_saida(temperatura_medida, vazao_saida, vazao_agua_quente, vazao_agua_fria, altura_agua, tempo_de_vazao):
    return ((temperatura_medida*altura_agua*math.pi*(RAIO**2))+(TEMPERATURA_AGUA_QUENTE*vazao_agua_quente*tempo_de_vazao)+(TEMPERATURA_AGUA_FRIA*vazao_agua_fria*tempo_de_vazao))/((altura_agua*math.pi*RAIO**2)+(vazao_agua_quente*tempo_de_vazao)+(vazao_agua_fria*tempo_de_vazao))

def vazao_saida(altura_agua):
    return (0.002)*math.sqrt(2*GRAVIDADE*altura_agua)

def altura_agua(altura_agua_medida, vazao_agua_quente, vazao_agua_fria, vazao_saida, tempo_vazao):
    return ((altura_agua_medida+vazao_agua_quente+vazao_agua_fria-vazao_saida)*tempo_vazao)/(math.pi*(RAIO**2))

def main():
    altura = altura_agua(ALTURA_INICIAL_AGUA, 1, 1, vazao_saida(ALTURA_INICIAL_AGUA), 1)
    vazao = vazao_saida(altura)
    temperatura = temp_saida(TEMPERATURA_INICIAL_AGUA, vazao, 1, 1, altura, 1)
    print "Altura da Água: ", altura
    print "Vazão da Água: ", vazao
    print "Temperatura da Água: ", temperatura

main()