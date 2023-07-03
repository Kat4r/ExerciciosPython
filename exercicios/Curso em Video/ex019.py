import math
ang = float(input('digite um valor qualquer: '))
rad = math.radians(ang)
print('{} de angulo tem um;\n seno de {:.3f} \n cosseno de {:.3f}\n tangente de {:.3f} '.format(ang,math.sin(rad),math.cos(rad),math.tan(rad)))
