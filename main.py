from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
from nltk.stem.snowball import SnowballStemmer
import nltk


class TextSummarizer:
     #ps = PorterStemmer()
     stemmer = SnowballStemmer("english")
     stopWords = set(stopwords.words("english")+ list(punctuation))
     text = ""
     sentences = ""
     def tokenize_sentence(self):
          words = word_tokenize(self.text)
          print(words)
          return words;

     def input_text(self):
          
          while True:
               self.text = input("Enter the text to summarize\n")
               if(len(self.text)>10):
                    break;
               else:
                    print("Please input the text as length at least 10")

     
     def cal_freq(self,words):
          
          # Second, we create a dictionary for the word frequency table.

          freqTable = dict()
          for word in words:
               word = word.lower()
               if word in self.stopWords:
                    continue
               #word = stemmer.stem(word)
               
               if word in freqTable:
                    freqTable[word] += 1
               else:
                    freqTable[word] = 1
          return freqTable;


     def compute_sentence(self,freqTable):
          
          self.sentences = sent_tokenize(self.text)
          sentenceValue = dict() # dict() creates the dictionary with key and it's corresponding value

          for sentence in self.sentences:
               
               for index, wordValue in enumerate(freqTable, start=1):
                    
                    if wordValue in sentence.lower(): # index[0] return word
                         
                         
                         if sentence in sentenceValue:
                              
                              sentenceValue[sentence] += index # index return value of occurence of that word
                              #sentenceValue.update({sentence: index})
                              #print(sentenceValue)
                         else:
                              
                             # sentenceValue[sentence] = wordValue
                              sentenceValue[sentence] = index
                              #print(sentenceValue)

          
          print(sentenceValue)
          return sentenceValue;
         
           

     def sumAvg(self,sentenceValue):
          sumValues = 0
          for sentence in sentenceValue:
               
               sumValues += sentenceValue[sentence]

           # Average value of a sentence from original text
          average = int(sumValues / len(sentenceValue))

          return average;


     def print_summary(self,sentenceValue,average):
          summary = ''
          for sentence in self.sentences:
               if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.5 * average)):
                    summary += " " + sentence
          
          #print(summary)
          return summary

#words= word_tokenize(text)

ts = TextSummarizer()
ts.input_text()
words = ts.tokenize_sentence()
freqTable = ts.cal_freq(words)
sentenceValue = ts.compute_sentence(freqTable)
avg = ts.sumAvg(sentenceValue)
summary = ts.print_summary(sentenceValue,avg)

print("==========================================================")
print("Final summary is:\n\n")
print(summary)




