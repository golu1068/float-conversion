#from PIL import Image, ImageDraw
#
##img = Image.new("RGB",(60,60),'white')
##dr = ImageDraw.Draw(img)
##dr.ellipse((0,0,50,50),'green')
##
##img.show()
#
#catIm = Image.open(r'E:\spyder_code\New_folder\multipath_test\paytm.jpg')
#print(catIm.size)
#croppedIm = catIm.crop((252, 80, 279, 106))
#croppedIm.save('cropped.png')

print("\n\nlist of right shifted code sequence in hex")
val=0x25961207
for i in range(1,33):
    a = val & 0x01
    b= val >> 1
    if (a == 1):
	    val = b | 0x40000000;
    else:
	    val = b | 0x00000000;
    print(i,a, hex(val))

#import numpy as np
#from scipy.fftpack import fft, ifft
#from scipy import fftpack
#import matplotlib.pyplot as plt
#
#fs = 120e3
#t = np.arange(0, 1, 1/fs)
#
#data = np.sin(2 * np.pi * 150e3 * (t))
#
#final_ip_fft = np.fft.fftshift(np.fft.fft(data))
#
#freqs = np.fft.fftshift(fftpack.fftfreq(len(data)))*fs
##plt.plot( abs(np.array(val)))  
##plt.plot(freqs, (abs(np.array(final_ip_fft))))
#x = list(range(0,len(data)))
##plt.plot(x, data)
#plt.hist(data)
    
##  sampling
#fm = 150e6
#fm_n = -fm
#fs = 120e6
##
#for n in range(10):
#    f1 = (fm + (n*fs))/1000000
#    f2 = (fm_n + (n*fs))/1000000
#    f3 = (fm - (n*fs))/1000000
#    f4 = (fm_n - (n*fs))/1000000
#    print(f1,f2,f3,f4)
    
#import matplotlib.pyplot as plt    
#
#file = r'F:\ranging\Artix-7_Builds\Delivery_board\data.txt'
#read_file = open(file, 'r+')
#arr=[];
#while 1:
#    line = read_file.readline()
#    if (line == ''):
#        break
#    line = line.split(':')
#    arr.append(int(line[1],16))
#    
##plt.plot(arr)
#arr_diff = [(arr[i] - arr[i-1])  for i in range(1, len(arr))] 
#plt.plot(arr_diff)  
    
    
    
    
    
    
    
    
    
    
    

    
