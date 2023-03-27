def computepay(hours, rate):
  print("In pomputepay",hours,rate)
  if hours > 40:
    reg = rate * hours
    otp = (hours - 40.0) * (rate * 0.5)
    pay = reg + otp
  else:
    pay = hours * rate
  print("Returning", pay)
  return pay

print("FreeCodeCamp Code 5")
sh = input("Igrese las horas: ")
sr = input("Ingrese la tasa: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pago:",xp)