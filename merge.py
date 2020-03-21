import sys
import os
from pathlib import Path
from os import listdir
from os.path import isfile, join

import PyPDF2

merger = PyPDF2.PdfFileMerger()

#get PDFs files and path
path = Path('C:/Users/tqhee/Dropbox/Insurance/USAA/dishwasher_claim/receipts/')
pdfs = [f for f in listdir(path) if isfile(join(path, f))]

os.chdir(path)


#iterate among the documents
for pdf in pdfs:
    try:
        #if doc exist then merge
        if os.path.exists(pdf):
            input = PyPDF2.PdfFileReader(open(pdf,'rb'))
            merger.append((input))
        else:
            print(f"problem with file {pdf}")

    except:
            print("cant merge !! sorry")
    else:
            print(f" {pdf} Merged !!! ")

merger.write("qualls-ale-receipts.pdf")