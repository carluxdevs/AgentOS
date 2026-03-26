import sys
import Quartz
from Foundation import NSURL

def extract_text(pdf_path):
    url = NSURL.fileURLWithPath_(pdf_path)
    pdf = Quartz.PDFDocument.alloc().initWithURL_(url)
    if pdf is None:
        print("Failed to open PDF")
        return
    text = ""
    for i in range(pdf.pageCount()):
        page = pdf.pageAtIndex_(i)
        text += page.string() + "\n"
    print(text)

extract_text(sys.argv[1])
