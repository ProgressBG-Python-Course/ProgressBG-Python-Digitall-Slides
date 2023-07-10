import subprocess
""" #google-chrome  --profile-directory="Profile 7" https://mail.google.com http://wwwcourses.github.io/ProgressBG-Python &"""

def load_browser_profile_not_correct(profile, urls_list):
	"""open Chrome browser in new window, 
	   with the given user profile and loads the specified URLs

	   Declaimer: for browser task automation is better to use the built-in webbrowser module 
	   #google-chrome  
	        --profile-directory="Profile 7" 
	        https://mail.google.com 
	        http://wwwcourses.github.io/ProgressBG-Python &
	"""

	cmd = "google-chrome"

	args = (		
		"--profile-directory='{:s}'".format(profile),
		*urls_list
	)

	print(args)
	subprocess.call([cmd, *args])

def load_browser(profile, url):
	"""open Chrome browser in new window, 
	   with the given user profile and loads the specified URLs

	   Declaimer: for browser task automation is better to use the built-in webbrowser module 
	"""
	cmd = "google-chrome"
	args = "--new-window --profile-directory=" + "'{:s}' {:s}".format(profile, url)

	subprocess.call(cmd + " " + args, shell=True)	

	

urls_to_load = [
	"https://mail.google.com",
	"http://wwwcourses.github.io/ProgressBG-Python"
]


load_browser("Profile 7",  " ".join(urls_to_load))