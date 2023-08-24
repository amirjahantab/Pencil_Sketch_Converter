# Pencil Sketch Converter

This code is a simple Python script that converts an image into a pencil sketch using the OpenCV library.

## Requirements

- Python 3.x
- OpenCV library

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Install the OpenCV library by running the following command:
   ```
   pip install opencv-python
   ```
3. Save the image you want to convert to a pencil sketch in the same directory as this script.
4. Update the `image_path` variable in the code with the path to your image file.
5. Run the script by executing the following command:
   ```
   python pencil_sketch_converter.py
   ```
6. The original image and the pencil sketch will be displayed in separate windows.
7. Press any key to close the windows and exit the script.

## Parameters

The `cv2.pencilSketch` function allows you to adjust the conversion settings using the following parameters:

- `sigma_s`: The spatial smoothness. Higher values result in a smoother sketch.
- `sigma_r`: The range smoothness. Higher values result in a sketch with more detail.
- `shade_factor`: The shading factor. Higher values result in a darker sketch.

Feel free to experiment with these parameters to achieve the desired sketch effect.
