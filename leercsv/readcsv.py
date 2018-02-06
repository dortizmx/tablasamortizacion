#-*- coding: utf-8 -*-

import sys
import csv
import os.path
from datetime import *
import locale
import time

def readCSVFile(filename) :
    itemlist = [{}]
    with open(filename) as filesource :
        items = filesource.read().splitlines()
        itemsnumber = len(items)
        print "Numero de Registros en el Archivo"
        x = 0
        for l in items :
            item = {}
            noelements = len(l.split("|"))
            line = l.split("|")
            print noelements
            noelm = 1
            while noelm <= noelements :
                nombre = "Elem" + str(noelm)
                item[nombre] =  line[noelm - 1]
                print item[nombre]
                noelm = noelm + 1




def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush() 

def main(argv) :
    #print "Lectura de archivo CSV"
    if len(sys.argv) == 1 or len(sys.argv) < 2 :
        print "No hay suficientes argumentos"
        print "--help para ayuda de comando"
    else:
        if(sys.argv[1] == '--help'):
            print "-i File input"
            print "-o File output"
            return 0
        filename = sys.argv[1]
        total = 100
        i = 0
        while i < total:
            message = "Starting work"
            if(i >= 30) :
                message = "Work in progress"
            progress(i, total, status=message)
            time.sleep(0.5)  # emulating long-playing job
            i += 1
        #readCSVFile(filename)
        print ("")
        
if __name__ == "__main__" :
    main(sys.argv)


