print('Please write the number to convert')
money = float(input())

# course, ua_usd == convert ua in usd
ua_usd, usd_ua = 37.99, 37.39
ua_eur, eur_ua = 41.10, 40.10

print(f'{money:.2f}', 'UAH --> USD', f'{money / ua_usd:.2f}', '\n'
      f'{money:.2f}', 'USD --> UAH', f'{money * usd_ua:.2f}', '\n'
      f'{money:.2f}', 'UAH --> EUR', f'{money / ua_eur:.2f}', '\n'
      f'{money:.2f}', 'EUR --> UAH', f'{money * eur_ua:.2f}')
