import os

dir = os.listdir()

for each in dir:
    if each != 'webp.py' and each[-4:] != 'webp':
        os.system(f'ffmpeg -i {each} {each.split('.')[0]}.webp')
        os.remove(each)
# os.system('pause')
print('Success!')    
