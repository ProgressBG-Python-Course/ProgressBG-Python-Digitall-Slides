import subprocess

def open_terminal(profile, directory):
	"""open a terminal with a custom profile in the given directory"""
	cmd = "gnome-terminal"
	args = (
		"--window-with-profile",profile, 
		"--working-directory",directory
	)

	subprocess.call([cmd, *args])

open_terminal("day", "/data/python_demos/music")