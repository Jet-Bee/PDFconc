# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:27:15 2024


Simple tool to concatenate pdf files. 

It can be used as python function or as a commandline tool

general: make sure this file is in the Python PATH

Use from Python script or from IDE:
    * import PDFconc
    * type: help(PDFconc.main) for help
    
Use from shell:
    * type: pythonPDFconc.py help for help on use in the shell
   
"""

__author__ = "Jethro Betcke"
__copyright__ = "Copyright 2024, Jethro Betcke"
__version__ = "0.02"
__maintainer__ = "Jethro Betcke"

from PyPDF2 import PdfWriter

import sys


help_text=\
"""
PDFconc

PDFconc concatenates an arbitrary number of pdf files and saves the result
to file. The program is controlled by a configuration file.

How to call:
    python PDFconc.py
        Without an argument the default configuration file './PDFconc.cfg'
        is used
    python PDFconc.py <configuration file name>    
        In this case the program uses the user specified configuration file
    python PDFconc.py h ; PDFconc.py help
        Display this help text
 
'    
 # <some comment for your documentation>    
./file1.pdf
 //abolute/path/file2.pdf
fileout:my_combined_pdf_files.pdf
',    

where the first and the last line are optional  
  
the pdf files are added in the same order as they appear in the 
configuration file

"""            


def read_config_file(config_filename):
    """
    Reads the configuration file that contains the names of the files 
    concatenated, and optionally a name for the result file and comments.
    The content of a typical config file looks like:
        
    # <some comment for your documentation>    
    ./file1.pdf
    //abolute/path/file2.pdf
    fileout:my_combined_pdf_files.pdf
    
    where the first and the last line are optional
    
        
    Arg:
        config_filename: string
        path and name of the configuration file 
    
    Returns:
    
    pdf_list_out: list of strings
        list of the filenames of the pdf-files that need to be combined
    pdf_out_file: string
        filename of the output file 
 
    
    """
    
    with open(config_filename) as fid:    
        pdf_list=fid.readlines()
                               
        pdf_list_r=[pdf_str.strip() for pdf_str in pdf_list ]
        
        is_infile=lambda pdf_str: (not pdf_str.startswith('outfile:'))\
                                   and (not pdf_str.startswith('#'))
            
        #get all the input files from the input
        pdf_list_out = filter(is_infile,
                              pdf_list_r) 
        pdf_list_out = list(pdf_list_out)
        
        pdf_out_file = filter(lambda pdf_str: pdf_str.startswith('outfile:'),
                              pdf_list_r)
        
        pdf_out_file_lst=list(pdf_out_file)
        
        if len(pdf_out_file_lst)>0:
            pdf_out_file = pdf_out_file_lst[0].replace('outfile:','').strip()
        else:
            pdf_out_file = None
        
    return  pdf_list_out, pdf_out_file     
        


def concat_pdfs(pdf_list, outfile='combined_pdfs.pdf') :
    """
    
    Concatenates pdf files, and saves the result to file
    
    Arg:
        pdf_list: list of strings
        list containing the path and filenames of the pdf that are to be 
        concatenated. Files are added in the order of the list.
        
    Keyword arg :
        outfile: string, default: 'combined_pdfs.pdf
        path and name of the resulting pdf file
        
    File output:  
        A new pdf file containing the combined input pdfs

    """
    
    
    merger = PdfWriter()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(outfile)
    merger.close()
     
    
    
def main(config_file='./PDFconc.cfg'):
    """
    Reads a configuration file containing the names of the pdfs that are to
    be concatenated, and optionally the name for the result file.
    See help(read_config_file) for details on the configuration file.
    
    The results are then stored in the file given in the configuration file,
    or in a default file. See help(concat_pdfs) for details.

    Keyword arg:
        config_file: string, default: './PDFconc.cfg'
        path and name of the configuration file

    Returns
    -------
    None.

    """
    
    
    pdf_list, pdf_out_file  = read_config_file(config_file)
    
    if pdf_out_file is None:
        concat_pdfs(pdf_list)
    else:
        concat_pdfs(pdf_list, outfile=pdf_out_file)
        

if __name__=='__main__'    :
        
    nrofargs=len(sys.argv)-1
    if nrofargs==0:
        # carry out program using the default configuration file
        main()
    else:
       user_input=sys.argv[1].strip() #clean the input 
       if user_input.lower() not in ['h','-h', 'help', '-help']: 
           # carry out program with given configuration file
           main(user_input)
       else:
           # give out help
           print(help_text)

      
     
      

    
    
        