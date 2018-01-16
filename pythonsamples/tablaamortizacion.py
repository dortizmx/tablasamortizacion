#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from datetime import *
from pymongo import MongoClient

def SetMoneda(num, simbolo="$", n_decimales=2):
    """Convierte el numero en un string en formato moneda
    SetMoneda(45924.457, 'RD$', 2) --> 'RD$ 45,924.46'     
    """
    #con abs, nos aseguramos que los dec. sea un positivo.
    n_decimales = abs(n_decimales)
    
    #se redondea a los decimales idicados.
    num = round(num, n_decimales)

    #se divide el entero del decimal y obtenemos los string
    num, dec = str(num).split(".")

    #si el num tiene menos decimales que los que se quieren mostrar,
    #se completan los faltantes con ceros.
    dec += "0" * (n_decimales - len(dec))
    
    #se invierte el num, para facilitar la adicion de comas.
    num = num[::-1]
    
    #se crea una lista con las cifras de miles como elementos.
    l = [num[pos:pos+3][::-1] for pos in range(0,50,3) if (num[pos:pos+3])]
    l.reverse()
    
    #se pasa la lista a string, uniendo sus elementos con comas.
    num = str.join(",", l)
    
    #si el numero es negativo, se quita una coma sobrante.
    try:
        if num[0:2] == "-,":
            num = "-%s" % num[2:]
    except IndexError:
        pass
    
    #si no se especifican decimales, se retorna un numero entero.
    if not n_decimales:
        return "%s %s" % (simbolo, num)
        
    return "%s %s.%s" % (simbolo, num, dec)

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

clear()


def getinteresmensual(tasainteres):
    interes = (tasainteres/100)/12
    return interes

def getAnualidad(meses,valorinicial,tasainteres):
    valorpresente = valorinicial 
    interes = getinteresmensual(tasainteres)
    fac = (1+ interes)**meses
    num = interes *(fac)
    den = (fac)-1
    res = num/den 
    retvalue = valorpresente * res
    return retvalue

def getMontoInteres(montocapital, interes):
    retvalue = montocapital * interes 
    return retvalue

def getMontoAbonoCapital(anualidad, montointeres):
    retvalue = anualidad - montointeres
    return retvalue


def tablaamortizacion(meses,valorinicial,anticipo,tasainteres):
    prm_meses = int(meses)
    vinicial = valorinicial - anticipo
    while (prm_meses > 0):
        anualidad = getAnualidad(prm_meses,vinicial,tasainteres)
        glbinteres = getinteresmensual(tasainteres);
        montointeres = getMontoInteres(vinicial, glbinteres)
        abonocapital = getMontoAbonoCapital(anualidad, montointeres)
        print "-----------------------------------------------------"
        print "No Pago        :       %i" %prm_meses
        prm_meses = prm_meses - 1
        print "Interes mensual:    %% %f" %glbinteres
        print "Monto Inicial  :      %s" %SetMoneda(vinicial,'$', 2)
        print "Pago Anualidad :      %s " %SetMoneda(anualidad, '$', 2)
        print "Pago Interes   :      %s " %SetMoneda(montointeres , '$', 2)
        print "Pago Capital   :      %s " %SetMoneda(abonocapital, '$', 2)
        print "-----------------------------------------------------"
        vinicial = vinicial - abonocapital

def creaTablaAmortizacion() :
    print "************************Tabla de amortizacion******************************"
    meses = float(raw_input("No Meses:"))
    montoprestamo = float(raw_input("Monto del Prestamo :"))
    anticipo = float(raw_input("Anticipo :"))
    tasaint = float(raw_input("Tasa interes :"))
    tablaamortizacion(meses,montoprestamo,anticipo,tasaint)
    opt = raw_input("Presiona enter para salir...")

def creaTablaPagosAdelantados():
    print "************************Tabla de Amortizacion*******************************"
    print "opcion en construccion"
    opt = raw_input("Presiona enter para salir...")


def menu():
    option = 0
    while (option <> "99") :
        clear()
        print "***************************************************************************"
        print " 1) Tabla Amortizacion"
        print " 2) Tabla Amortizacion con pagos adelantados"
        print "99) Salir"
        print "***************************************************************************"
        option = raw_input("numero de opcion :")
        if(option == "1") :
            clear()
            creaTablaAmortizacion()
        if (option == "2") :
            clear()
            creaTablaPagosAdelantados()
    

def main(args):
    clear()
    menu()
    #print "************************Tabla de amortizacion******************************"
    #meses = float(raw_input("No Meses:"))
    #montoprestamo = float(raw_input("Monto del Prestamo :"))
    #anticipo = float(raw_input("Anticipo :"))
    #tasaint = float(raw_input("Tasa interes :"))
    #tablaamortizacion(meses,montoprestamo,anticipo,tasaint)


if __name__ == "__main__":
    main(sys.argv)

