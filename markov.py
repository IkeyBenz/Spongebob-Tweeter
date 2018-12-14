import pickle

markovFile = open('chain.pickle', 'rb')
starterFile = open('starters.pickle', 'rb')

markovChain = pickle.load(markovFile)
sentenceStarters = pickle.load(starterFile)
