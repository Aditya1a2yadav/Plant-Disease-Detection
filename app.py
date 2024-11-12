from flask import Flask,render_template,request,flash,redirect
import pickle
import os
import numpy as np
import pandas as pd
import tensorflow
from tensorflow import keras
from tensorflow.keras.preprocessing import image


app=Flask(__name__)

app.config["SECRET_KEY"]="secret"
app.config["UPLOAD_FOLDER"]="upload"

with open("model.pkl","rb") as mw:
    model=pickle.load(mw)

labels={0: 'Apple___Apple-scab',
        1: 'Apple___Black-rot',
        2: 'Apple___Cedar-apple-rust',
        3: 'Apple___healthy',
        4: 'Blueberry___healthy',
        5: 'Cherry___Powdery-mildew',
        6: 'Cherry___healthy',
        7: 'Corn___Cercospora-leaf-spot-Gray-leaf-spot',
        8: 'Corn___Common-rust',
        9: 'Corn___Northern-Leaf-Blight',
        10: 'Corn___healthy',
        11: 'Grape___Black-rot',
        12: 'Grape___Esca(Black-Measles)',
        13: 'Grape___Leaf-blight(Isariopsis-Leaf-Spot)',
        14: 'Grape___healthy',
        15: 'Orange___Haunglongbing(Citrus-greening)',
        16: 'Peach___Bacterial-spot',
        17: 'Peach___healthy',
        18: 'Pepperbell___Bacterial-spot',
        19: 'Pepperbell___healthy',
        20: 'Potato___Early-blight',
        21: 'Potato___Late-blight',
        22: 'Potato___healthy',
        23: 'Raspberry___healthy',
        24: 'Soybean___healthy',
        25: 'Squash___Powdery-mildew',
        26: 'Strawberry___Leaf-scorch',
        27: 'Strawberry___healthy',
        28: 'Tomato___Bacterial-spot',
        29: 'Tomato___Early-blight',
        30: 'Tomato___Late-blight',
        31: 'Tomato___Leaf-Mold',
        32: 'Tomato___Septoria-leaf-spot',
        33: 'Tomato___Spider-mites Two-spotted-spider-mite',
        34: 'Tomato___Target-Spot',
        35: 'Tomato___Tomato-Yellow-Leaf-Curl-Virus',
        36: 'Tomato___Tomato-mosaic-virus',
        37: 'Tomato___healthy'}

@app.route("/",methods=["GET","POST"])  
@app.route("/prediction",methods=["GET","POST"])  
def predict ():


    message=""
    if request.method=="POST":
        if "my_image" not in request.files:
            flash("No file Uploaded")
            return redirect(request.url)
        
        img=request.files["my_image"]
        if img.filename=="":
            flash("No file Uploaded")
            return redirect(request.url)
        if img:
            img_path=os.path.join(app.config["UPLOAD_FOLDER"],img.filename)
            img.save(img_path)
            img=image.load_img(img_path,target_size=(224,224,3))
            img_arr=image.img_to_array(img)
            img_arr=img_arr/255.0
            img_arr=np.expand_dims(img_arr, axis=0)
            predictions = model.predict(img_arr)
            predicted_class = np.argmax(predictions, axis=-1)
            label = labels[predicted_class[0]]
            plant_name=label.split("___")[0]
            disease=label.split("___")[1]
            message=[plant_name,disease]


    return render_template("prediction.html",title="predicion",output=message)


if __name__=="__main__":
   app.run(debug=True)