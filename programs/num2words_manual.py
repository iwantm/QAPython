ones = list(range(0, 10))  # 1-10
elevens = list(range(10, 21))  # 10-20
tens = list(range(30, 101, 10))  # 30-100
bigs = list(10**x for x in range(3, 12+1, 3))

ones_words = (' ', 'one', 'two', 'three', 'four', 'five',
              'six', 'seven', 'eight', 'nine')

elevens_words = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                 'seventeen', 'eighteen', 'nineteen', 'twenty')

tens_words = ('thirty', 'forty', 'fifty', 'sixty',
              'seventy', 'eighty', 'ninety', 'hundred')

bigs_words = ('thousand', 'million', 'billion', 'trillion')

num2word = {}

for number, word in zip(bigs + tens + elevens + ones,
                        bigs_words + tens_words + elevens_words + ones_words):
    num2word[number] = word


def to_word(num):
    if num <= 20:
        return num2word[num]
    elif num < 100:
        divided = num//10 * 10
        remaining = num % 10
        return(num2word[divided] + ' ' + num2word[remaining])
    elif num < 1000:
        divided = num//100
        remaining = num % 100
        return(num2word[divided] + ' hundred and ' + to_word(remaining))
    for big in bigs[::-1]:
        if num/big > 1:
            return(to_word(num//big) + ' ' + num2word[big] + ", " + to_word(num % big))
