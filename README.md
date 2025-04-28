🖼️ Automated Image Captioning with CNN (InceptionV3) & Transformers
An AI-powered image captioning system that uses InceptionV3 for image feature extraction and Transformers for generating descriptive captions. Ideal for improving accessibility and enhancing image search functionalities. 🚀

📚 About the Project
Goal: Build a system that can "see" an image and "say" what's happening in natural language.

🔎 Feature Extraction: InceptionV3 extracts deep visual features.

📝 Caption Generation: Transformers understand and generate language.

🔥 Attention Mechanism: The model focuses on important parts of the image while generating each word.

🛠️ Streamlit App: A simple web interface to upload and caption your images!

🎯 Key Features
🖼️ CNN Encoder: Pre-trained InceptionV3 for high-level visual understanding.

🧠 Transformer Decoder: Custom Transformer model for sequence prediction.

📈 Training & Validation: Monitored using BLEU-1 to BLEU-4, METEOR, ROUGE scores.

🎛️ Fine-tuned Hyperparameters: Learning rate scheduling, label smoothing, etc.

📋 Tokenization & Padding: Robust preprocessing for captions.

🖥️ GPU/TPU Support: Faster training on supported hardware.

🌐 Real-Time Streamlit Interface: Upload ➡️ Caption ➡️ Enjoy!



⚙️ Tech Stack


Technology	Purpose
🧠 TensorFlow & Keras	   Deep learning models

🏗️ InceptionV3	         CNN feature extractor

📚 Transformer	         Caption generation

📸 Flickr8k Dataset  	   Training and evaluation

🧹 Matplotlib, Seaborn	 Training visualization

🌍 Streamlit	           Web app deployment





🚀 How It Works

Input Image → Preprocessed and resized.

CNN Encoder → Extracts feature vectors.

Transformer Decoder → Predicts the sequence of words (the caption).

Output → A grammatically correct, meaningful sentence describing the image!
