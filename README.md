# DPH
This project is for a course named Machine Learning which asks us to realize a method to optimize image search in unbalanced datasets ["Deep Priority Hashing"](https://github.com/thuml/DPH/tree/master/data).

## Prerequisites
Python3

## Datasets
We use ImageNet, NUS-WIDE in our experiments. You can download the ImageNet dataset and NUS-WIDE dataset [here](https://drive.google.com/drive/folders/0B7IzDz-4yH_HOXdoaDU4dk40RFE?usp=sharing).
After downloading, you need to move the imagenet.tar.gz to [./data/images_imagenet](./data/images_imagenet) and extract the file there.
```
mv imagenet.tar.gz ./data/images_imagenet
cd ./data/images_imagenet
tar -zxvf imagenet.tar.gz
```
Also, for NUS-WIDE, you need to move the nus_wide.tar.gz to ./data/nuswide (You need to Add a new Folder for 'nuswide') and extract the file there. 
```
mv nus_wide.tar.gz ./data/nuswide
cd ./data/nuswide
tar -zxvf nus_wide.tar.gz
```

You can also use more txt file to train model or evaluate it. You can replace the txt files where are located in ./data/imagenet or ./data/nuswide_81 folder of [here](https://github.com/thuml/DPH) as you like. Each line in the list file follows the following format:
```
<image path> <100 categorities labels>
```
