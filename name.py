import random
import os
import time, sys
import vlc


from gtts import gTTS
def rand_int(m,r):
    return (random.randint(m,r))
v = ['a','e','i','o','u']
a =['b' ,"c" ,"d", 'f',"g" ,"h" ,"j" ,"k" ,"l" ,"m","n","p" ,"q","r","s","t" ,"u","v" ,"w" ,"x" ,"y" ,"z"]
print(len(a))


for i in range(0,1000):
    v_r = rand_int(2,3)
    vo =[]
    for i in range(0,v_r):
        vo.append(v[rand_int(0,4)])
    for i in range(0,6-v_r):
        vo.append(a[rand_int(0,20)])
    randomindex = []
    while len(randomindex)!=6:

        randint =rand_int(0,5)
        if randint  not in randomindex:
            randomindex.append(randint)
    print(randomindex)
    word = []
    for i in range(0,6):
        word.append(vo[randomindex[i]])
    print(''.join(word))
    mytext = ''.join(word)

    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("b.mp3")
    player = vlc.MediaPlayer("b.mp3")
    player.play()
    time.sleep(2)
    player.stop()
    # Playing the converted file
