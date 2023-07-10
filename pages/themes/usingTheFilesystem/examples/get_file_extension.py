import os.path

filename = "/data/new/test.txt"
extension = os.path.splitext(filename)[1][1:]

print(extension)