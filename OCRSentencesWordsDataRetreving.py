# Import libraries
!pip3 install PIL
!pip3 install pytesseract
!pip3 install pdf2image

from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
  
# Path of the pdf
PDF_file = "Minutes.pdf"
  
'''
Part #1 : Converting PDF to images
'''
  
# Store all the pages of the PDF in a variable
pages = convert_from_path(PDF_file, 500)
  
# Counter to store images of each page of PDF to image
image_counter = 1
  
# Iterate through all the pages stored above
for page in pages:
  
    # Declaring filename for each page of PDF as JPG
    # For each page, filename will be:
    # PDF page 1 -> page_1.jpg
    # PDF page 2 -> page_2.jpg
    # PDF page 3 -> page_3.jpg
    # ....
    # PDF page n -> page_n.jpg
    filename = "page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system
    page.save(filename, 'JPEG')
  
    # Increment the counter to update filename
    image_counter = image_counter + 1
  
'''
Part #2 - Recognizing text from the images using OCR
'''
# Variable to get count of total number of pages
filelimit = image_counter-1
  
# Creating a text file to write the output
outfile = "out_text.txt"
  
# Open the file in append mode so that 
# All contents of all images are added to the same file
f = open(outfile, "a")
  
# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):
  
    # Set filename to recognize text from
    # Again, these files will be:
    # page_1.jpg
    # page_2.jpg
    # ....
    # page_n.jpg
    filename = "page_"+str(i)+".jpg"
          
    # Recognize the text as string in image using pytesserct
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
  
    # The recognized text is stored in variable text
    # Any string processing may be applied on text
    # Here, basic formatting has been done:
    # In many PDFs, at line ending, if a word can't
    # be written fully, a 'hyphen' is added.
    # The rest of the word is written in the next line
    # Eg: This is a sample text this word here GeeksF-
    # orGeeks is half on first line, remaining on next.
    # To remove this, we replace every '-\n' to ''.
    text = text.replace('-\n', '')    
  
    # Finally, write the processed text to the file.
    f.write(text)
  
# Close the file after writing all the text.
f.close()


my_file = open('out_text.txt', "r")

data = my_file.read()
data_into_list = data.replace("\n",' ').split(".")

#from nltk.corpus import words
Data_Into_List_Copy = data_into_list
ExtraSpacesRemovedData_Into_List = []
SentenceIndex = 0
SentenceListOfList=[]
for Sentence in Data_Into_List_Copy:
    SentenceList=[]
    for item in Sentence:
        SentenceList.append(item)
    SentenceListOfList.append(SentenceList)
    
#!pip3 install translate
#!pip3 install deep_translator
#!pip3 install num2words
from deep_translator import GoogleTranslator
from translate import Translator
translator= Translator(to_lang="German")
translation = translator.translate("Good Morning!")
SchoolTranslatedIntoGerman = []
#translated = GoogleTranslator(source='auto', target='de').translate(to_translate)
import time
from num2words import num2words
for item in data_into_list:
    print(type(item))
    if item.isnumeric() == True:
        itemnumber = num2words(int(item))
        new_word = GoogleTranslator(source='auto', target='de').translate(itemnumber)
        SchoolTranslatedIntoGerman.append(new_word)
    else:
        print(len(item))
        print(item)
        new_word = GoogleTranslator(source='auto', target='de').translate(item)
        SchoolTranslatedIntoGerman.append(new_word)