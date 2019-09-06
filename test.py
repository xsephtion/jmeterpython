import os
import subprocess

def run():
    dir = os.getcwd()
    jmeter = "\\jmeter\\bin\\"
    jmx = "\\test\scripts\\"
    setpath = "SET PATH=%PATH%;" + jmeter

    subprocess.call(setpath, shell=True)
    filename = "script1.jmx"
    script = dir+jmx+filename
    print(script)
    task = dir + jmeter + 'jmeter.bat -n -t ' + script + ' -l  testResults.jtl'
    print(task)
    proc = subprocess.Popen(task, shell=True, stdout=subprocess.PIPE )
    out = proc.communicate()
    print(out)
    input()


run()