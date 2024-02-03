import os
from Final_Pattern_Match_old import ConvPdfToText , InputStmmr , TextMinning , WordFileProcessing
path = "C:\\Users\\Sarvesh\\AppData\\Roaming\\nltk_data\\corpora\\cgisample\\"
path_out = "C:\\Users\\Sarvesh\\AppData\\Roaming\\nltk_data\\corpora\\cgisample\\"
items = os.listdir(path)
listFile = []
class ReadFile():
    def __init__(self,path):
        self.path = path

    def listpdffiles(self):
        for names in items:
            if names.endswith(".pdf") or names.endswith(".docx") or names.endswith(".doc"):
                listFile.append(names)
                continue
        print(listFile)
        return listFile

    def RemoveFile(self):
        try:
            for file in os.listdir(self.path):
                if file.endswith(".txt"):
                    os.unlink(self.path+file)
                else:
                    print("No text File Found!..")
        except Exception:
            print("File <{}> not found".format(file))


class ProcessPdfFiles(ReadFile):

    def __init__(self,path,path_out,Srchpattrn):
        self.path = path
        self.path_out = path_out
        self.Srchpattrn = Srchpattrn

    def processFiles(self):
        ObjRead = ReadFile(self.path)
        #print("Currently rea ProcessFiles.. ")
        ObjReadFile = ReadFile(self.path)
        listFile = ObjReadFile.listpdffiles()
        print(listFile)
        for file in listFile:

            if file.endswith(".pdf"):
                fl_name = file.split('.')[0]
                ObjFPM = ConvPdfToText(self.path+file, self.path_out, fl_name)
                ObjFPM.Pdfconv()
                ObjInputStmmr = InputStmmr(self.Srchpattrn)
                Text_comp = ObjInputStmmr.SrchpattrnStmmed()
                #print( Text_comp)
                ObjTextMinning = TextMinning(self.path_out, Text_comp,fl_name)
                ObjTextMinning.Textminner()
                #ObjReadFile.RemoveFile()
                continue
            elif file.endswith(".docx") or names.endswith(".doc"):
                fl_name = file.split('.')[0]
                ObjWord = WordFileProcessing(self.path,file, fl_name )
                ObjWord.ReadDocFiles()
                ObjInputStmmr = InputStmmr(self.Srchpattrn)
                Text_comp = ObjInputStmmr.SrchpattrnStmmed()
                ObjTextMinning = TextMinning(self.path_out, Text_comp,fl_name)
                ObjTextMinning.Textminner()
                #ObjReadFile.RemoveFile()
                continue

#--------------------------------------------
#   Main Execution Steps
#--------------------------------------------
class main(ProcessPdfFiles):
    if __name__ == "__main__" :
        Srchpattrn = input("What would you like to search now ? ")
        ObjProcessPdfFiles = ProcessPdfFiles(path, path_out,Srchpattrn)
        ObjProcessPdfFiles.processFiles()
        print('main is called')


