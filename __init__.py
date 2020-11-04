import random
import uuid

class GenData:
    """Params:
    fpath: desired path and name of files to write data to
    size: desired size of generated data in GB
    """
    
    def __init__(self, fpath='./data.csv', size=1):
        self.fpath = fpath
        self.size = size
    
    def generate(self):
        outfile = self.fpath

        # 1GB = 1024 * 1024 * 1024 
        outsize = (1024 * 1024 * 1024) * self.size

        with open(outfile, 'w') as csvfile:
            size = 0
            headers = 'id_field,random_50a,random_50b,random_range\n'
            csvfile.write(headers)
            while size < outsize:
                txt = f'{uuid.uuid4()},{round(random.random()*50,6)},{round(random.random()*50,6)},{random.randrange(1000)}\n'
                size += len(txt)
                csvfile.write(txt)