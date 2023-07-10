import subprocess
import os, signal

def kill_process(grep_str, user):   
  ps_output = subprocess.check_output(('ps', 'aux')).decode('ascii')

  for line in ps_output.split("\n"): 
    if grep_str in line:
      fields = line.split()

      ps_user = fields[0]
      ps_pid = fields[1]

      # kill process if it is started by user
      if ps_user==user:
      	print("Killing ", line)
      	os.kill(int(ps_pid), signal.SIGKILL)      	



grep_str = "home/nemsys/.local/bin/bpython"
user = "nemsys"

kill_process(grep_str, user)

