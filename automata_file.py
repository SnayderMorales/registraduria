from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
class Automata: 
    def automata(self, archivo, archivoConsulta):
        simbolos = []
        estados = set()
        transicion = {}
        i = 0
        j = 1
        cadena = ''
        #Armar automata con archivo guardado
        for consul in archivoConsulta:
            cadena +=str(consul)
        cadena += ''
        cadena2 = ''
        for arch in archivo:
            simbolos.append(str(arch))
            estados.add('q'+str(i))
            transicion['q'+str(i)] = {str(arch): {'q'+str(j)}}
            cadena2+=str(arch)
        
            #transiciones.append(transicion)
           #transicion.add('q'+i: {arch: 'q'+j})        
            i = i+1 
            j = j+1
        
        estados.add('q'+str(j-1))
        transicion['q'+str(i)] = {'': {'q'+str(i)}}
        print('Cadena')
        print(cadena)
        print('------------Quintupla-----------------')
        print('Transiciones')
        print(transicion)
        print('Estados')
        print(estados)
        print('Simbolos')
        print(simbolos)
        print('Estado Inicial')
        print('q0')
        print('Estado final')
        print('q'+str(i))
        print('-------------Final de Quintupla----------------')
        nfa = NFA(
    states=estados,
    input_symbols=simbolos,
    transitions=transicion,
    initial_state='q0',
    final_states={'q'+str(i)}
)
        i=0
        j=1
        romper = False
        estadoFinal = {}
        for salto in nfa.transitions:
            print(nfa.transitions[salto])
            if(romper):
                    return 'rejected'
            for valor in nfa.transitions[salto]:
                print(valor)
                if(romper):
                    break
                for val in valor:
                    if(cadena[i]==val):
                        #print(cadena[i] +' = '+val)
                        i = i+1
                        j=j+1
                        estadoFinal = salto
                    else:
                        #print(cadena[i] +' != '+val)
                        print('La cadena no cumple con el automata estado en el '+ salto+ '; Archivo son diferentes')
                        romper = True
                        break
        fin = list(nfa.final_states)
        finalRecorrido = int(estadoFinal.replace('q',''))
        finalEstado = int(str(fin[0]).replace('q',''))      
        if len(cadena)==i and finalEstado-finalRecorrido == 1:
            return 'La cadena cumple con el automata archivos existe'
        else:
            return 'La cadena no cumple con el automata archivos no existe'
        
        