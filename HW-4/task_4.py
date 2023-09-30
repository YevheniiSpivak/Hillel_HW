# Ви маєте список ['Tst', 'aBc', 'TEST', 'Hello', "neW'],
# відсортуйте його, але врахуйте що слова в списку можуть  починатися з великої або малої літери

lst = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
lst.sort(key=str.lower)

print(lst)
