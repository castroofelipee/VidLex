import time
import random
import string
import subprocess
import platform


################################################
#               Windows System                 #
################################################
def open_notepad_and_write():
    system = platform.system()
    duration = 10 * 60  
    start_time = time.time()
    
    if system == 'Windows':
        subprocess.Popen(['notepad.exe'])
        time.sleep(5)  

        while time.time() - start_time < duration:
            text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            for char in text:
                subprocess.call(['powershell', '-Command', f'$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys("{char}")'])
                time.sleep(random.uniform(0.05, 0.2))  
            time.sleep(random.uniform(0.5, 2))


    ################################################
    #     Linux (Ubuntu, Pop_Os, Fedora) System    #
    ################################################
    elif system == 'Linux':
        tmp_file_path = '/tmp/random_text.txt'

        with open(tmp_file_path, 'w') as file:
            file.write('')

        subprocess.Popen(['xdg-open', tmp_file_path])
        time.sleep(5)  

        while time.time() - start_time < duration:
            text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        
            with open(tmp_file_path, 'a') as file:
                for char in text:
                    file.write(char)
                    file.flush()  
                    time.sleep(random.uniform(0.05, 0.2))  
                file.write('\n')
            time.sleep(random.uniform(0.5, 2))  

    print("Writing task completed.")
