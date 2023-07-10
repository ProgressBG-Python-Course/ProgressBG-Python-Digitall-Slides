import os
import subprocess


def open_terminal(profile, directory):
	cmd = "gnome-terminal"
	args = (
		"--window-with-profile",profile, 
		"--working-directory",directory
	)

	subprocess.call([cmd, *args])

def load_browser(profile, url):
	"""open Chrome browser in new window, 
	   with the given user profile and loads the specified URLs

	   Declaimer: for browser task automation is better to use the built-in webbrowser module 
	"""
	cmd = "google-chrome"
	args = "--new-window --profile-directory=" + "'{:s}' {:s}".format(profile, url)

	subprocess.call(cmd + " " + args, shell=True)
	#google-chrome  --profile-directory="Profile 7" https://mail.google.com http://wwwcourses.github.io/ProgressBG-Python &

def open_vscode(directory):
	cmd = "code"	

	subprocess.call([cmd, directory])


# project folder
project_path = "/data/python_demos/music"

urls_to_load = [
	"https://mail.google.com",
	"http://wwwcourses.github.io/ProgressBG-Python"
]
urls_to_load_str = " ".join(urls_to_load)


# automate starting process:
open_terminal("Default", project_path)
# load_browser("Profile 7",  urls_to_load_str)
# open_vscode(project_path)