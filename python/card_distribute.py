
def card_distribute(number, cards):
    return [cards[i::number][:len(cards) // number] for i in range(number)]

assert card_distribute(3, ['SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK']) == [['SA', 'S4', 'S7', 'S10'], ['S2', 'S5', 'S8', 'SJ'], ['S3', 'S6', 'S9', 'SQ']]


