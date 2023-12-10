import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf


st.image('https://github.com/Suraj9968/MonnkeyPox-Detector/blob/master/assets/logo.png?raw=true')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                            content:'This app is in its early stage. We recommend you to seek professional advice from a dermatologist. Thank you.'; 
                            visibility: visible;
                            display: block;
                            position: relative;
                            #background-color: red;
                            padding: 5px;
                            top: 2px;
                        }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#Add CSS styling for center alignment
st.markdown(
    """
    <style>
    .center {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the pre-trained model
model = tf.keras.models.load_model('best_model (1).h5')

# Define the labels for the categories
labels = {
    0: 'Chickenpox',
    1: 'Cowpox',
    2: 'HFMD',
    3: 'Healthy',
    4: 'Measles',
    5: 'MPOX'
}

# Function to preprocess the image
def preprocess_image(image):
    # Resize the image to 224x224
    image = image.resize((224, 224))
    # Convert the image to a numpy array
    image_array = np.array(image)
    # Normalize the image array
    # image_array = image_array / 255.0
    # Add an extra dimension to match the model's input shape
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# Function to make predictions
def predict(image):
    # Preprocess the image
    processed_image = preprocess_image(image)
    # Make the prediction
    prediction = model.predict(processed_image)
    # Get the predicted label index
    label_index = np.argmax(prediction)
    # Get the predicted label
    predicted_label = labels[label_index]
    # Get the confidence level
    confidence = prediction[0][label_index] * 100
    return predicted_label, confidence

# Streamlit app
def main():
    # Center align the heading
    st.markdown("<h1 class='center'>Skin Lesion Classifier</h1>", unsafe_allow_html=True)

    # Display a file uploader widget
    number = st.radio('Pick one', ['Upload from gallery', 'Capture by camera'])
    if number == 'Capture by camera':
        uploaded_file = st.camera_input("Take a picture")
    else:
        uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg", "bmp"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Process and classify the image
        predicted_label, confidence = predict(image)

        # Display the predicted label and confidence
        st.markdown("<h3 class='center'>This might be:</h2>", unsafe_allow_html=True)
        st.markdown(f"<h1 class='center'>{predicted_label}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='center'>Confidence: {confidence:.2f}%</p>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()