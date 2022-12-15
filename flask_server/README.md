# Steps for Flask Server deployment over AWS

Step 1. Create an EC2 instance and provide proper Inbound access of SSH entry from your IP <br>
Step 2. Connect to EC2 using putty <br>
Step 3. Copy files/folder - requirements.txt, main-app.py, rnn_model_fake_real_text_classification.hdf5, and templates folder to your EC2 using WinSCP(Windows)/Terminal(MacOs)  <br>
Step 4. Execute  install -r requirements.txt     on your EC2  <br>
Step 5. Execute  python3 main-app.py             on your EC2   [ The Flask server will be up on port 8080 ]  <br>

Open the web browser and type in the url as-    http://(aws-public-host-name):8080/  <br>

The webpage should be displayed  <br>
