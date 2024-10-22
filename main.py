import time, os



while True:

  f = open("README.txt", "a+")
  print("HIGH SCORE TABLE")
  print()
  print()

  initials = input("INITIALS > ")
  score = input("SCORE > ")
  f.write(f"{initials} {score}\n")
  print()
  print("ADDED")

  
  time.sleep(2)
  os.system("clear")

  f.close()