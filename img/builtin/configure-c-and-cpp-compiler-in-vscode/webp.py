import os

dir = os.listdir()

for each in dir:
    if each != 'webp.py':
        os.system(f'ffmpeg -i {each} {each[:-3]}webp')
        os.remove(each)

print('Success!')    
