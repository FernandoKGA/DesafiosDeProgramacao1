#His goal is to minimize the sum of numbers written on
#remaining (not discarded) cards.

#he can discard at most, 2 or 3 cards with same number
#he wont discard if its impossible to choose two or 3 cards

#find the minimum sum of numbers on remaining cards

#maximize the number of removals

def cardsFrequencyIsDiffFromOne(cards):
    cardsFrequency = {}
    for card in cards:
        if card not in cardsFrequency:
            cardsFrequency[card] = 1
        else:
            cardsFrequency[card] += 1
    if len(cardsFrequency) == 5:
        return cardsFrequency, False
    else:
        return cardsFrequency, True

def fiveCards(cards):
    (cardsFrequency, isValid) = cardsFrequencyIsDiffFromOne(cards)
    if isValid:
        minimumSum = {}
        for card in cardsFrequency.keys():
            if cardsFrequency[card] >= 2:
                bulkCopyOfCards = cards.copy()
                i = 0
                if cardsFrequency[card] == 2:
                    while i < 2:
                        bulkCopyOfCards.remove(card)
                        i += 1
                else:
                    while i < 3:
                        bulkCopyOfCards.remove(card)
                        i += 1
                minimumSum[sum(bulkCopyOfCards)] = card
                    
        lenMinSum = len(minimumSum)
        if lenMinSum == 1:
            print(int(list(minimumSum.keys())[0]))
        else:
            if lenMinSum >= 2:
                minimumSumNumber = min(minimumSum.keys())
                print(minimumSumNumber)
    else:
        print(sum(cards))

cards = list(map(int,input().split()))
fiveCards(cards)
