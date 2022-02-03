
#1-ое решение



def rearrange(s):
    string = s.split()
    numbers = []
    for i in range(20):
        numbers.append(str(i))
    # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']

    copy_string = string * 1  # создали копию списка от входной строки

    for word in string:
        for i in range(len(word)):
            if word[i] in numbers:
                pos = int(word[i])
                new_word = word[:i] + word[i + 1:]
                copy_string[pos - 1] = new_word

    return ' '.join(copy_string)

print(rearrange('th3e 2is I1t t4est'))



#2 Проверка условия




def doesBrickFit(a,b,c,w,h):
    gran1 = a*b
    gran2 = a*c
    otv = w*h

    if (gran1 <= otv and (( a<=h and b <= w ) or (a <= w and b <= h))) or (gran2 <= otv and (( a<=h and c <= w ) or (a <= w and c <= h))):
        return True
    else:
        return False

print(doesBrickFit(1,2,1,1,1))


#3 Не решил до конца

#Хорда меньше радиуса одной окружности. Если х радиус, то хорда**2 = х**2 * (2 - sqrt(2)).

def SpiderVsFly(s,f):
    #Переход между радиалами
    answer = []
    sradian = s[0] #положение
    scircle = int(s[1])
    fradian = f[0]
    fcircle = int(f[1])
    Alp = 'ABCDEFGH'

    si = Alp.find(sradian)
    fi = Alp.find(fradian)

    kmin = kright = kleft = 0
    Left = Right = False
    posFly = fi
    posSpider = si
    while Alp[posFly] != Alp[posSpider]: #прогон вправо
        posSpider = (si+1)%8
        kright += 1

    posSpider = si
    while Alp[posFly] != Alp[posSpider]: #прогон влево
        posSpider = si-1
        kleft += 1
    if kleft < kright:
        Left = True
        kmin = kleft
    else:
        Right = True
        kmin = kright

    #Поиск минимального пути

    if kmin < 3:
        #паук доходит до одинакового круга с мухой и переходит
        while fcircle != scircle:
            answer.append(str(sradian)+str(scircle-1))
            scircle -= 1
        if Right:
            while Alp[si] != Alp[fi]:
                answer.append(Alp[(si+1)%8]+str(fcircle))
                si += 1

        if Left:
            while Alp[si] != Alp[fi]:
                answer.append(Alp[si-1]+str(fcircle))
                si -= 1
    # else:
    #     #паук спускается до 1 круга и по центральному кругу переходит на радиал, в котором муха.
    #     if Right:
    #     if Left:
    return answer

# print(SpiderVsFly('A4','C1'))



