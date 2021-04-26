file = open('script2.txt', 'w')
file.write('ident\n')
step=0.02
i=0
while i<=1:
    angle = step*360
    file.write('torus\n')
    file.write(' '.join(list(map(str, [0,0,150,10,60])))+'\n')
    file.write('rotate\n')
    file.write('x ' + str(angle)+'\n')
    file.write('apply\n')
    i+=step

file.write('rotate\n')
file.write('z 90\n')
file.write('rotate\n')
file.write('x 30\n')
# file.write('rotate\n')
# file.write('y -20\n')
file.write('move\n')
file.write('250 250 0\n')
file.write('apply\n')
file.write('display\n')
file.write('save\n05.png\n')
file.write('quit\n')
file.close()
