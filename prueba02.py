import string
finalState="z"
a=list(string.ascii_uppercase)
states=list(string.ascii_lowercase)
alphabet=[ 
   ['0'],['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9'],['_'],['.'],['p'],['d'],['f'],['c'],['a'],  a] 
transitions=[
#    0     1     2     3     4     5     6     7     8     9    10     11    12    13    14    15    16    17
 [ []   ,["b"],["c"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #0 - a
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["d"],["d"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #1 - b
,[ ["d"],["d"],["d"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #2 - c
,[ []   ,["e"],["e"],["e"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #3 - d
,[ ["f"],["f"],["f"],["f"],["f"],["f"],["f"],["f"],["f"],["f"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #3 - e
,[ ["g"],["g"],["g"],["g"],["g"],["g"],["g"],["g"],["g"],["g"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #5 - f
,[ ["h"],["h"],["h"],["h"],["h"],["h"],["h"],["h"],["h"],["h"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #6 - g
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["i"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #7 - h
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["j"]] #8 - i
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["k"]] #9 - j
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["l"]] #10 - k
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["m"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["l"]] #11 - l
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["n"]] #12 - m
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["o"]] #13 - n
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["p"]] #14 - o
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["q"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["p"]] #15 - p
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["r"],[]   ,[]   ] #16 - q
,[ []   ,["s"],["s"],["s"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #17 - r
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["t"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #18 - s
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["u"],[]   ] #29 - t
,[ []   ,["v"],["v"],["v"],["v"],["v"],["v"],["v"],["v"],["v"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #20 - u
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["w"],[]   ,[]   ,[]   ,[]   ,[]   ,[]   ] #21 - v
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["x"],[]   ,[]   ,[]   ,[]   ,[]   ] #22 - w
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["y"],[]   ,[]   ,[]   ,[]   ] #23 - x
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,["z"],[]   ,[]   ,[]   ] #24 - y
,[ []   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ,[]   ]]#25 - z

def validateChar(simbol):
    index=0
    for aux in alphabet:
        for data in aux:
            if data == simbol:
                return index
        index+=1
    return -1


def validateState(state):
    index=0
    for singleState in states:
        if singleState==state:
            return index
        index+=1
    return -1

def validateWord(sentence):

    state="a"
    accepted=[]

    for char in sentence:
        x=validateState(state)
        y=validateChar(char)
        if x == -1 or y==-1:
            print('No existe estado o simbolo')
            return accepted
        else:
            if len(transitions[x][y]) == 1:
                accepted.append(char)
                state=transitions[x][y][0]
                # print(f'Nuevo estado: {state}')
            else:
                print('No hay transicion valida')
                return accepted
    if state==finalState:
        print('String accepted')
        return accepted

    else:
        print('Not in final state')
        return accepted
    

def main():
    # print(ord(states[0])-96)

    # state= input('Type a state: ')
    # y=validateState(state)
    # print(f'State found with index: {y}')
    sentence='203426_STEVEN_PADILLA_c1_a3.pd'
    word=validateWord(sentence)
    print("".join(word))

    
main()
