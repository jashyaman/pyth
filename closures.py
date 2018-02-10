lcnt = 0
def function1(listOfSentences):
    rtnLst = []



    def closureFn(cnt):
        global lcnt
        print("letter count current value %d " % lcnt)
        lcnt = lcnt + cnt
        print("letter count new value %d " % lcnt)


    for sentence in listOfSentences:
        charCount = len(sentence)
        listOfWords = sentence.split(" ")
        #print(len(listOfWords))
        rtnLst.append(len(listOfWords))
        closureFn(len(listOfWords))
    return rtnLst




inputList = ['helo mi llamo shyam','hola my name is shyam','traceback should reveal that more effort is need to produce results']
rtnList = function1(inputList)
print(rtnList)

inputList2 = ['fresh list of new word bodies to count','perhaps some effort in self restraint is the key']
rtnList2 = function1(inputList2)
print(rtnList)

#not convinced with this example of closures. but will not push too hard as of now.
