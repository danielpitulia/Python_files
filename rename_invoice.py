# This program renames invoice files based on the invoice dates using OCR. 
# In order for OCR to work, I needed to convert the invoice files from pdf to jpg. Then I scan the file for the invoice date using pytesseract and rename the file. 
# Date: april 2022. 
import os, pytesseract, re, shutil
from pdf2image import convert_from_path
from PIL import Image

filesInFolder = os.listdir('.')
pdfsInFolder = []
os.makedirs('output')
invoice_name = input("What is the name of the invoices? Filename should contain this string") 

for file in filesInFolder:
    # Select files ending with .pdf that contain 'invoice_name' in filename 
    if file.endswith('pdf') and invoice_name in file:
        image = convert_from_path(file)
       
        # Convert to jpg and save to output folder.
        image[0].save('output\\' + file[:-4] + '.jpg')
        
        # Scan text in image using OCR Tesseract
        textFromImage = pytesseract.image_to_string(Image.open('output\\' + file[:-4] + '.jpg'), lang='swe')
        
        # Scan first date that appears in the file matching "20..-..", which will become the new filename
        startPos = re.search("20..-..-..", textFromImage).span()[0]
        newName = textFromImage[startPos:startPos + 10]
        os.rename(file, 'Faktura_SE_' + newName + '.pdf')

# Remove temporary output folder
shutil.rmtree('output')
