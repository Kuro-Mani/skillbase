import pefile
import sys

mal_file = sys.argv[1]
pe = pefile.PE(mal_file)
if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print ("%s" % entry.dll)
        for imp in entry.imports:
            if imp.name != None:
                print ("\t%s" % hex(imp.address),imp.name)
            else:
                print ("\tord(%s)" % (str(imp.ordinal)))
        print ("\n")