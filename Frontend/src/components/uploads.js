'use client';

import { useState } from 'react';
import axios from 'axios';
import './uploads.css'; // Import the CSS file

const UploadForm = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleDragOver = (event) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'copy';
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    setSelectedFile(file);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!selectedFile) {
      alert('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    setLoading(true);

    try {
      const response = await axios.post('http://localhost:5000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setTimeout(() => {
        setResult(response.data);
        setLoading(false);
      }, 2000); // Simulate 2 seconds loading
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('An error occurred while uploading the file.');
      setLoading(false);
    }
  };

  const handleReturn = () => {
    setSelectedFile(null);
    setResult(null);
    setLoading(false);
  };

  return (
    <div className={`upload-container ${result ? 'result-background' : 'upload-background'}`}>
      <video autoPlay muted loop className="background-video">
        <source src="/videos/1.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <div className="content-container">
        <h2 className="model-heading">Alzheimer's Disease Prediction Model</h2>
        {loading ? (
          <div className="loading-container">
            <div className="loading-spinner"></div>
          </div>
        ) : !result ? (
          <div className="upload-card">
            <form onSubmit={handleSubmit} onDragOver={handleDragOver} onDrop={handleDrop}>
              {!selectedFile ? (
                <div className="drop-area">
                  <p className="instruction-text">Drag & Drop an MRI image here</p>
                  <p className="or-text">or</p>
                  <label htmlFor="file-input" className="file-label">
                    <input type="file" id="file-input" onChange={handleFileChange} className="file-input" />
                    Choose a file
                  </label>
                </div>
              ) : (
                <div className="file-info">
                  <img src={URL.createObjectURL(selectedFile)} alt="Selected File" className="preview-image" />
                  <p className="file-name">{selectedFile.name}</p>
                </div>
              )}
              <button type="submit" className="upload-button">
                <i className="fas fa-upload"></i> Predict
              </button>
            </form>
          </div>
        ) : (
          <div className="result-container">
            <div className="result-card">
              <h3 className="result-title">Result</h3>
              <p className="result-text">Prediction: <span className="result-value">{result.prediction}</span></p>
              <p className="result-text">Probability: <span className="result-value">{result.probability}%</span></p>
            </div>
            <button className="return-button" onClick={handleReturn}>
              <i className="fas fa-arrow-left"></i> Return
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default UploadForm;
