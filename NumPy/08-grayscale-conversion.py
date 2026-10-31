import numpy as np
from PIL import Image
from pathlib import Path

base_path = Path(__file__).parent

image_path = base_path / "images" / "image1.jpg"
output_path = base_path / "images" / "image1-gray.jpg"

original_image = Image.open(image_path)
image_data = np.asarray(original_image)

print("Image shape:", image_data.shape)   #(1543, 2048, 3)

red_channel = image_data[:,:,0]
print("red channel:", red_channel)

#for change image to image gray ====> Y = 0.2126R + 0.7152G + 0.0722B
weights = [0.2126, 0.7152, 0.0722]
grayscale_image_data = image_data @ weights
grayscale_image_data = grayscale_image_data.astype('uint8')
grayscale_image = Image.fromarray(grayscale_image_data)
grayscale_image.save(output_path)