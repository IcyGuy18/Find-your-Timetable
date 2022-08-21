import subprocess
import sys
import pkg_resources
import urllib.request
import pip

def internet_is_available(host='http://www.google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

# A basic procedure to install modules that are not present in the system - thanks, Girrafish! 
# (https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t)
def _setup():
    if not internet_is_available():
        sys.exit("No internet connection")
    
    required = {'xlrd', 'tk', 'IPython', 'numpy', 'openpyxl', 'pandas', 'requests'}
    installed = {i.key for i in pkg_resources.working_set}
    missing = required - installed
    
    if missing:
        subprocess.check_call([sys.executable,'-m','pip','--disable-pip-version-check','install',*missing], stdout=subprocess.DEVNULL) # I shouldn't disable pip version check, but that looked untidy