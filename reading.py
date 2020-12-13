import PyPDF2

file = open('/mnt/0CF2710AF270F972/CodeByFreak/python/sample2.pdf')

pd = PyPDF2.PdfFileReader(file)

x = pd.getPage(1)

print(x.extractText())