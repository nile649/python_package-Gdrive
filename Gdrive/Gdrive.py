import subprocess
import os

class Gdrive:
    def __init__(self):
        self.path = os.getcwd()   
    def __call__(self,fileId:str,OutId:str)->None:
        path = subprocess.Popen(['which','python'], stdout=subprocess.PIPE).communicate()[0].decode('ascii')[:-7]
        file = path+'Gdrive.sh'
#         subprocess.check_call(['chmod','+x',file])
        subprocess.check_call([file, fileId, OutId])
        return None
        

if __name__ == '__main__':
    gdrive = Gdrive()
    gdrive("1Z1RqRo0_JiavaZw2yzZG6WETdZQ8qX86", "lol2.zip")
        
