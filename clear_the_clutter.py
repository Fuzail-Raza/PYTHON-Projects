import os
import random
import string


# def generate_random_name(length):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for _ in range(length))

# extensions=['txt','png','pdf']

# if not os.path.exists("data"):
#     os.mkdir("data")
# for i in range(1,20):
#     ext=random.choice(extensions)
#     os.mkdir(f"data/{generate_random_name(i)}.{ext}")

def ext_choice(exten):
    i=1
    for files in os.listdir('data'):
        if(files.endswith(f'.{exten}')):
            os.rename(f"data/{files}",f"data/{i}.{exten}")
            i+=1
        print(files)

ext_choice('png')