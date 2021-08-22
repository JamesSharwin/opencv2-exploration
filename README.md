# My intro to object detection with OpenCV2

A repo of my exploration of open-cv, started with the idea of being able to detect when my cat is on webcam, spiralled 
from there.

OpenCV2 includes an out-of-the box cat classifier(s): `haarcascade_frontalcatface.xml` and 
`haarcascade_frontalcatface_entended.xml`. These are fairly decent at getting most cat faces, but for some reason 
struggled with my cat, Hammy.

<img alt="Picture of my cat" src="random/hammy.png?raw=true" title="Hammy" width="300"/>
<img alt="Picture of alternative feline" src="random/generic_cat.png?raw=True" title="Hammy" width="300"/>

# Pre-requisites

Python3 installation with opencv (v4.x) `pip install opencv-python`

# Making the training data for a HAAR Cascade Classifier

So, basically for training we need a decent sized set of positive images (containing the thing you are trying to detect), 
as well as a set of negative images of similar composition, but not containing your target object. At least 100 of each 
is a good benchmark.

In root there is a folder for negative images (`negative_images`) and one for positive images 
(`positive_images`), you can either drop your own existing photos into these folders, or you can use the `capture_webcam` 
function which will add a timelapse series of images from your webcam to, the `raw_images` folder, from here you can run 
`categorise.py` and each photo will appear and you can press `p` for a positive image, `n` for a negative image, `i` for 
an inconclusive image, and these will be moved to the appropriate folders accordingly.

From here there are a few more steps. You need to make summary files of the negative and positive images you have captured.
Starting with the negatives, simply run `generate_negative_txt.py` and a file called `neg.txt` will be generated.

The positive images are a bit more involved, and this is where our opencv v3 docker image comes into play. The steps for 
this are:

1. Pull this handy pre-made docker image (V3) `docker pull jjanzic/docker-python3-opencv:contrib-opencv-3.4.2`
2. Build through docker desktop - including mounting the project directory, so you can access files between your local 
repo and your docker instance.
3. Run you v3 container: `docker exec -it opencv3  /bin/bash` 

From within the bash terminal of your docker image you can then run the scripts necessary to generate the summary of the 
positive images.

Run this to annotate your images - basically click once to start a box, drag, and click again to expand and finish that 
box, follow the instructions printed in the terminal to see how you accept changes and move on to the next image.
`opencv_annotation --annotations=pos.txt --images=positive/`. This should result in a file called `pos.txt` being 
generated in root.

This command will then generate a vector file needed to train the HAAR cascade model.
`open_createsamples -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec`

Finally, to train your model:
`opencv_traincascade -data cascade -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 200 -numNeg 100`.

Then you should have a nice model generated in `cascade` called `cascade.xml`.

Running `main.py` will implement this on your live webcam feed.