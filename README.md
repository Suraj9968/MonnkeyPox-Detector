# Mpox Skin Lesion Detection Web App


The global outbreak of the virus previously called 'Monkeypox', now referred to as mpox, has caused widespread concern over the past year and continued to be a major topic in public health news headlines. During the peak transmission period back in July 2022, the World Health Organization (WHO) declared it a Public Health Emergency of International Concern (PHEIC). To obstruct its expeditious pace, early diagnosis was a must at that time. In that scenario, computer-aided monkeypox identification from skin lesion images could be a beneficial measure.


Graphical representation of our intended working pipeline:<br />

![Working pipeline](https://github.com/ShamsNafisaAli/Monkeypox-Skin-Lesion-Dataset-v2/blob/main/Assets/GA_aug.JPG)

* * *

# Dataset

The dataset itself is available for download at the [Kaggle](https://www.kaggle.com/datasets/joydippaul/mpox-skin-lesion-dataset-version-20-msld-v20) or the [Google Drive](https://drive.google.com/drive/folders/1_bGmbDQNgJViQenjZ4QUhhzpdiubga48?usp=sharing).<br />


Some sample images from the dataset:<br />


![Sample Images](https://github.com/ShamsNafisaAli/Monkeypox-Skin-Lesion-Dataset-v2/blob/main/Assets/samples.jpg)


* * *

# Dataset Description
The dataset contains a total number of 755 images from 541 unique patients. The class distribution is presented as follows:

| Class label                    | No. of Original Images | No. of Unique Patients |
|-------------------------------|-----------------------|------------------------|
| Mpox                          | 284                   | 143                    |
| Chickenpox                    | 75                    | 62                     |
| Measles                       | 55                    | 46                     |
| Cowpox                        | 66                    | 41                     |
| Hand, foot and mouth disease  | 161                   | 144                    |
| Healthy                       | 114                   | 105                    |
| Total                         | 755                   | 54                     |



There are 2 folders in the dataset.<br />

1) Original Images: This folder includes a subfolder named "FOLDS" containing five folds (fold1-fold5) for 5-fold cross-validation with the original images. Each fold has separate folders for the test, train, and validation sets.<br />

2) Augmented Images: To aid the classification task, several data augmentation methods such as rotation, translation, reflection, shear, hue, saturation, contrast and brightness jitter, noise, scaling etc. have been applied using MATLAB R2020a. Although this can be readily done using ImageGenerator/other image augmentors, to ensure reproducibility of the results, the augmented images are provided in this folder. It contains a subfolder called "FOLDS_AUG" with augmented images of the train sets from each fold in the "FOLDS" subfolder of the "Original Images".***The augmentation process resulted in an approximate 14-fold increase in the number of images.***<br />
 

# Web-Application

Since we intend to build an end to end solution - starting with dataset creation and ending with a live web app, a prototype of the web-app has already been developed using the open-source python streamlit framework with a flask core and has been hosted in the streamlit provided server for better user experience. In the app, [Skin Lesion Detector](https://skinlesionclassifierbymhealthlab.streamlit.app/), users can get, not only a suggestion but also the accuracy of the suggestion. <br />

The app's dynamic and future updates will incorporate the ability to store user data and use them to train the model realtime.<br />

![Sample Images](https://github.com/ShamsNafisaAli/Monkeypox-Skin-Lesion-Dataset-v2/blob/main/Assets/app_int_dark.png)

* * *