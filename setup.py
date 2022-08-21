from subprocess import check_call, DEVNULL
from sys import exit as sysExe, executable as exe
from pkg_resources import working_set
from urllib.request import urlopen

def internet_is_available(host='http://www.google.com'):
    try:
        urlopen(host)
        return True
    except:
        return False

# A basic procedure to install modules that are not present in the system - thanks, Girrafish! 
# (https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t)
def _setup():
    if not internet_is_available():
        sysExe("No internet connection")
    
    required = {'xlrd', 'tk', 'IPython', 'numpy', 'openpyxl', 'pandas', 'requests'}
    installed = {i.key for i in working_set}
    missing = required - installed
    
    if missing:
        check_call([exe,'-m','pip','--disable-pip-version-check','install',*missing], stdout=DEVNULL) # I shouldn't disable pip version check, but that looked untidy