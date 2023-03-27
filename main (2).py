def main():
  print("FreeCodeCamp Code 3\n")

  sh = input("Ingrese las Horas: ")
  sr = input("Ingrese la Tasa: ")
  fh = float(sh)
  fr = float(sr)

  if fh > 40:
    print("OverTime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    print(reg,otp)
    xp = reg + otp
  else:
    print("Regular")
    xp = fh * fr
  print("Pago:",xp)

if __name__ == "__main__":
  main()