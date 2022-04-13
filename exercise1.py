'''
Author: Scott Chieu
KUID: 3070568
Date: 04/13/2022
Lab: lab05
Last modified: 04/13/2022
Purpose: This program lets user enter a txt file. The program will returns a dictionary with every words in the text(counted), and a dictionary with words only used once.
'''

def build_count(romeo):
	dog = {}
	romeo = romeo.split()
	for word in romeo:
		countword = clean_word(word)
		if countword not in dog:
			dog[countword] = 0
		dog[countword] += 1
	return dog
def clean_word(word):
	countword = ""
	for _ in word:
		if _ not in "!?:;,|.=='\ ":
			countword += _
	countword = countword.lower()
	return countword
def unique_words(word_counts):
	juliet = []
	for _ in word_counts:
		if word_counts[_] == 1:
			juliet.append(_)
	return juliet
def main():
	print("=============Welcome=============")
	file_name = input("Enter file name: ")
	cat = ""
	with open(file_name, "r") as f:
		cat = f.read()
	word_counts = build_count(cat)
	store = unique_words(word_counts)
	with open("word_data.txt", "w") as f:
		for d in word_counts:
			f.write(d)
			f.write(" ")
			f.write(str(word_counts[d]))
			f.write("\n")
	with open("unique_words.txt", "w") as f:
		for d in store:
			f.write(d)
			f.write("\n")
	print(str(file_name) + "has been processed.")
	print("Output stored in word_data.txt and unique_words.txt")
	print("exiting...")
main()