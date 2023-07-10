password = "abracadabra"
user_pass = input("Enter your password:")
tries = 0

while tries < 3:
  if user_pass == password:
    break
  else:
    user_pass = input("Enter your password:")

  tries += 1

print("Nice, your user_name is: ", user_name)
