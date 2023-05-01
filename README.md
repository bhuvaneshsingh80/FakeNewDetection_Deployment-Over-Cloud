# Fake News Detection model deployment over AWS Cloud
Fake news detection project is taken to complete a part of course - Data Lake Engineering

The project provides step by step documentation and code to train and deploy the machine learning model over AWS Cloud environment.
The code is in python. Model training through AWS Sagemaker Notebook. Visualization through Tableau. 
Web application for user interface is deployed over Flask.  

All the required code files are provided. 

Datasets for initial training: <br>
•	Fake images dataset – CASIA 2.0           https://www.kaggle.com/datasets/divg07/casia-20-image-tampering-detection-dataset <br>
•	Fake news/images dataset – MediaEval 2016 http://www.multimediaeval.org/datasets/  <br>
•	Sarcasm text – SARC                       https://metatext.io/datasets/self-annotated-reddit-corpus-(sarc)  <br>

### STEPS:
1. Create an EC2 instance on AWS - Provide proper Inbound rules for SSH, http and https ports <br>
2. Create an S3 bucket  <br>
3. Upload all data files (tweets files, image files ) on this S3 bucket <br>
4. Open AWS Sagemaker and create a Notebook Instance (set properties : connect to any  S3 bucket) <br>
5. click  'Open Jupyter' <br>
6. Copy paste and execute commands as in file:  SEIS-745_DLE_Project_SemanticAnalysis.ipynb   <br>
    [This will generate the semantic analysis file analysis_sheet.csv - This file is used for further visualization] <br>
     *You might need to !pip3 install library-name for errors  "library-name module not found" <br>
    
7. In new notebook Copy paste and execute commands as in file:  SEIS-745_DLE_Project_TextClassification.ipynb    <br>
    [ This is for text classification model. It will generate the model file: rnn_model_fake_real_text_classification.hdf5] <br>
    
8. In new notebook Copy paste and execute commands as in file:  SEIS-745_DLE_Project_ImageClassification.ipynb <br>
    [ This is for image classification model. It will generate the model file: vgg16_model_fake_real_image.hdf5]<br>

9. For flask server installation and web interface follow the steps in flask_server folder
    
10. For NiFi and Kafka pipeline refer - Nifi_Kafka folder
    
**Note: AS the hdf5 file of image model (vgg16_model_fake_real_image.hdf5) is >25MB, so issue over GitHub, thus sharing the file over google drive : https://drive.google.com/drive/folders/19cwJBIqxtdfzeiBqV80flSlSKyu6BJ91?usp=sharing 
