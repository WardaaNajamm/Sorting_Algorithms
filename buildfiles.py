
from tkinter import filedialog as fd
import random
import time


def fillFile(fileSize, fileName):
    for i in range(fileSize):
        file = open(fileName + ".txt", "w")
        for i in range(fileSize):
            values = random.randint(1, fileSize)
            file.write(f"{values}\n")

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode.
    words = list(map(int, fileObj.read().split())) #puts the file into an array.
    fileObj. close()
    return words


