from wordcloud import WordCloud
import matplotlib.pyplot as plt

	
def word_cloud(text, filename):

	wc = WordCloud().generate(text)
	plt.figure(figsize=(18, 14))
	plt.imshow(wc)
	plt.savefig(filename)

if __name__ == "__main__": 
	word_cloud("Vies heel vies") 
	

