# Mpox Skin Lesion Detection Web App


The global outbreak of the virus previously called 'Monkeypox', now referred to as mpox, has caused widespread concern over the past year and continued to be a major topic in public health news headlines. During the peak transmission period back in July 2022, the World Health Organization (WHO) declared it a Public Health Emergency of International Concern (PHEIC). To obstruct its expeditious pace, early diagnosis was a must at that time. In that scenario, computer-aided monkeypox identification from skin lesion images could be a beneficial measure.


Graphical representation of our intended working pipeline:<br />

![Working pipeline](https://github.com/Suraj9968/MonnkeyPox-Detector/blob/master/assets/GA_aug.jpeg)

* * *

# Dataset

The dataset itself is available for download at the [Kaggle](https://www.kaggle.com/datasets/joydippaul/mpox-skin-lesion-dataset-version-20-msld-v20) or the [Google Drive](https://drive.google.com/drive/folders/1_bGmbDQNgJViQenjZ4QUhhzpdiubga48?usp=sharing).<br />


Some sample images from the dataset:<br />


![Sample Images](https://github.com/Suraj9968/MonnkeyPox-Detector/blob/master/assets/samples.jpg)


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
 

# Web-Application

In the development of our Monkeypox Skin Lesion Detection Web App, we leveraged the power of deep learning through the implementation of a ResNet-50 model. ResNet-50, known for its deep architecture and outstanding performance in image classification tasks, played a pivotal role in accurately identifying patterns associated with Monkeypox skin lesions. The robust capabilities of ResNet-50 enabled our model to provide precise and reliable results, contributing to the app's effectiveness in early detection. Complementing the advanced backend, we employed Streamlit for the frontend interface, ensuring a seamless and user-friendly experience. Streamlit's simplicity and versatility allowed us to create an intuitive interface that facilitates effortless image uploads and provides users with prompt and easily understandable analysis results. Together, the combination of ResNet-50 and Streamlit enhances the overall functionality of our web app, offering a powerful tool for Monkeypox detection accessible to both healthcare professionals and the broader community. In the app, [Skin Lesion Detector](https://monnkeypox-detector-howppfwjtxbnulgzecicjv.streamlit.app/), users can get, not only a suggestion but also the accuracy of the suggestion. <br />

![Sample Images](https://github.com/Suraj9968/MonnkeyPox-Detector/blob/master/assets/Screenshot%202023-12-10%20202710.png)
![Sample Images](https://github.com/Suraj9968/MonnkeyPox-Detector/blob/master/assets/Screenshot%202023-12-10%20202754.png)

* * *