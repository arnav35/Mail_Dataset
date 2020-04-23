import glob
import errno
import csv
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk
#Run this command in python shell - nltk.download('punkt')


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

#read all txt files in the folder
path = '*.txt'
files = glob.glob(path)

for name in files:
	print(name)
	try:
		#Change encoding of file here
		with open(name, "r", encoding="cp1252") as file:
			str = file.read()
			
			soup = BeautifulSoup(str, "html.parser") # create a new bs4 object from the html data loaded
			
			for script in soup(["script", "style"]): # remove all javascript and stylesheet code
			    script.extract()

			# get text
			text = soup.get_text()

			# break into lines and remove leading and trailing space on each
			lines = (line.strip() for line in text.splitlines())

			# break multi-headlines into a line each
			chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

			# drop blank lines
			text = '\n'.join(chunk for chunk in chunks if chunk)

			#optional to remove all puntuations
			text = re.sub(r'[^\w]', ' ', text)
			#to remove https links
			text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
			#to remove digits
			text = re.sub(r'[0-9]+', '', text)

			tokens = word_tokenize(text)

			for i in tokens:
				if len(i) > 20:
					tokens.remove(i)

			#to remove random meaningless long sequences of characters
			text =""
			for i in tokens:
				if len(i) < 20:
					text += i+" "

			#to lower-case
			str = text.lower()
			str = str.strip()

			#remove punctuations
			no_punct = ""
			
			for char in str:
			   if char not in punctuations:
			   	no_punct = no_punct + char		 
			
			stop_words = set(stopwords.words("english"))

			#create tokens
			tokens = word_tokenize(no_punct)

			#remove stopwords
			result = [i for i in tokens if not i in stop_words]
			
			lemmatizer=WordNetLemmatizer()

			final = []
			for word in result:
				final.append(lemmatizer.lemmatize(word))

			with open('newdataset.csv', mode='a') as writer:
				file_writer = csv.writer(writer,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
				
				file_writer.writerow([final, '2'])
				
	except IOError as exc:
		if exc.errno != errno.EISDIR:
        		raise
