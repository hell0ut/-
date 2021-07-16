import math
import os
import struct
import time


# Node of Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

# Count entropy of file/string
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


# Huffman make dictionary
def generateTables(node, val=''):
    newVal = val + str(node.huff)
    if (node.left):
        generateTables(node.left, newVal)
    if (node.right):
        generateTables(node.right, newVal)
    if (not node.left and not node.right):
        global code_table_forward
        code_table_forward[node.symbol]=newVal


# Generate HuffmanCodes
def get_codes(file):
    table=char_table(file)
    nodes = []
    for char in table.keys():
        freq=table[char]
        nodes.append(Node(freq, char))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes[0]
        right = nodes[1]
        left.huff = 0
        right.huff = 1
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    generateTables(nodes[0])


# Get freqs of symbols
def char_table(file):
    symbs = {}
    with open(file, "rb") as f:
        while byte := f.read(1):
            try:
                symbs[byte] += 1
            except:
                symbs[byte] = 1
    return symbs


# Generating packed dictionary at the start of file
def generateDict():
    global code_table_forward
    dict_info=b''
    codes=''
    for symb,code in code_table_forward.items():
        dict_info+=symb+struct.pack('B',len(code))
        codes+=code
    return dict_info,codes


# Compressing =)
def compressFile(file):
    get_codes(file)
    compressed_data=''
    dict_info, codes = generateDict() # array of tupples(char,lenght of Huffman Code)
    with open(file, "rb") as f:
        while (byte := f.read(1)):
            compressed_data+=code_table_forward[byte]
    compressed_data=codes+compressed_data
    bytes_compressed_data=[compressed_data[i:i+8] for i in range(0, len(compressed_data), 8)]

    with open('compr_'+file, "wb") as f:
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
    with open('decompressed_' + file, "wb") as f:
        full_symb = ''
        for symb in encodedbytes[i_new:]:
            full_symb+=symb
            try:
                f.write(new_dict[full_symb])
                full_symb=''
            except:
                pass


if __name__=="__main__":
    code_table_forward = {}
    file='unnamed.jpg'
    print(f'file:{file}')
    start_time = time.time()
    compressFile(file)
    print("Compression time--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    decompressFile('compr_' + file)
    print("Decompression time--- %s seconds ---" % (time.time() - start_time))
    print(entropy(file))
    print(entropy('compr_' + file))
    print('old size: ', os.stat(file).st_size)
    print('compressed size,', os.stat('compr_' + file).st_size)
    print('compression ratio: ', os.stat(file).st_size / os.stat('compr_' + file).st_size)
    print('________')
