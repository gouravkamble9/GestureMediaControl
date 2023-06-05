import win32com.client
import os
import shutil
import os.path
from pdf2image import convert_from_path

def ppttoimages(pathname):
	x = pathname.replace("/","\\")
	current_dir = os.getcwd()
	updated_dir = current_dir.replace("\\", "\\\\")
	newpathofoutput=updated_dir+"\\\sample"
	in_file=x
	out_file=os.path.splitext(newpathofoutput)[0]
	powerpoint=win32com.client.Dispatch("Powerpoint.Application")
	pdf=powerpoint.Presentations.Open(in_file,WithWindow=False)
	pdf.SaveAs(out_file,32)
	pdf.Close()
	powerpoint.Quit()



	os.mkdir('imag')
	out_dir="imag/"
	# Store Pdf with convert_from_path function

	images = convert_from_path('sample.pdf',500,poppler_path=r'C:\Program Files\Release-22.04.0-0\poppler-22.04.0\Library\bin')

	for i in range(len(images)):

		# Save pages as images in the pdf
		images[i].save(out_dir+'page'+ str(i) +'.jpg', 'JPEG')


	#resize images
	from PIL import Image

	f = r'imag'
	for file in os.listdir(f):
		f_img = f + "/" + file
		img = Image.open(f_img)
		img = img.resize((1550, 768))
		img.save(f_img)

	import main