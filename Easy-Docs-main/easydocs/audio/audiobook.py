from gtts import gTTS
import pyttsx3
import pdfplumber
from io import BytesIO


def convert_text_to_audio(text_input, slow):
	if slow == "Yes":
		audio = gTTS(text=text_input, lang='en', slow=True)
	elif slow == "No":
		audio = gTTS(text=text_input, lang='en', slow=False)

	return audio

def convert_pdf_to_audio(pdf_file, slow):
	pdf_text = ''

	try:
		with pdfplumber.open(pdf_file) as pdf:
			pages = pdf.pages
			for val in pages:
				pdf_text += val.extract_text()

		print(pdf_text)

		if slow == "Yes":
			audio = gTTS(text=pdf_text, lang='en', slow=True)
		elif slow == "No":
			audio = gTTS(text=pdf_text, lang='en', slow=False)
		
		return audio
	except:
		return "Not in a readable format."

if __name__ == "__main__":
	sample_text = "This is some test audio to check whether this goddamn thing works!"
	convert_text_to_audio(sample_text, "No", "Yes")
