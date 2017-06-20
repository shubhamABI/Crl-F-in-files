"""
    this set of function is used to find tracing of any kewyword 
    from given set of directory.
    Example:-if we need to search some set of keyword from 
    a project source code folder with path of that file.
    it is just similar to Ctrl+F (fild in Files).but here you will
    get result in excel sheet.
    S.No File_path keyword lineNo line 
"""
from openpyxl import Workbook
from openpyxl.styles import Font
import os


"""
this function is used to add keywords
which need to be serach in files
"""
#global parameters
keywordList=["pcs"]
sheet=""
wb=""
row_count=1
excel_sheet_path=os.path.expanduser("~/Desktop/KeywordSearchlog.xlsx")

def add_keyword(x):
    list1=x.split("|")

    global keywordList
    keywordList.extend(list1)
    print(keywordList)
    
#add_keyword(input("Please Enter the word"))
#print(keywordList)
    """
    read the input directory 
    """
def readfile(indir):
    
    #indir="F:\\SHUBHAM\\Find and replace project in python\\files"
    """
    craete excel sheet for storing result
    """

    createExcelSheetforlog(excel_sheet_path)
    
    """
    it will give each file iteratinf input directory
    
    """
    for root, dirs, filenames in os.walk(indir):
       for f in filenames:
           file_path=root+"\\"+f
           search_in_file(file_path)
    print("Searching Completed!!!")
           
def search_in_file(path):
    with open(path) as fl:
        count=1
        for line in fl:
            for kw in keywordList:
                if kw.lower() in line.lower():
                    #print(path+"----"+kw+"---"+str(count)+"---"+line)
                    insert_data_into_excel_Sheet(path,kw,count,line)
                    count+=1
                    
    
          
      
   
def createExcelSheetforlog(path):
    global sheet1
    global wb
    wb=Workbook()
    sheet=wb.active
    sheet.title="logs"
    sheet1=wb.get_sheet_by_name("logs")
    header_font=Font(size=12,bold=True)
    sheet1['A1'].font,sheet1['B1'].font,sheet1['C1'].font,sheet1['D1'].font,sheet1['E1'].font=header_font,header_font,header_font,header_font,header_font
    sheet1['A1']="S.No"
    sheet1['B1']="File Path"
    sheet1['C1']="Keyword"
    sheet1['D1']="Line Number"
    sheet1['E1']="Line"
    wb.save(path)
    
    
    """
        @insert_data_into_excel is used to trace record into excel sheet.
        @filepath:-path of file where keyword is present.
        @Keyword
        @line No
        @line which have that keyword
    """
def insert_data_into_excel_Sheet(filepath,keyword,lineNo,line):
    global row_count
    sheet1['A'+str(row_count)]=row_count
    sheet1['B'+str(row_count)]=filepath
    sheet1['C'+str(row_count)]=keyword
    sheet1['D'+str(row_count)]=lineNo
    sheet1['E'+str(row_count)]=line
    row_count+=1       
    wb.save(excel_sheet_path)
    


if __name__ == '__main__':
    keyword_string=input("Please Enter list of keyword seprated by |(pipe) \n")
    add_keyword(keyword_string)
    indir=input("Please enter full path of source\n")
    print("Searching.....")
    readfile(indir)