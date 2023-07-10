try:
  raise ValueError
except ValueError:
  print("/"*30)
  print("ValueError")
  print("\\"*30)
  raise
except Exception:
  print("@"*30)
  print("Exception")
  print("@"*30)
