from Huffman import *

def show(str):
    for key,value in Huffman(str).items():
        print("%4r | %10r"%(key,value))

str = input("INPUT STRING::")

print("Compressed::",compress(str))
show(str)
