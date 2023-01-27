import PyPDF2
import glob

merger = PyPDF2.PdfFileMerger()
for file in glob.glob('./tag/*.pdf'):
    merger.append(file)
merger.write('merge.pdf')
merger.close()