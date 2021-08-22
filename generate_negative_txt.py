import os
from fire import Fire
PATH_NAME = 'negative_images'

def main():

    if not os.path.exists(PATH_NAME):
        raise NotADirectoryError(f"Directory not found: {PATH_NAME}")

    with open('neg.txt', 'w') as file:
        for im_name in [f for f in os.listdir(PATH_NAME) if not f.startswith('.')]:
            file.write(im_name + '\n')

if __name__ == "__main__":
    Fire(main)
