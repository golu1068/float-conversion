import math
import plotly_plot as pp
import numpy as np

def float2bin(f, size=64):
    final_val='';
#    if(f < 0):
#        sign = 1
#    else:
#        sign = 0
    for i in range(size-1):
        val = f*2
        f,i = math.modf(val)
        final_val = final_val + str(int(i))
    return final_val
  
def bin2fraction(f):
    out=0.0;
    for i in range(len(f)):
        out = out + float((int(f[i])*(2**-(i+1))))
        # for mantissa add 1 to out
    return out

def float2hex(b, double=False):
    if (double == True):
        if (b < 0):
            sign=1
        else:
            sign = 0
        f,i = math.modf(math.fabs(b))
        i_bin = bin(int(i)).replace('0b','')
        f_bin = float2bin(f, size=64)
        e_m = i_bin + '.' + f_bin
        point_index = e_m.index('.')
        if (float(e_m) > 1):
            e = f'{point_index- 1 + 1023:011b}'.replace('0b', '')
            e_m = e_m.replace('.','')
            mantissa = e_m[1:]
        elif (float(e_m) < 1):
            e_m = e_m.replace('.','')
            for i in range(len(e_m)):
                if (e_m[i] == '1'):
                    e_m = e_m[:i+1] + '.' + e_m[i+1:]
                    v = 1023-i
                    e = f'{v:011b}'#bin(126).replace('0b', '')
                    mantissa = e_m[i+2:]
                    break        
            if (i+1 == len(e_m)):
                e=0
                mantissa = 0
        else:
            e=f'{1023:011b}'
            mantissa = e_m[2:]
        s_p_v = (str(sign)+str(e)+str(mantissa))
        s_p_v = s_p_v[:64]
        
        int_spv = int(s_p_v, 2)
        hex_spv = f'{int_spv:04x}'
        re = '0x'+hex_spv
        return re
    
    else:
        if (b < 0):
            sign=1
        else:
            sign = 0
        f,i = math.modf(math.fabs(b))
        i_bin = bin(int(i)).replace('0b','')
        f_bin = float2bin(f, size=32)
        e_m = i_bin + '.' + f_bin
        point_index = e_m.index('.')
        if (float(e_m) > 1):
            e = f'{point_index- 1 + 127:08b}'.replace('0b', '')
            e_m = e_m.replace('.','')
            mantissa = e_m[1:]
        elif (float(e_m) < 1):
            e_m = e_m.replace('.','')
            for i in range(len(e_m)):
                if (e_m[i] == '1'):
                    e_m = e_m[:i+1] + '.' + e_m[i+1:]
                    v = 127-i
                    e = f'{v:08b}'#bin(126).replace('0b', '')
                    mantissa = e_m[i+2:]
                    break        
            if (i+1 == len(e_m)):
                e=0
                mantissa = 0
        else:
            e=f'{127:08b}'
            mantissa = e_m[2:]
        
        s_p_v = (str(sign)+str(e)+str(mantissa))
        s_p_v = s_p_v[:32]
#        if (singleprecision == True):
#            return s_p_v
        
#        if (len(s_p_v) > 32):
#            s_p_v = s_p_v[0:32]
#        elif (len(s_p_v) < 32):
#            s_p_v = s_p_v + '0'*(32 - len(s_p_v))
        int_spv = int(s_p_v, 2)
        hex_spv = f'{int_spv:04x}'
        re = '0x'+hex_spv
        
        return re

def hex2float(h, double=False):
    if (h == 0):
        return 0
    
    if (double == True):
        if (type(h) == str):
            binary = "{0:064b}".format(int(h,16))
        else:  
            binary = "{0:064b}".format(h)
            
        sign = int(binary[0])
        exp = binary[1:12]
        man = binary[12:]
        exp_int = int(exp, 2)
        exp_int = 2**(exp_int - 1023)
        man_int = bin2fraction(man)
#        print(man_int)

        re = exp_int * (1 + man_int)
        if (sign == 0):
           return re
        elif(sign == 1):
            return '-' + str(re)
    else:
        if (type(h) == str):
            binary = "{0:032b}".format(int(h,16))
        else:  
            binary = "{0:032b}".format(h)#str(bin(h).replace('0b', ''))
    
        sign = int(binary[0])
        exp = binary[1:9]
        man = binary[9:]
        exp_int = int(exp, 2)
        exp_int = 2**(exp_int - 127)
        man_int = bin2fraction(man)
        re = exp_int * (1 + man_int)
        if (sign == 0):
           return re
        elif(sign == 1):
            return '-' + str(re)
    
#a=float2hex(50.3, double =False)
#print('a= ',a)
          
h =  '0xce4ccccd'
x = hex2float(h, double =False)
print(x);


#read_file = r'E:\write\split_0_30 (2).txt'
#read_file = r'E:\data_dump_184.txt'
#read_file_w = r'E:\wfwfwfwfw.txt'
#file_r = open(read_file, 'r')
#file_a = open(read_file_w, 'w+')
#data_arr = [];carr_ph=[];
#vall=[];
#
#while 1:
#    line = file_r.readline()
#    if (line == '' or len(line) == 1):
#        break
#    data = line.split()
##    line = file_r.readline()
##    if (line == ''):
##        break
##    data_2 = line.split()
##    data = data_2[1] + data_1[1]
#    fl_val = int('0x'+data[1], 16)
##    fl_val = hex2float('0x'+data[1], double=False)
##    data_arr.append(int(data[1]))
#    data_arr.append(fl_val)
#    file_a.write('0x'+data[1] + '         ' + str(fl_val) + '\n')
#    ######################################################################
#    line = file_r.readline()
#    line = file_r.readline()
##    line = file_r.readline()
##    if (line == '' or len(line) == 1):
##        break
##    data = line.split()
##    fl_val = hex2float('0x'+data[1], double=False)
##    carr_ph.append(float(fl_val)/(2*np.pi))
##    file_a.write('0x'+data[1] + '         ' + str(float(fl_val)/(2*np.pi)) + '     ###  divided by 2pi\n')
##for i in range(1,len(carr_ph)):
##    vall.append(((carr_ph[i] - carr_ph[i-1])))
#    
#file_a.close()
#file_r.close()

#################################################################

## SNR
#sqr_data_mean = [(data_arr[i]**2)  for i in range(len(data_arr))]
#sqr_data_mean = np.mean(sqr_data_mean)
#quad_data_mean = [(data_arr[i]**4)  for i in range(len(data_arr))]
#quad_data_mean = np.mean(quad_data_mean)
#
#num_nume = (np.sqrt((2*(sqr_data_mean**2)) - quad_data_mean))
#num_deno = sqr_data_mean - num_nume
#SNR = num_nume/num_deno
#SNR_db = 10*np.log10(SNR/1)
#print(SNR_db)


#print(quad_data_mean)
#num = np.sqrt((2*(sqr_data_mean**2)) - quad_data_mean)
##print(sqr_data_mean - num)
#SNR = 10*np.log10(num/(sqr_data_mean - num))
#print(SNR)


##############################################################

#x = list(range(0, len(data_arr)))

#pp.plot(x, data_arr , filename = 'code_ph error')
#pp.plot(x, carr_ph , filename = 'carr_ph error')
#xx = list(range(0, len(vall)))
#pp.plot(xx, vall , filename = 'diff')

#01000001101001101110000101001000
#01000001101001101110000101001000
#hex2bin = dict('{:x} {:04b}'.format(x,x).split() for x in range(16))
#bin2hex = dict('{:b} {:x}'.format(x,x).split() for x in range(16))
    
#def float_dec2bin(d):
#    neg = False
#    if d < 0:
#        d = -d
#        neg = True
#    hx = float(d).hex()
#    p = hx.index('p')
#    bn = ''.join(hex2bin.get(char, char) for char in hx[2:p]) 
#    return (('-' if neg else '') + bn.strip('0') + hx[p:p+2]
#            + bin(int(hx[p+2:]))[2:])

#def float2bin(f):
#    hx = float.hex(f)
#    print(hx)
##    hx = float(f).hex()
#    p = hx.index('p')
##    p_sign = hx[p+1:p+2]
#    if (f < 0):
#        neg=1
##        si='-'
#    else:
#        neg=0
##        si = ''
#    bn = ''.join(f"{int(char,16):04b}" for char in hx[2+neg:p] if (char != '.'))
#    if (neg == 1):
#        bn = '-' + bn
#    else:
#        bn = bn
#    bn = int(bn)
##    bn = bn[:4] + '.' + bn[4:]
##    p_val = hx[p+2:]
##    binary = si + str(bn.strip('0')) + 'p' + p_sign + str(bin(int(p_val)).replace('0b',''))
#    
#    return str(bn)

        
        
#b=float_dec2bin(.375)
#print(b)
#a=float2bin(0.375)
#print(a)
#p_index = a.index('p')
#p_sign = a[p_index+1: p_index+2]
#p_val = int(a[p_index+2:], 2)
#a_val = a[:p_index]
#a_val_p = a_val.replace('.', '')
##print(int(a_val))
#if (p_sign == '-'):
#    a_val = str(float(a_val)/(pow(10, p_val)))
#else:
#    a_val = str(float(a_val)*(pow(10, p_val)))
##if (len(a_val) < p_val):
##    a_val = a_val + '0'*(p_val - len(a_val)) + '.0'
##else:
##    a_val = a_val[:p_val+1] + '.' + a_val[p_val+1:]
#print(a_val)
##print(f"{int(a_val[:len(a_val)-1],2):04x}")
#
##
#    01000000000011001100110011001101
#    01000000000001100110011001100110



##00111111000010100011110101110001
### #################################################
#read_file = r'E:\data_error_4.txt'
#file = open(read_file, 'r+')
#arr=[];
#while 1:
#    line = file.readline()
#    print(line)
#    if (line == '' or line == '\n'):
#        break
#    data = '0x' + line.split()[1]
#    arr.append(hex2float(data, double =False))
#x = list(range(0, len(arr)))
#pp.plot(x, arr, plot=True, filename = 'error')   