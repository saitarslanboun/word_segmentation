import io, sys

from textblob import TextBlob

if __name__ == "__main__":
	with io.open (sys.argv[1], "r", encoding="utf-8") as myfile:
                text=myfile.read()

	zen = TextBlob(text)
	sentence_list = zen.sentences

	text_file = open("train.txt", "w")
	for sentence in sentence_list:
		text_file.write(str(sentence))
		text_file.write("\n\n")
	text_file.close()
