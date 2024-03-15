# Pre-processing Custom Dataset for Deepfake Detection

The pre-processing pipeline involves several steps, including frame extraction, face detection, face alignment, face extraction, and labeling.

## Dataset Pre-processing Steps:

### 1. Frame Extraction:

- Extract frames from the input video at a rate of 30 fps, capturing every 4th frame.

### 2. Face Detection:

- Utilize the MTCNN (Multi-Task Cascaded Convolutional Networks) algorithm implemented with Tensorflow to locate faces within the video frames.

### 3. Face Alignment:

- Normalize the orientation and size of detected faces to ensure consistent positioning and alignment for further processing.

### 4. Face Extraction:

- Extract the detected faces from the video frames, ensuring that the extracted faces are of uniform size and aspect ratio.

### 5. Labeling:

- Annotate the resized face images with appropriate labels indicating whether they belong to real individuals (0) or synthetic/generated faces (1).

## Result
- Input :
    - Real : 726 frames
    - 1:1200 -> 300 ; 2:1056 -> 264 ; 3:648 -> 162;
    - Fake : 292 frames
    - 1:25 ; 2:488 -> 122 ; 3:500 -> 145 ;

- Output :
    - Real : 566 images
    - 1:140 ;2:264 ;3:162 ;
    - Fake : 289 images
    - 1:22 ;2:122 ;3:145 ;
 
### MTCNN accuracy = 89.1%
