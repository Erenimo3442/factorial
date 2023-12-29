while True:
  try:
    deger = int(input("Sayı giriniz: "))
    if deger > 0:
      break
    elif deger == 0:
      deger = 1
      break
    else:
      print("Hatalı giriş")
      continue
  except:
    print("Hatalı giriş")
    continue

fac_deger = deger - 1

while fac_deger > 1:
  deger = deger * fac_deger
  fac_deger -= 1

print(f"Sayınızın faktoriyel değeri : {deger}")