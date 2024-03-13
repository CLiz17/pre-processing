## Pre-processing Custom Dataset for Deepfake Detection

### Pre-processing a raw video dataset involves several steps,

- Frame extraction : Extract frames at 30 fps, capturing every 4th frame.
- Face Detection : Locate faces within video frames using MTCNN in OpenCV
- Face Alignment : Normalize orientation and size of detected faces
- Face Extraction : Extract detected faces from video frames
- Labeling : Annotate resized face images with appropriate labels (0 for real, 1 for fake)
