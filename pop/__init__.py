import time
import sys
from playsound3 import playsound

#NÃO FINALIZADO, CÓPIA DO ROCK (POR ENQUANTO)
def pop():
    # TOCA A MÚSICA ESCOLHIDA
    time.sleep(2)
    print('\nMúsica = _____ _____')
    playsound('sons/1st.mp3', block=False)
    time.sleep(5)

    #PERGUNTA QUAL É A MÚSICA E ANALISA A RESPOSTA
    print('Baseado neste pequeno techo de que música se trata ?')
    x=3
    y=0
    while x != 0:
        trem = input().upper()
        if trem == 'CRAZY TRAIN':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', trem, 'meus parabéns!!!')
            y=y+1
            break
        elif trem == 'REPETIR':
            playsound('sons/1st.mp3', block=False)
            continue
        elif trem == 'DICA':
            print('CR_Z_ __A__')

        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y ,'de 9 músicas')
                time.sleep(1)
                sys.exit()

    print('\nSegunda música')
    time.sleep(2)
    playsound('sons/2st.mp3', block=False)
    print('\nMúsica = _____ ___ _______')
    time.sleep(5)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        dinheiro = input().upper()
        if dinheiro == 'MONEY FOR NOTHING':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', dinheiro, 'meus parabéns!!!')
            y = y + 1
            break
        elif dinheiro == 'REPETIR':
            playsound('sons/2st.mp3', block=False)
            continue
        elif dinheiro == 'DICA':
            print('__NE_ F__ N_T____')

        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 9 músicas')
                time.sleep(1)
                sys.exit()

    print('\nTerceira música')
    time.sleep(2)
    playsound('sons/3st.mp3', block=False)
    print('\nMúsica = _____ _______')
    time.sleep(4)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        areia = input().upper()
        if areia == 'ENTER SANDMAN':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', areia, 'meus parabéns!!!')
            y = y + 1
            break
        elif areia == 'REPETIR':
            playsound('sons/3st.mp3', block=False)
            continue
        elif areia == 'DICA':
            print('E___R ___MA_')

        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 9 músicas')
                time.sleep(1)
                sys.exit()

    print('\nQuarta música')
    time.sleep(2)
    playsound('sons/4st.mp3', block=False)
    print('\nMúsica = _______ __ _____')
    time.sleep(4)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        nado = input().upper()
        if nado == 'SULTANS OF SWING':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', nado, 'meus parabéns!!!')
            y = y + 1
            break
        elif nado == 'REPETIR':
            playsound('sons/4st.mp3', block=False)
            continue
        elif nado == 'DICA':
            print('S___A__ _F _W_I__')

        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 9 músicas')
                time.sleep(1)
                sys.exit()

    print('\nQuinta música')
    time.sleep(2)
    playsound('sons/5st.mp3', block=False)
    print('\nMúsica = ___')
    time.sleep(5)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        nip = input().upper()
        if nip == 'NIB':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', nip, 'meus parabéns!!!')
            y = y + 1
            break
        elif nip == 'REPETIR':
            playsound('sons/5st.mp3', block=False)
            continue
        elif nip == 'DICA':
            print('__B')

        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 9 músicas')
                time.sleep(1)
                sys.exit()

    print('\nSexta música')
    time.sleep(2)
    playsound('sons/6st.mp3', block=False)
    print('\nMúsica = ______ ___________')
    time.sleep(4)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        sagrado = input().upper()
        if sagrado == 'UNHOLY CONFESSIONS':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', sagrado, 'meus parabéns!!!')
            y = y + 1
            break
        elif sagrado == 'REPETIR':
            playsound('sons/6st.mp3', block=False)
            continue
        elif sagrado == 'DICA':
            print('U_HO__ CO___S_I___')


        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 9 músicas')
                time.sleep(1)
                sys.exit()

    print('\nSétima música')
    time.sleep(2)
    playsound('sons/7st.mp3', block=False)
    print('\nMúsica = _____ __ __ _____')
    time.sleep(5)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        nip = input().upper()
        if nip == 'SHAPE OF MY HEART':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', nip, 'meus parabéns!!!')
            y = y + 1
            break
        elif nip == 'REPETIR':
            playsound('sons/7st.mp3', block=False)
            continue
        elif nip == 'DICA':
            print('SH___ O_ M_ __ART')


        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 12 músicas')
                time.sleep(1)
                sys.exit()

    print('\nOitava música')
    time.sleep(2)
    playsound('sons/8st.mp3', block=False)
    print('\nMúsica = ___')
    time.sleep(6)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        dois = input().upper()
        if dois == 'ONE':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', dois, 'meus parabéns!!!')
            y = y + 1
            break
        elif dois == 'REPETIR':
            playsound('sons/8st.mp3', block=False)
            continue
        elif dois == 'DICA':
            print('_N_')


        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 12 músicas')
                time.sleep(1)
                sys.exit()

    print('\nNona música')
    time.sleep(2)
    playsound('sons/9st.mp3', block=False)
    print('\nMúsica = _____ __________')
    time.sleep(7)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        fornia = input().upper()
        if fornia == 'HOTEL CALIFORNIA':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', fornia, 'meus parabéns!!!')
            y = y + 1
            break
        elif fornia == 'REPETIR':
            playsound('sons/9st.mp3', block=False)
            continue
        elif fornia == 'DICA':
            print('H__E_ ____FO__IA')


        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 12 músicas')
                time.sleep(1)
                sys.exit()

    print('\nDécima música')
    time.sleep(2)
    playsound('sons/10st.mp3', block=False)
    print('\nMúsica = __ _______')
    time.sleep(9)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        senhor = input().upper()
        if senhor == 'MR CROWLEY':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', senhor, 'meus parabéns!!!')
            y = y + 1
            break
        elif senhor == 'REPETIR':
            playsound('sons/10st.mp3', block=False)
            continue
        elif senhor == 'DICA':
            print('M_ C_____')

        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 12 músicas')
                time.sleep(1)
                sys.exit()

    print('\nDécima primeira música')
    time.sleep(2)
    playsound('sons/11st.mp3', block=False)
    print('\nMúsica = ____ __ ___ ____')
    time.sleep(7)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        senhor = input().upper()
        if senhor == 'HAIL TO THE KING':
            playsound('sons/correct.mp3', block=False)
            print('A resposta é', senhor, 'meus parabéns!!!')
            y = y + 1
            break
        elif senhor == 'REPETIR':
            playsound('sons/11st.mp3', block=False)
            continue
        elif senhor == 'DICA':
            print('H___ __ T_E ___ING')
        else:
            playsound('sons/wrong.mp3', block=False)
            x=x-1
            if x != 0:
                if x == 2:
                    print(f'Você errou, mas ainda tem {x} vidas')
                    break
                elif x == 1:
                    print(f'Você errou, mas ainda tem {x} vida')
                    break
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 12 músicas')
                time.sleep(1)
                sys.exit()

    print('\nUltima Música')
    time.sleep(2)
    playsound('sons/12st.mp3', block=False)
    print('\nMúsica = _____ ______ ___')
    time.sleep(9)
    print('\nBaseado neste pequeno trecho de que música se trata ?')

    while x != 0:
        amor = input().upper()
        if amor == 'STILL LOVING YOU':
            playsound('sons/won.mp3', block=False)
            print('A resposta é', amor, 'meus parabéns!!!')
            y = y + 1
            break
        elif amor == 'REPETIR':
            playsound('sons/12st.mp3', block=False)
            continue
        elif amor == 'DICA':
            print('S_T___ L_____ Y__')
        else:
            playsound('sons/won.mp3', block=False)
            x=x-1
            if x == 0:
                playsound('sons/wrong.mp3', block=False)
                print("GAME OVER")
                print('\nVocê acertou', y, 'de 12 músicas')
                time.sleep(1)
                sys.exit()

    print('\nMEUS PARABÉNS VOCÊ SOBREVIVEU ATÉ A ULTIMA MÚSICA!!!')
    time.sleep(1)
