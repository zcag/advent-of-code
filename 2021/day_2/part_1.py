exec('d,p=0,0;'+open('input').read().replace('forward','p+=').replace('down','d+=').replace('up','d-=')+'print(d*p)')
