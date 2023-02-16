# To enable GPU acceleration
1. download vscommunity and download desktop C++ package
2. download CUDA Toolkit. In my case, i'm using Version 11 and download exe(local)
3. download NVIDIA cuDNN (you may need to sign in to download this package).
4. Once down copy the bin, include and bin files into CUDA directory which can be found in NVIDIA GPU Computing program files ../CUDA/version
5. Uninstall all installed pytorch using pip uninstall torch, torchvision and torchaudio to prevent the conflict with cuda version
6. Go to https://pytorch.org/get-started/locally/ and select pip, cuda 11.6 and copy pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116 into terminal
7. You're done !

# To train custom model
1. download model from roboflow 
2. download as zip. Extract this file and copy it later to google drive
3. From google drive, create "construction_model" and extract downloaded files into this directory.
4. mount google colab to access the drive using this command

# Google colab link
https://colab.research.google.com/drive/1xUC9W2tIsSR0qiHSFpfBUqwtX4MbxBGU#scrollTo=lOG1LplnDx99

## Mount drive
from google.colab import drive
drive.mount('/content/drive')

## Run NVIDIA-SMI to determine resource and ensure GPU is used to train the model
!nvidia-smi

## Install yolo packages
!pip install ultralytics
from ultralytics import YOLO

## Run below command to check our import is workin
!yolo task=detect mode=predict model=yolov8l.pt conf=0.25 source="https://ultralytics.com/images/bus.jpg"

## Custom Data Training
1. First edit data.yaml 
2. Please ensure "path" variable is there and pointed to correct "Construction safety" as follow:
path: ../drive/MyDrive/Construction_Safety
train: ../train/images
val: ../valid/images
test: ../test/images

## If done, run below command to run our custome training
!yolo task=detect mode=train model=yolov8l.pt data=../content/drive/MyDrive/Construction_Safety/data.yaml epochs=50 imgsz=640

## Output Files 
go to "runs --> detect -> train -> weights -> best.pt"
download this best.pt to be used in the script
