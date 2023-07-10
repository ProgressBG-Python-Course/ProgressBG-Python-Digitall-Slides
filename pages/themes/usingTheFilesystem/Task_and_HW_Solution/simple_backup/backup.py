import os
import datetime

def backup(src, dest, timestamp):
  """Backup files in src folder into dest folder.
      Do not remove the files in source folder.
      To each file attach suffix with current timestamp in the format '%Y-%m-%d_%H_%M_%S%'

    Args:
        src (string): Source folder
        dest (string): Destination folder

    Example:
      src/track5.mp3 => dest/track5.mp3_2018-04-12_18-30-45
    """

  # get list of all file/dir names in source folder
  entries = os.listdir(src)

  for filename in entries:
    src_full_filename = src+filename
    dest_full_filename = dest+filename+"_"+timestamp
    os.rename(src_full_filename, dest_full_filename)


def get_timestamp():
  #get the current local date-time
  cldt = datetime.datetime.today()

  # get the timestamp as a string with given format
  timestamp = datetime.datetime.strftime(cldt, '%Y-%m-%d_%H_%M_%S')

  return timestamp


###########################################################
# MAIN
###########################################################
# set the source and destination paths for the backup
# note, the trailing foreword slash is important
src = "../data/"
dest = "./"

timestamp = get_timestamp()
print(timestamp)

backup(src, dest, timestamp)