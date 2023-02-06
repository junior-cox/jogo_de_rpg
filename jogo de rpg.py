#jogo de rpg
#voce deve fugi pelo o muro com a escada
import linha
luz=False
vaculhar=False
vasmus=False
grita=True
es=int(0)
while(True):
   linha.linha()
   print('voce esta no terreno de uma casa ')
   print('1 ir para a casa ')
   print('2 vasculha o terreno ')
   print('3 sair do terreno')
   p1=int(input('//'))
   linha.linha()
   if(p1==2):
     if(es==0):
        print('1 voce acha uma escada')
     print('2 voce acha um murro baixo ')
     print('3 deicha pra depoes')
     vaterr=int(input('//'))
     if(vaterr==2):
        if(es==0):
          print('voce nao tem altura ')
        if(es==1):
          print('voce tem altura com a escada')
          print('1 que usar a escada  ')
          print('2 voltar e porcura ')
          fim=int(input('//'))
          if(fim==1):
            print('voce saio do terreno ')
            linha.linha()
            print('v1.0')
            exit()
     if(es==0):
       if(vaterr==1):
          print('1 pega escada')
          print('2 nao pega a escada')
          pega=int(input('//'))
          if(pega==1):
            es=int(1)
   if(p1==1):
     q1=True
     while(q1):
        print('voce esta tentro da casa')
        if(luz==False):
           print('1 ligar a luz ')
        if(luz==True):
           print('1 vasculha a casa')
        print('2 gritar')
        print('3 sair')
        if(vasmus==True):
           print('4 vacular muchila ')
        c1=int(input('//'))
        linha.linha()
        if(luz==False):
          if(c1==1):
            print('a luz foi ligada !!!!!')
            luz=True
            c1=0
            vaculhar=True
        if(luz==True):
          if(vaculhar==True):
             if(c1==1):
              print('voce acha uma muchila ???')
              vasmus=True
        if(grita):
           if(c1==2):
             print('voce grita mais nada acomtese')
             grita=False
        if(vasmus==True):
            if(c1==2):
               print('voce acho uma chave')
        if(c1==3):
           print('voce saiu da casa')
           q1=False
             