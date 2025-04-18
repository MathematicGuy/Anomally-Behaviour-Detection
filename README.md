mediapipe: For extracting pose and hand landmarks.

pandas: For data manipulation and analysis.

opencv-python-headless: For image and video processing without GUI support.

tensorflow: For building and training neural networks, including LSTMs.

scikit-learn: For additional machine learning utilities.

numpy: For numerical computations.

matplotlib: For data visualization.

```txt
Each frame has 33 landmarks (MediaPipe Pose detects 33 distinct body keypoints). For each landmark, you get 4 values:

    x (normalized horizontal coordinate)

    y (normalized vertical coordinate)

    z (relative depth)

    visibility (confidence of that landmark being visible)

So for each frame:

    33 landmarks × 4 values each = 132 features total.
```

### Main Dataset
[Single_person_violent](https://www.kaggle.com/datasets/anuja2188/single-person-violent-activity)

[A-Dataset-for-Automatic-Violence-Detection-in-Videos](https://github.com/airtlab/A-Dataset-for-Automatic-Violence-Detection-in-Videos/tree/master?tab=readme-ov-file#a-dataset-for-automatic-violence-detection-in-videos)


### Training Data Directory Structure
**Original Data**
```txt
Single_person_violent/
├── Kick
│   ├── kicking1.mp4
│   ├── kicking2.mp4
│   └── ...
├── Punching
│   ├── punching1.mp4
│   ├── punching2.mp4
│   └── ...
└── Standing
    ├── standing1.mp4
    ├── standing2.mp4
    └── ...
```

**Extracted Frames for Pose Estimation and Trainning**
```txt
frames/
├── Kick
│   └── kicking1
│       ├── frame_0.jpg
│       ├── frame_5.jpg
│       ...
├── Punching
│   └── punching1
│       ├── frame_0.jpg
│       ├── frame_5.jpg
│       ...
└── Non-violent
    └── non1
        ├── frame_0.jpg
        ├── frame_5.jpg
        ...
```

```mermaid
%% Training Pipeline
flowchart TD
    subgraph Preprocessing
        A[Raw Video Files] --> B[Ensure Vertical Orientation]
        B --> C[Resize Frames to 720×1280]
        C --> D[Extract Pose Keypoints]
    end

    subgraph Segmentation & Padding
        D --> E[Segment Sequence with Tail]
        E --> F[Segments of shape max_seq_len, n_features]
    end

    subgraph Dataset Assembly
        F --> G[Collect X_seq_padded & y_seq_labels]
        G --> H[Convert to NumPy arrays]
    end

    subgraph Model Training & Tuning
        H --> I[Define build_lstm_model / build_gru_model / build_dnn_model]
        I --> J[Grid Search over dropout_rate]
        J --> K[Fit each model with validation_data]
        K --> L[Record train_acc & val_acc]
        K --> M[Save each model to .keras/.h5]
    end

    subgraph Visualization
        L --> N[Create DataFrame of results]
        N --> O[Plot Test Accuracy vs Dropout]
    end
```

```mermaid
%% Live Inference Pipeline
flowchart TD
  subgraph Live_Inference
    P[Start Webcam / Video Input] --> Q[Ensure Vertical & Resize]
    Q --> R[Pose Estimation & Keypoint Extraction]
    R --> S[Update Rolling Buffer]
    S --> T[Visibility Check – wrists and ankles]
    T --> U[Speed Check – landmark movement]
    U --> V{Limbs detected AND speed > threshold?}
    V -- "No"  --> W[Label ‘Non‑violent’]
    V -- "Yes" --> X[Model Inference LSTM/GRU/DNN]
    X --> Y[Display Label & Draw Landmarks]
  end
```
