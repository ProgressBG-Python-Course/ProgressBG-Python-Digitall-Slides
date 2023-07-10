import subprocess

def open_vscode(directory):
  """open VS Code editor and load given directory"""
  cmd = "code"	

  subprocess.call([cmd, directory,"-n"])

open_vscode("/data/python_demos/music")