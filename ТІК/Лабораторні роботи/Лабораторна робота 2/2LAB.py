import math
import os
import struct

class Char:
    def __init__(self, name, freq) -> None:
        self._name = name
        self._freq = freq
        self._code = ""

    def __lt__(self, other):
        return True if self._freq < other.get_freq() else False

    def __eq__(self, other):
        return True if self._name == other.get_name() and self._freq == other.get_freq() else False

    def __str__(self):
        return "{0}\t {1}\t {2}".format(self._name, str(self._freq), self._code)

    def __iter__(self):
        return self

    def get_name(self):
        return self._name

    def get_freq(self):
        return self._freq

    def get_code(self):
        return self._code

    def append_code(self, code):
        self._code += str(code)


def entropy(file):
    with open(file, 'rb') as f:
        byteArr = list(f.read())
    fileSize = len(byteArr)
    freqList = []
    for b in range(256):
        ctr = 0
        for byte in byteArr:
            if byte == b:
                ctr += 1
        freqList.append(float(ctr) / fileSize)
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    ent = -ent
    return ent


def shannonTable(file):
    symbs = {}
    lst=[]
    with open(file, "rb") as f:
        while (byte := f.read(1)):

            try:
                symbs[byte] += 1
            except:
                symbs[byte] = 1
    lenght=os.stat(file).st_size
    for key, value in symbs.items():
        lst.append(Char(key,value/lenght))
    return lst


def find_middle(lst):
    if len(lst) == 1: return None
    s = k = b = 0
    for p in lst: s += p.get_freq()
    s /= 2
    for p in range(len(lst)):
        k += lst[p].get_freq()
        if k == s: return p
        elif k > s:
            j = len(lst) - 1
            while b < s:
                b += lst[j].get_freq()
                j -= 1
            return p if abs(s - k) < abs(s - b) else j
    return


def generateDict():
    global code_table_forward
    dict_info=b''
    codes=''
    for symb,code in code_table_forward.items():
        dict_info+=symb+struct.pack('B',len(code))
        codes+=code
    return dict_info,codes


def shannon_fano(lst):
    middle = find_middle(lst)
    if middle is None: return
    for i in lst[: middle + 1]:
        i.append_code(0)
    shannon_fano(lst[: middle + 1])
    for i in lst[middle + 1:]:
        i.append_code(1)
    shannon_fano(lst[middle + 1:])


def compressFile(file):
    compressed_data=''
    dict_info, codes = generateDict() # array of tupples(char,lenght of Huffman Code)
    with open(file, "rb") as f:
        while (byte := f.read(1)):
            compressed_data+=code_table_forward[byte]
    compressed_data=codes+compressed_data
    bytes_compressed_data=[compressed_data[i:i+8] for i in range(0, len(compressed_data), 8)]

    with open('comprSHENO_'+file, "wb") as f:
        f.write(struct.pack('H',len(dict_info)//2))
        f.write(dict_info)
        for byte_string in bytes_compressed_data:
            byte=int(byte_string,2)
            byte=byte.to_bytes(1,'little')
            f.write(byte)

def decompressFile(file):
    with open(file, "rb") as f:
        leng=struct.unpack('H',f.read(2))[0]*2
        dict_info=f.read(leng)
        dict_infoarray=[struct.unpack('cB', dict_info[i:i + 2]) for i in range(0, len(dict_info), 2)]
        numb_bits=0
        for el in dict_infoarray:
            numb_bits+=el[1]
        compressed_data_bytes=f.read()
    encodedbytes=''
    for index,byte in enumerate(compressed_data_bytes):
        new_byte=f'{byte:b}'
        if len(new_byte) <8:
            new_byte = '0' * (8-len(new_byte)) + new_byte
            if index==len(compressed_data_bytes)-1:
                new_byte=f'{byte:b}'
        encodedbytes+=new_byte
    i, i_new=0, 0
    new_dict={}
    for el in dict_infoarray:
        i_new=i+el[1]
        new_dict[encodedbytes[i:i_new]]=el[0]
        i=i_new
    with open('decompressedSHENO_' + file, "wb") as f:
        full_symb = ''
        for symb in encodedbytes[i_new:]:
            full_symb+=symb
            try:
                f.write(new_dict[full_symb])
                full_symb=''
            except:
                pass

def ShannonFanno(file):
    lst=shannonTable(file)
    shannon_fano(lst)
    global code_table_forward,code_table_reverse
    for item in lst:
        code_table_forward[item.get_name()]=item.get_code()


if __name__=="__main__":
    code_table_forward = {}
    code_table_reverse = {}
    file='aboba.txt'
    print(file)
    ShannonFanno(file)
    #compressFile(file)
    decompressFile('comprSHENO_' + file)
    print(entropy(file))
    print(entropy('comprSHENO_' + file))
    print('old size: ',os.stat(file).st_size)
    print('compressed size,',os.stat('comprSHENO_' + file).st_size)
    print('compression ratio: ',os.stat(file).st_size/os.stat('comprSHENO_' + file).st_size)
    print('________')