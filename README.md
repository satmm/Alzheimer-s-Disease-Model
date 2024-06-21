---
# Alzheimer's Disease Classification System

This project leverages a Convolutional Neural Network (CNN) model, Deep Learning model based on DenseNet-169 architecture, leveraging TensorFlow and Keras framework ,to classify stages of Alzheimer's disease in patients based on a dataset obtained from Kaggle.You can find the dataset here - https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images includes images categorized into four classes related to Alzheimer's disease stages. DenseNet architecture plays a pivotal role in this project by efficiently managing feature reuse through dense connections between layers. Unlike traditional architectures that rely on deep or wide networks, DenseNets enhance parameter efficiency and facilitate better information flow and gradient propagation throughout the network. This feature reuse not only simplifies training but also enhances model regularization, reducing overfitting on smaller datasets. The project integrates this robust architecture into a Flask backend for predictive model deployment and a Next.js frontend for intuitive user interaction and result visualization.








### Video Demonstration


https://github.com/satmm/Alzheimer-s-Disease-Model/assets/81502695/3fd727bf-4c9f-448b-a9f0-fee48dda0947



### File Structure

The project is organized into two main directories: `Backend` and `Frontend`, each serving a distinct purpose within the system.

```
sample
│
├── .gitattributes
│
├── Backend
│   ├── .gitignore
│   ├── alzheimers_model.keras
│   ├── app.py
│   ├── best_weights.keras
│   ├── requirements.txt
│   ├── train_model.py
│   ├──Alzheimer_s Dataset
│   └── uploads
│
├── Frontend
│   ├── .eslintrc.json
│   ├── .gitignore
│   ├── jsconfig.json
│   ├── next.config.mjs
│   ├── node_modules
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   ├── next.svg
│   │   ├── vercel.svg
│   │   └── videos
│   └── src
│       ├── app
│       └── components
│
├──.gitattributes 
└── README.md

   ```
### Backend (Flask)

The backend of this project is implemented using Flask, a lightweight and efficient web framework for Python. It serves as the interface between the Deep Learning model and the user interface, providing endpoints to receive image inputs, process them through the model, and return predictions.

#### Files and Structure

1. **train_model.py**: Python script responsible for training the Deep Learning model using DenseNet-169 architecture. It preprocesses the dataset, augments images, builds the model, trains it, and saves the trained model (`alzheimers_model.keras`).

2. **app.py**: Flask application that loads the trained model (`alzheimers_model.keras`), compiles it with an Adam optimizer, and exposes API endpoints:
   - `/`: Home route indicating the Flask backend is running.
   - `/predict`: POST route accepting image uploads, preprocessing them, predicting Alzheimer's stage using the loaded model, and returning results in JSON format.

3. **alzheimers_model.keras**: The `alzheimers_model.keras` file contains the architecture of the deep learning model used for classifying Alzheimer's disease stages. Specifically, it is based on the DenseNet-169 architecture, which is known for its efficiency in handling complex image classification tasks. This file encapsulates the structure of the neural network, including the layers, activation functions, and connections that define how the model processes input images. The model's architecture is essential for transforming the raw input data into a format that can be interpreted to predict the stage of Alzheimer's disease.

4. **best_weights.keras**: The `best_weights.keras` file holds the optimized weights that the DenseNet-169 model has learned during the training process. These weights are critical parameters that influence how the model makes predictions based on the input data. During training, the model adjusts these weights to minimize the error in its predictions, and the `best_weights.keras` file stores the set of weights that resulted in the highest accuracy. When the Flask backend application loads the model, it uses these weights to ensure that predictions are as accurate as possible, leveraging the learned knowledge from the training phase.

### Frontend (Next.js)

The frontend is developed using Next.js, a React framework that enables server-side rendering and optimized production builds. It provides a user-friendly interface for uploading images, interacting with the backend for predictions, and displaying results.

#### Files and Structure

1. **pages/index.js**: Entry point of the Next.js application where the main functionality is implemented.
   - **Upload Form**: Allows users to upload an image.
   - **Prediction Display**: Renders the predicted Alzheimer's stage and probability returned by the Flask backend after processing the uploaded image.

2. **public/**: Directory containing static assets like images and icons used in the frontend.

3. **styles/**: Directory for styling components and pages using CSS modules or other styling approaches compatible with Next.js.

### Tech Stack

- **Backend**: Flask, Python
- **Deep Learning Framework**: TensorFlow (Keras API)
- **Model Architecture**: DenseNet-169
- **Data Augmentation**: ImageDataGenerator from TensorFlow
- **Optimizer**: Adam optimizer
- **Frontend Framework**: Next.js
- **Styling**: CSS Modules
- **Deployment**: Vercel for hosting the Next.js frontend, Heroku deploying Flask backend.

### Installation and Setup

To run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/satmm/Alzheimer-s-Disease-Model.git
   cd Alzheimer-s-Disease-Model
   ```

2. **Backend Setup**:
   - Navigate to the `Backend` directory:
     ```bash
     cd Backend
     ```
   - Set up the Python environment and install dependencies:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     pip install -r requirements.txt
     ```
   - Run the Flask application:
     ```bash
     python app.py
     ```

3. **Frontend Setup**:
   - Navigate to the `Frontend` directory and install Node.js dependencies:
     ```bash
     cd ../Frontend
     npm install
     ```
   - Start the Next.js development server:
     ```bash
     npm run dev
     ```

4. **Access the Application**:
   - Open your web browser and navigate to `http://localhost:3000/` to access the Next.js frontend.
   - Upload an image to predict the Alzheimer's disease stage based on the trained model.

### Handling Large Files with Git LFS

#### Why Are `alzheimers_model.keras` and `best_weights.keras` Not Visible on GitHub?

GitHub has a file size limit of 100MB for files in repositories. The files `alzheimers_model.keras` and `best_weights.keras` exceed this limit (each being around 1.94 GB). To handle such large files, Git Large File Storage (LFS) is used. Git LFS is an extension for managing large files in Git repositories by replacing them with text pointers within Git, while storing the actual file contents on a remote server.

#### Using Git LFS

1. **Install Git LFS**:
   Ensure Git LFS is installed and initialize it:
   ```bash
   git lfs install
   ```

2. **Track the Large Files**:
   Specify which files should be managed by Git LFS by modifying the `.gitattributes` file at the root of your repository:
   ```plaintext
   *.keras filter=lfs diff=lfs merge=lfs -text
   ```

   This configuration tells Git LFS to track files with the `.keras` extension.

3. **Add and Commit the Large Files**:
   ```bash
   git add .gitattributes
   git add Backend/alzheimers_model.keras Backend/best_weights.keras
   git commit -m "Add large files and configure Git LFS tracking"
   ```

4. **Push to GitHub**:
   ```bash
   git push origin main
   ```

   When someone clones the repository, the `alzheimers_model.keras` and `best_weights.keras` files will not be directly included in the cloned repository as they are managed by Git LFS. Instead, they will get small pointer files. To fully clone the repository with the large files, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/satmm/Alzheimer-s-Disease-Model.git
   cd Alzheimer-s-Disease-Model
   ```

2. **Pull the Large Files Managed by Git LFS**:
   After cloning, run the following command to download the actual large files:
   ```bash
   git lfs pull
   ```

This will ensure that the `alzheimers_model.keras` and `best_weights.keras` files are downloaded and available in the local repository.

#### The Role of `.gitattributes`

The `.gitattributes` file is used to define attributes for pathnames. Here, it is used to configure Git LFS to track files with specific extensions. When you push changes to GitHub, Git LFS replaces the actual large files with text pointers in the repository and uploads the actual content to a remote storage.

### Summary

By using Git LFS to manage large files and configuring Vercel properly, you can deploy both the frontend and backend of your Alzheimer's Disease Classification System seamlessly. The backend serverless functions will handle the predictions, while the frontend will provide the user interface. Make sure to push your Git changes and then deploy with the Vercel CLI.

### Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Ensure to follow the coding standards and documentation guidelines provided in the repository.

### License

This project is licensed under the [MIT License](LICENSE).

---
