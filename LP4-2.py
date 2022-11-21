def main():
  weight = int(input("enter package weight in kg:"))
  length = int(input("enter package length in cm:"))
  width = int(input("enter package weight in cm:"))
  height = int(input("enter package weight in cm:"))
  heav = 0
  lar = 0 
  if weight > 27:
    heav = 1
  if length * width * height > 100000:
    lar = 1
  if heav == 1 and lar == 0:
    print("too heavy")
  if heav == 0 and lar == 1:
    print("too large")
  if heav == 1 and lar == 1:
    print("too heavy and too large")
  pass


if __name__ == "__main__":
  main()