import string
import tkinter

def choose_file(): 
    import tkinter
    from tkinter import filedialog
    root_window = tkinter.Tk()
    root_window.withdraw()
    return filedialog.askopenfilename()


def read_words(x):
        words = []
        for a in range(len(x)):
                line = x[a]
                line = line[:-2]
                table = str.maketrans({key: None for key in string.punctuation})
                line_pure = line.translate(table)
                words_split = line_pure.split()
                if words_split == []:
                        continue
                for b in range(len(words_split)):
                        words.append(str(words_split[b]).lower())
        return words

def ignored_words(l):
        ignored=[]
        for b in range(len(l)):
                ignore_split = l[b].split()
                ignored.append(ignore_split[0])
        return ignored


def word_to_count(total_word, words_to_ignore):
        wtc=[]
        for z in range(len(total_word)):
                if total_word[z] not in words_to_ignore and total_word[z] not in wtc:
                        wtc.append(total_word[z])
        return wtc

def count_the_words(word_to_be_counted, total_word):
        final=[]
        for i in range(len(word_to_be_counted)):
                theword = word_to_be_counted[i]
                numofword = total_word.count(theword)
                final.append([numofword, theword])
        final.sort(reverse=True)
        final = final[:56]
        return final



def main():
        file1 = open("CommencementSpeechByGates2014.txt", "r")
        splitlines = file1.readlines()
        
        word = read_words(splitlines)
        
        '''
        for a in range(len(splitlines)):
                line = splitlines[a]
                line = line[:-2]
                table = str.maketrans({key: None for key in string.punctuation})
                line_pure = line.translate(table)
                words_split = line_pure.split()
                if words_split == []:
                        continue
                for b in range(len(words_split)):
                        words.append(str(words_split[b]).lower())
        '''

        file2 = open("stopWords.txt", "r")
        ignore = file2.readlines()

        wti = ignored_words(ignore)
        print(wti)

        '''
        ignored=[]
        for b in range(len(ignore)):
        ignore_split = ignore[b].split()
        ignored.append(ignore_split[0])
        '''

        wtc = word_to_count(word, wti)
        print(wtc)
        '''
        wtc=[]
        for z in range(len(word)):
        if word[z] not in wti and word[z] not in wtc:
                wtc.append(word[z])
        '''
        result = count_the_words(wtc, word)

        '''
        final=[]
        for i in range(len(wtc)):
        theword = wtc[i]
        numofword = words.count(theword)
        final.append([numofword, theword])

        final.sort(reverse=True)
        final = final[:56]
        print(final)
        '''

        print(result)