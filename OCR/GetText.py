from PIL import Image
import pytesseract
import numpy as np
def GetText(file):
    filename = '/media/abinashlingank/Disk1/MSARS/newspaper.jpg'
    img1 = np.array(Image.open(file))
    text = pytesseract.image_to_string(img1)
    return text
    # print(text)



































from pytesseract import Output
import pytesseract
import cv2


from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('/media/abinashlingank/Disk1/MSARS/OCR/TOI_Delhi_13-12-2023.pdf')
 
for i in range(len(images)):
    # images[i].save('page'+ str(i) +'.jpg', 'JPEG')
    # results = pytesseract.image_to_data(images[i], 
    # output_type=Output.DICT)
    text = pytesseract.image_to_string(images[i])

    print(text)


















# from pytesseract import Output
# import pytesseract
# import cv2

# filename = '/media/abinashlingank/Disk1/MSARS/newspaper.jpg'
# image = cv2.imread(filename)

# results = pytesseract.image_to_data(image, 
# output_type=Output.DICT)

# print(results)




# # importing required modules 
# from PyPDF2 import PdfReader 
  
# # creating a pdf reader object 
# reader = PdfReader('/media/abinashlingank/Disk1/MSARS/OCR/TOI_Delhi_13-12-2023.pdf') 
  
# # printing number of pages in pdf file 
# print(len(reader.pages)) 
  
# # getting a specific page from the pdf file 
# for page in reader.pages: 
    
#     # extracting text from page 
#     text = page.extract_text() 
#     print(text) 

