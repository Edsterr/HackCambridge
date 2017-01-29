from __future__ import print_function
import pkg_resources
import string
import re
import math
import operator

exclude = list(string.punctuation)
easy_word_set = set([ln.strip() for ln in pkg_resources.resource_stream('textstat', 'easy_words.txt')])


class textstatistics:
    def __init__(self):
        return None
    
    #Outputs total of number of characters(alphanumerical and punct.) in
    #a given text string
    def char_count(self, text, ignore_spaces=True):
        if ignore_spaces:
            text = text.replace(" ", "")
        return len(text)

    #Outputs the number of words in a given string
    def word_count(self, text, removepunct=True):
        if removepunct:
            text = ''.join(ch for ch in text if ch not in exclude)
        count = len(text.split())
        return count

    #Outputs (roughly) the  number of syllables in a given word
    #Feel free to change for a more optimal solution
    def syllable_count(self, text):
        count = 0
        vowels = 'aeiouy'
        start = vowels + 'x'
        text = text.lower()
        text = "".join(x for x in text if x not in exclude)

        if text is None:
            return 0
        elif len(text) == 0:
            return 0
        else:
            if text[0] in start:
                count += 1
            try:
                if text[1] in vowels and text[0] not in start:
                    count +=1
            except:
                pass
            for index in range(2, len(text)):
                if text[index] in vowels and text[index-1] not in vowels:
                    count += 1
            if text.endswith('e'):
                count -= 1
            if text.endswith('le'):
                count += 1
            if count == 0:
                count += 1
                
            #For averaging purposes in later functions
            #If this function is changed you may have to change the coefficient
            count = count - (0.1*count)
            return count

    #Outputs the number of sentences in a given string
    def sentence_count(self, text):
        ignoreCount = 0
        sentences = text.translate(exclude)
        for sentence in sentences:
            if self.word_count(sentence) <= 2:
                ignoreCount = ignoreCount + 1
        return max(1, len(sentences) - ignoreCount)

    #Outputs mean length of sentence across a given string
    def avg_sentence_length(self, text):
        wc = self.word_count(text)
        sc = self.sentence_count(text)
        try:
            ASL = float(wc/sc)
            return round(wc/sc, 1)
        except:
            print("Error(ASL): Sentence Count is Zero, Cannot Divide")
            return

    #Outputs mean syllables per word in a given string
    def avg_syllables_per_word(self, text):
        syllable = self.syllable_count(text)
        words = self.word_count(text)
        try:
            ASPW = float(syllable)/float(words)
            return round(ASPW, 1)
        except:
            print("Error(ASyPW): Number of words are zero, cannot divide")
            return

    #Outputs mean number of letters per word
    def avg_letter_per_word(self, text):
        try:
            ALPW = float(float(self.char_count(text))/float(self.word_count(text)))
            return round(ALPW, 2)
        except:
            print("Error(ALPW): Number of words are zero, cannot divide")
            return

    #Outputs the reciprocal of (mean number of words per sentence)
    def avg_sentence_per_word(self, text):
        try:
            ASPW = float(float(self.sentence_count(text))/float(self.word_count(text)))
            return round(ASPW, 2)
        except:
            print("Error(AStPW): Number of words are zero, cannot divide")
            return

    #The following are function to determine complexity of a given string

    #https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
    #https://en.wikipedia.org/wiki/SMOG
    #https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
    #https://en.wikipedia.org/wiki/Automated_readability_index
    #https://en.wikipedia.org/wiki/Linsear_Write
    #https://en.wikipedia.org/wiki/Gunning_fog_index
    
    def flesch_reading_ease(self, text):
        ASL = self.avg_sentence_length(text)
        ASW = self.avg_syllables_per_word(text)
        FRE = 206.835 - float(1.015 * ASL) - float(84.6 * ASW)
        return round(FRE, 2)

    def flesch_kincaid_grade(self, text):
        ASL = self.avg_sentence_length(text)
        ASW = self.avg_syllables_per_word(text)
        FKRA = float(0.39 * ASL) + float(11.8 * ASW) - 15.59
        return round(FKRA, 1)

    def polysyllabcount(self, text):
        count = 0
        for word in text.split():
            wrds = self.syllable_count(word)
            if wrds >= 3:
                count += 1
        return count

    def smog_index(self, text):
        if self.sentence_count(text) >= 3:
            try:
                poly_syllab = self.polysyllabcount(text)
                SMOG = (1.043 * (30*(poly_syllab/self.sentence_count(text)))**.5) + 3.1291
                return round(SMOG, 1)
            except:
                print("Error(SI): Sentence count is zero, cannot divide")
        else:
            return 0

    def coleman_liau_index(self, text):
        L = round(self.avg_letter_per_word(text)*100, 2)
        S = round(self.avg_sentence_per_word(text)*100, 2)
        CLI = float((0.058 * L) - (0.296 * S) - 15.8)
        return round(CLI, 2)

    def automated_readability_index(self, text):
        chrs = self.char_count(text)
        wrds = self.word_count(text)
        snts = self.sentence_count(text)
        try:
            a = (float(chrs)/float(wrds))
            b = (float(wrds)/float(snts))
            ARI = (4.71 * round(a, 2)) + (0.5*round(b, 2)) - 21.43
            return round(ARI, 1)
        except Exception as E:
            print("Error(ARI) : Sentence count is zero, cannot divide")
            return None

    def linsear_write_formula(self, text):
        easy_word = []
        difficult_word = []
        text_list = text.split()

        Number = 0
        for i, value in enumerate(text_list):
            if i <= 101:
                try:
                    if self.syllable_count(value) < 3:
                        easy_word.append(value)
                    elif self.syllable_count(value) > 3:
                        difficult_word.append(value)
                    text = ' '.join(text_list[:100])
                    Number = float((len(easy_word)*1 + len(difficult_word)*3)/self.sentence_count(text))
                    if Number > 20:
                        Number /= 2
                    else:
                        Number = (Number-2)/2
                except Exception as E:
                    print("Error (LWF): ", E)
        return float(Number)

    def difficult_words(self, text):
        text_list = text.split()
        diff_words_set = set()
        for value in text_list:
            if value not in easy_word_set:
                if self.syllable_count(value) > 1:
                    if value not in diff_words_set:
                        diff_words_set.add(value)
        return len(diff_words_set)

    def dale_chall_readability_score(self, text):
        word_count = self.word_count(text)
        count = word_count - self.difficult_words(text)
        if word_count > 0:
            per = float(count)/float(word_count)*100
        else:
            print("Error(DCRS): Word Count is zero cannot divide")
            return None
        difficult_words = 100-per
        if difficult_words > 5:
            score = (0.1579 * difficult_words) + (0.0496 * self.avg_sentence_length(text)) + 3.6365
        else:
            score = (0.1579 * difficult_words) + (0.0496 * self.avg_sentence_length(text))
        return round(score, 2)

    def gunning_fog(self, text):
        try:
            per_diff_words = (self.difficult_words(text)/self.word_count(text)*100) + 5
            grade = 0.4*(self.avg_sentence_length(text) + per_diff_words)
            return grade
        except:
            print("Error(GF): Word Count is Zero, cannot divide")

    def text_standard(self, text):
        grade = []

        # Appending Flesch Kincaid Grade
        lower = round(self.flesch_kincaid_grade(text))
        upper = math.ceil(self.flesch_kincaid_grade(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Flesch Reading Easy
        score = self.flesch_reading_ease(text)
        if score < 100 and score >= 90:
            grade.append(5)
        elif score < 90 and score >= 80:
            grade.append(6)
        elif score < 80 and score >= 70:
            grade.append(7)
        elif score < 70 and score >= 60:
            grade.append(8)
            grade.append(9)
        elif score < 60 and score >= 50:
            grade.append(10)
        elif score < 50 and score >= 40:
            grade.append(11)
        elif score < 40 and score >= 30:
            grade.append(12)
        else:
            grade.append(13)

        # Appending SMOG Index
        lower = round(self.smog_index(text))
        upper = math.ceil(self.smog_index(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Coleman_Liau_Index
        lower = round(self.coleman_liau_index(text))
        upper = math.ceil(self.coleman_liau_index(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Automated_Readability_Index
        lower = round(self.automated_readability_index(text))
        upper = math.ceil(self.automated_readability_index(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Dale_Chall_Readability_Score
        lower = round(self.dale_chall_readability_score(text))
        upper = math.ceil(self.dale_chall_readability_score(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Linsear_Write_Formula
        lower = round(self.linsear_write_formula(text))
        upper = math.ceil(self.linsear_write_formula(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Gunning Fog Index
        lower = round(self.gunning_fog(text))
        upper = math.ceil(self.gunning_fog(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Finding the Readability Consensus based upon all the above tests
        d = dict([(x, grade.count(x)) for x in grade])
        sorted_x = sorted(d.items(), key=operator.itemgetter(1))
        final_grade = str((sorted_x)[len(sorted_x)-1])
        score = final_grade.split(',')[0].strip('(')
        return str(int(score)-1) + "th " + "and " + str(int(score)) + "th grade"

textstat = textstatistics()
