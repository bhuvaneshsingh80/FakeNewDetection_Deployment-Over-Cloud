# SEIS736-Big Data Engineering-Fake News Detection Project
Fake news detection project is taken to complete a part of course - Big Data Engineering

The project provides step by step documentation and code to train and deploy the machine learning model over AWS Cloud environment.
The code is in python. Model training through AWS Sagemaker Notebook. Visualization through Tableau. 
Web application for user interface is deployed over Flask.  Datapipeline for collecting Twitter tweets is done through NiFi and Kafka

All the required code files are provided. 

Datasets for initial training: <br>
•	Fake images dataset – CASIA 2.0           https://www.kaggle.com/datasets/divg07/casia-20-image-tampering-detection-dataset <br>
•	Fake news/images dataset – MediaEval 2016 http://www.multimediaeval.org/datasets/  <br>
•	Sarcasm text – SARC                       https://metatext.io/datasets/self-annotated-reddit-corpus-(sarc)  <br>

### STEPS:
1. Create an EC2 instance on AWS - Provide proper Inbound rules for SSH, http and https ports <br>
2. Create an S3 bucket by the name : seis736-bucket <br>
3. Upload all data files (tweets files, image files ) on this S3 bucket <br>
4. Open AWS Sagemaker and create a Notebook Instance (set properties : connect to any  S3 bucket) <br>
5. click  'Open Jupyter' <br>
6. Copy paste and execute commands as in file:  SEIS-736_BDE_Project_SemanticAnalysis.ipynb   <br>
    [This will generate the semantic analysis file data_statistics.csv - This file is used for further visualization] <br>
     **You might need to !pip3 install <library-name> wherever the error for <library-name> module not found <br>
    
7. In new notebook Copy paste and execute commands as in file:  SEIS-736_BDE_Project_TextClassification.ipynb    <br>
    [ This is for text classification model. It will generate the model file: rnn_model_fake_real_text_classification.hdf5] <br>
    
8. In new notebook Copy paste and execute commands as in file:  SEIS-736_BDE_Project_ImageClassification.ipynb <br>
    [ This is for image classification model. It will generate the model file: vgg16_model_fake_real_image.hdf5]<br>

9. For flask server installtion and web interface follow the steps in flask_server folder
    
10. For NiFi and Kafka pipeline refer - Nifi and Kafka steps file
    
