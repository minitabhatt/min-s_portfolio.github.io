import PyPDF2
a = PyPDF2.PdfFileReader('D:\\USERS\HP\Desktop\GSEB OLD PAPERS\\NB Data\Mahi\Sample Paper\\Chemistry-MS.pdf')
#print(a.documentInfo)
#print(a.getNumPages())
str=' '
for i in range(1, 9):
    str+=a.getPage(i). extractText()
with open ("text.txt","w",encoding='utf-8') as f:
    f.write(str)



