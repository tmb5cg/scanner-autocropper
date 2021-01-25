from PyPDF2 import PdfFileWriter, PdfFileReader
import os

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import imgdetect


def split_pdf(input_filepath, output_filepath):

    original_output_filepath = output_filepath + "/"
    arr = input_filepath.split("/")
    lenarr = len(arr)

    individual_filename = arr[lenarr-1]

    # remove .pdf
    individual_filename = individual_filename[:-4] 


    # pdf_filename = "1.17.94.pdf"


    # dir_path = os.path.dirname(os.path.realpath(__file__))


    # input_filepath = dir_path + "/" + pdf_filename
    # output_filepath = dir_path + "/" + pdf_filename[:-4] + "_split"

    pdf_outputfolder = output_filepath + "/pdfs"
    images_outputfolder = output_filepath + "/uncropped_images"
    if not os.path.exists(pdf_outputfolder):
        os.makedirs(pdf_outputfolder)
    if not os.path.exists(images_outputfolder):
        os.makedirs(images_outputfolder)


    inputpdf = PdfFileReader(open(input_filepath, "rb"))

    numpgs = inputpdf.numPages

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        output_filepath = pdf_outputfolder + "/"

        newpdf_filename = output_filepath + individual_filename + "_" + "%s.pdf" % i

        with open(output_filepath + individual_filename + "_" + "%s.pdf" % i, "wb") as outputStream:
            # Save individual PDF
            output.write(outputStream)
        
        jpgfilename = individual_filename + "_" + "%s" % i + "_"

        # Convert to jpeg
        convert_from_path(newpdf_filename, output_folder=images_outputfolder, fmt="png", output_file=jpgfilename)

        converted_filename = images_outputfolder + "/" + jpgfilename + "0001-1.png"
        print(converted_filename)

        # Crop image
        imgdetect.doWork(converted_filename, original_output_filepath)
    

