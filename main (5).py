def main():
  print("FreeCodeCamp Code 6")

  num = 0
  tot = 0.0

  while True:
    sval = input("Ingresa un número: ")
    if sval == "done":
      break
    try:
      fval = float(sval)
    except:
      print("Valor Invalido")
    num += 1
    tot = tot + fval

  print(tot,num,tot/num)

if __name__ == "__main__":
  main()