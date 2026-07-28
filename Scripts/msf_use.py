import os
import subprocess as sb 

searchploit=input("Give the (exploit or auxilary or file or payload) from metasploit = ")
msfcom = f"""use {searchploit}; show options;"""

execute = sb.run(["msfconsole", "-q", "-x", msfcom])

print(execute)
