import random

user_id = '1234'
username = 'Ivan Ivanov'
money_lost_balance_about_last_month = 0

print(f'Welcome to the Slot Machine Game!\nHello {username}')

symbols = ["🍒", "🍊", "🍋", "🍇", "🔔", "💎"]

balance = int(input('Enter your initial balance: '))

bet = 0

while balance > 0:
    print(30 * '-')
    print('Current Balance:', balance)

    while True:
        bet = int(input('Enter your bet amount (0 to exit): '))

        if bet == 0:
            break

        if bet > balance:
            print('Insufficient balance. Please a lower bet!')
        else:
            break

    if bet == 0:
        break

    balance -= bet

    print('Spinning the reels...')
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    if user_id == '1234' and money_lost_balance_about_last_month >= 1000:
        print(reel1, reel1, reel1)
        winnings = bet * 10
        balance += winnings
        print('Congratulations! You won Jackpot', winnings, 'money!')
        money_lost_balance_about_last_month = 0
        continue

    print(reel1, reel2, reel3)

    if reel1 == reel2 == reel3:
        winnings = bet * 10
        balance += winnings
        print('Congratulations! You won Jackpot', winnings, 'money!')

    elif reel1 == reel2 or reel2 == reel3:
        winnings = bet * 2
        balance += winnings
        print('Congratulations! You won', winnings, 'money!')

    else:
        money_lost_balance_about_last_month += bet
        print('Sorry! No match. Better luck next time!')

if balance <= 0:
    print('Game over. Final balance:', balance)
    