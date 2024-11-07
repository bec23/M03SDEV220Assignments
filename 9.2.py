#define a generator function called get_odds() that returns odd numbers from range(10). use for loop to find and print the third value returned
def get_odds():
    for number in range(10):
        if number %2 != 0:
            yield number
odds = get_odds()
for i, value in enumerate(odds):
    if i ==2:
        print(value)
        break