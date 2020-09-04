# First Order Motion Model for Image Animation

This repository provides an improved usage for the project [First Order Motion Model for Image Animation](https://github.com/AliaksandrSiarohin/first-order-model). 

## Example animations

The videos on the left show the driving videos. The first row on the right for each dataset shows the source videos. The bottom row contains the animated sequences with motion transferred from the driving video and object taken from the source image. We trained a separate network for each task.

### VoxCeleb Dataset
![Screenshot](sup-mat/vox-teaser.gif)

### Installation and Usage
1. Create a virtual environment with dependecies. 

Since the model is dependent on a much odlder version of pytorch (1.0.0), we use Anaconda to manage dependencies.

Install anaconda on your local machine or server from [here](https://docs.anaconda.com/anaconda/install/).

Once anaconda is installed, create a virtual environment named deepfake. 
In your terminal, run:
```
conda create -n deepfake python=3.7
```
Verify that the new environment was installed correctly:
```
conda env list
```
Activate the enviroment you just created:
```
conda activate deepfake
```

Now you can download the repo and install dependencies:
```
cd first-order-model
pip install -r requirements.txt
```

2. Prepare data

We have prepared a sample video and an image under the folder ```mydata```. If you would like to crop videos and images on your own, refer to the ```Crop videos and images``` session below. Generally, the extact size of 256x256 for videos and images are not required, but you should use sources with similar scales and make sure the human face is in the middle of your video/image.

To run the demo, you also need to download a checkpoint of the model.
Checkpoints can be found under following link: [google-drive](https://drive.google.com/open?id=1PyQJmkdCsAkOYwUyaj_l-l0as-iLDgeH) or [yandex-disk](https://yadi.sk/d/lEw8uRm140L_eQ).
Select ```vox-adv-cpk.pth.tar```, download it and put under the ```mydata``` directory.



3.  Animation Demo

To run the demo and generate a video, run the following command:
```
python demo.py --relative --adapt_scale --config config/dataset_name.yaml --driving_video path/to/driving --source_image path/to/source --checkpoint path/to/checkpoint --result_video path/to/output --cpu
```
The result will be stored in ```output/result.mp4```.

Example command in our case: (In our example, we put the video, image and the checkpoint all under folder ```mydata```)
```
python demo.py  --relative --adapt_scale --config config/vox-adv-256.yaml --driving_video mydata/unravel.mp4 --source_image mydata/girl.png --checkpoint mydata/vox-adv-cpk.pth.tar --result_video output/result.mp4  --cpu
```
If you have GPU on your computer, delete the ```--cpu``` flag.

You shoule obtain an animated video ```result.mp4``` under ```output```.

### Crop videos and images

The driving videos and source images should be cropped (or at least the human-face/object is in the middle of your image) before it can be used in our method. To obtain some semi-automatic crop suggestions you can use ```python crop-video.py --inp some_youtube_video.mp4```. It will generate commands for crops using ffmpeg. In order to use the script, face-alligment library is needed:
```
git clone https://github.com/1adrianb/face-alignment
cd face-alignment
pip install -r requirements.txt
python setup.py install
```

We also provide a piece of code for resize images in python.

TODO: fix bug in crop-video.py and improve crop-img.py

### Face-swap
It is possible to modify the method to perform face-swap using supervised segmentation masks.
![Screenshot](sup-mat/face-swap.gif)
For both unsupervised and supervised video editing, such as face-swap, please refer to [Motion Co-Segmentation](https://github.com/AliaksandrSiarohin/motion-cosegmentation).

