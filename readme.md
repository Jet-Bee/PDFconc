# PDFconc.py

## Introduction

Merging a collection of PDFs with a GUI tool like Acrobat or online service is fairly intuitive and fine if you have to do it once. But if you have to repeat the proces more often, for example because one of the pdfs gets updated, this becomes a bit more cumbersome. This mild annoyance sparked the creation of this Python tool to effortsly merge pdf files as often as you like. It is controlled by a simple ascii configuration file that you can easily adapt to your needs.

## Installation and Prerequisites

Requires Python 3 with the PyPDF2 package installed.

PDFconc was tested using Python 3.10.9 and PyDF2 3.0.1

To install PyPDF2 either:

`pip install PyPDF2` from shell or IDE or `conda install PyPDF2` from shell

Optionally add the PDFconc directory to the python path variable, to be able to call it from anywhere in the directory tree.

## How to use

The tool can be used in three ways:
- as commandline application
- as IDE application
- as module to be used in python scripts

### commandline application
From a shell commandline the application can be called with:

`python PDFconc.py`  (use default configuration file)
`python PDFconc.py  <your configuration file>`  (use user-defined configuration file)
`python PDFconc.py help` (get detailed help)

### IDE application
To use the application in an IDE first add the PDFconc directory to the python path and then import the module:

```
import sys
sys.path.append(<PDFconc directory>)
import PDFconc
```

It can than we called from the IDE commandline with:
`PDFconc.main()`  (use default configuration file)
`PDFconc.main(<your configuration file>)`  (use user-defined configuration file)
`help(PDFconc.main)` (get more detailed help)

## The configuration file 
The configuration file contains the names of the files that are to be concatenated, and optionally the name of an outputfile and comments. 

Here is an example:

```
# <some comment for your documentation> 
# As much comments as you like   
/file1.pdf
//abolute/path/file2.pdf
# <some comment about the output file>
fileout: my_combined_pdf_files.pdf
```

in case there is no line starting with `fileout:` the result will be saved under `combined_pdfs.pdf` in the current directory.

## Example files
The PDFconc directory contains the pdf files My_first_PDF.pdf, PDF2.pdf and PDF_GAMMA.pdf. These are combined when you use the configuration files PDFconc.cfg or PDFconc_with__user_set_outputfile.cfg
