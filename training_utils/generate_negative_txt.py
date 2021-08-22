import os
from fire import Fire
PATH_NAME = 'negative_images'

def main():
    with open('training_assets/neg.txt', 'w') as file:
        for im_name in [f for f in os.listdir(PATH_NAME) if not f.startswith('.')]:
            file.write(im_name + '\n')

if __name__ == "__main__":
    Fire(main)
