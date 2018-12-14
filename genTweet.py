import random
class TweetGenerator:
    
    def __init__(self, chain, starters):
        self.dictogram = chain
        self.sentenceStarters = starters
    
    def probableWordFrom(self, dictogram):
        ''' Picks a random word from histogram containing words and weights '''
        words, weights = zip(*dictogram.items())

        # Creates a list of integers, which act as separators between weights
        accumulator, separators = 0, []
        for weight in weights:
            accumulator += weight
            separators.append(accumulator)

        # The indices of the words lst and seperators lst are concurrent
        # Here we return the word at index of whichever weight in the separators lst
        # is greater than this random number
        rand = random.randint(0, accumulator)
        for index, separator in enumerate(separators):
            if rand <= separator:
                return words[index]

    def makeSentence(self):
        ''' Generates a sentence using the sentence starters and markov chain '''
        # Starts the words list out with two randomly chosen words from the sentence starters dict
        words = list(self.probableWordFrom(self.sentenceStarters))

        # Generates a new word based on the previous two words
        newWord = self.probableWordFrom(self.dictogram[(words[-2], words[-1])])

        # Every sentence ends with a '###' character to signify it ended
        while newWord != '###':
            words.append(newWord)
            newWord = self.probableWordFrom(self.dictogram[(words[-2], words[-1])])
        
        sentence = ' '.join(words)
        sentence = sentence[0].upper() + sentence[1:]
        return sentence
