from decouple import config
from logic import chek_win, chek_bet

MY_MONEY = int(config('MY_MONEY'))

print(f"Добро пожаловать в игру Казино! У вас на счету {MY_MONEY}$")

while True:
    bet_slot = input("Выберите число от 1 до 30 или 'q' для выхода: ")
    if bet_slot == "q":
        break

    bet_slot = chek_bet(bet_slot)
    if bet_slot is None:
        continue

    bet_money = int(input("Сколько вы хотите поставить? "))
    bet_money = chek_bet(bet_money, MY_MONEY)
    if bet_money is None:
        continue

    MY_MONEY -= bet_money
    result = chek_win(bet_slot)
    if result:
        MY_MONEY += bet_money * 2
        print(f"Вы выиграли! Вам начислено {MY_MONEY} долларов.")
    else:
        print(f'Вы проиграли! Вы потеряли {MY_MONEY} долларов.')

    play_again = input("Хотите сыграть еще? (Да/Нет) ")
    if play_again.lower() == "нет" or play_again.lower() == "no":
        print(f"Игра окончена. Ваш итоговый капитал {MY_MONEY} долларов.")
        break

