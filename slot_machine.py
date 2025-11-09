import random 
symbols = ["⚪️","⬜️","🤍","💎"]
balance = 1000

print('='*60)
print('='*60)
print('Welcome to symbiosis slot machine club')
print('symbols = ⚪️ ⬜️ 🤍 💎')
print('='*60)
print('='*60)

while balance > 0 :
  print(f'your balance:{balance}')
  bet =input('enter your bet amount:')

  if not bet.isdigit():
    print('please enter a number')
    continue
  bet = int(bet) 
  if bet<=0:
    print('bet must be greater than zero')
    continue
  if bet >balance:
    print('not enough money')
    continue


  #place the bet 
  balance-=bet
  row =[random.choice(symbols) for _ in range(3)]
  print('spining.....')
  print('|'.join(row))
  if row[0]==row[1]==row[2]:
    if row[0]=='⚪️':
      win=bet*2
    elif row[0]=='⬜️':
      win=bet*3
    elif row[0]=='🤍':
      win=bet*5
    else:#💎
      win=bet*10
    print(f'congrats you won Rs.{win}')
    balance+=win
  else:
    print('you lost this round')
  try_again = input('spin again??(Y/N):').upper()
  if try_again !="Y":
    break
print('#'*60)
print(f'game over! final balance:{balance}')
print('#'*60)




    
