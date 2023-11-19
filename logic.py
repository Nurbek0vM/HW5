from random import randint

def chek_win(bet_slot):
    win_lsot = randint(1,30)
    return bet_slot == win_lsot

def chek_bet(bet, max_bet=None):
    try:
        bet = int(bet)
    except ValueError:
        print('Пожалуйста, введите число. ')
        return None
    if max_bet and bet > max_bet:
        print("У вас недостаточно средств для ставки.")
        return None
    return bet