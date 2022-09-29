import string
#Definición del lenguaje
# matr1= ["1","2"]
mat2_1=["8","9"]
mat2_2=["0","1","2"]
periodo=["1","2","3"]
num=["0","1","2","3","4","5","6","7","8","9"]
act=["1","2","3","4","5","6","7","8","9"]
separador="_"
letras=list(string.ascii_uppercase)
punto,p,d,f=".","p","d","f"




def comprobarAutomata(caracteres):
    estadoIni="a"
    estadoFin="z"
    estado=estadoIni
    for i in range (0,len(caracteres)):
        dato=caracteres[i]
        if estado=="a":
            if dato=="1":
                estado="b"
            elif dato=="2":
                estado="c"
            else:
                return False
        elif estado=="b":
            band=False
            for x in mat2_1:
                if dato==x:
                    estado="d"
                    band=True
            if band==False:
                return False
        elif estado=="c":
            band=False
            for x in mat2_2:
                if dato==x:
                    estado="d"
                    band=True
            if band==False:
                return False
        elif estado=="d":
            band=False
            for x in periodo:
                if dato==x:
                    estado="e"
                    band=True
            if band==False:
                return False
        elif estado=="e":
            band=False
            for x in num:
                if dato==x:
                    estado="f"
                    band=True
            if band==False:
                return False
        elif estado=="f":
            band=False
            for x in num:
                if dato==x:
                    estado="g"
                    band=True
            if band==False:
                return False
        elif estado=="g":
            band=False
            for x in num:
                if dato==x:
                    estado="h"
                    band=True
            if band==False:
                return False
        elif estado=="h":
            if dato==separador:
                estado="i"
            else:
                return False
        elif estado=="i":
            band=False
            for x in letras:
                if dato==x:
                    estado="j"
                    band=True
            if band==False:
                return False
        elif estado=="j":
            band=False
            for x in letras:
                if dato==x:
                    estado="k"
                    band=True
            if band==False:
                return False
        elif estado=="k":
            band=False
            for x in letras:
                if dato==x:
                    estado="m"
                    band=True
            if band==False:
                return False
        elif estado=="m":
            band=False
            for x in letras:
                if dato==x:
                    estado="m"
                    band=True
            if band==False:
                if dato==separador:
                    estado="n"
                else:
                    return False
        elif estado=="n":
            band=False
            for x in letras:
                if dato==x:
                    estado="l"
                    band=True
            if band==False:
                return False
        elif estado=="l":
            band=False
            for x in letras:
                if dato==x:
                    estado="o"
                    band=True
            if band==False:
                return False
        elif estado=="o":
            band=False
            for x in letras:
                if dato==x:
                    estado="p"
                    band=True
            if band==False:
                return False
        elif estado=="p":
            band=False
            for x in letras:
                if dato==x:
                    estado="p"
                    band=True
            if band==False:
                if dato==separador:
                    estado="q"
                else:
                    return False
        elif estado=="q":
            if dato=="C":
                estado="r"
            else:
                return False
        elif estado=="r":
            band = False
            for x in periodo:
                if dato==x:
                    estado="s"
                    band=True
            if band==False:
                return False
        elif estado=="s":
            if dato == separador:
                estado="t"
            else:
                return False
        elif estado=="t":
            if dato=="A":
                estado="u"
            else:
                return False
        elif estado=="u":
            band = False
            for x in act:
                if dato==x:
                    estado="v"
                    band=True
            if band==False:
                return False
        elif estado=="v":
            if dato== punto:
                estado="w"
            else:
                return False
        elif estado=="w":
            if dato == p :
                estado="x"
            else:
                return False
        elif estado=="x":
            if dato == d :
                estado="y"
            else:
                return False  
        elif estado=="y":
            if dato == f :
                estado="z"
            else:
                return False
        else:
            estado="False"
            return False
        
    if estado==estadoFin:
        return True


def main():
    # print("Letras:",letras)
    # automata=Automata("203426_PADILLA_GUTIERREZ_C1_A5.pdf")
    # cadena="203426_PADILLA_GUTIERREZ_C1_A5.pdf"
    # cadena="203"
    cadena= input("Cadena a analizar:") 
    caracteres=list(cadena)
    result=comprobarAutomata(caracteres)
    if result:
        print("Cadena aceptada")
    else:
        print("Cadena NOOO aceptada")



if __name__ == "__main__":
    main()