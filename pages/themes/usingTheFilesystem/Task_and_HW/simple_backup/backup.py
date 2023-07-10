# Backup the all the files in data folder

def backup(src, dest):
  """Backup files in src folder into dest folder.
    Do not remove the files in source folder.
    To each file attach suffix with curent timestamp in the form
    '2018-04-12_18-30-45'
  
  Args:
      src (string): Source folder
      dest (string): Destination folder

  Example:
    /src/track5.mp3 => /dest/track5.mp3_2018-04-12_18-30-45  
  """
