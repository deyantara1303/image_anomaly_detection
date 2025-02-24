import os
import random
import cv2
from augly import image as iaug

class BatchAugmentor:
	def __init__(self, normal_dir, overlay_dir, augmented_dir, num_images=200):
		self.normal_dir = normal_dir
		self.overlay_dir =overlay_dir
		self.output_dir = augmented_dir
		self.num_images = num_images

	def rotate_overlay(self, overlay, angle):
		# grab the dimensions of the image and calculate the center of the image
		(h, w) = overlay.shape[:2]
		center = (w//2, h//2)
		# rotate image by 'angle' degrees around the center of the image
		M = cv2.getRotationMatrix2D(center, angle, 1.0)
		rotated = cv2.warpAffine(overlay, M, (w, h))
		return rotated

	def augment(self):
		# List all the images in normal and overlay directories
		normal_images = [os.path.join(self.normal_dir, f) for f in os.listdir(self.normal_dir)
						 if f.lower().endswith(('.jpg', '.png'))]
		overlay_images = [os.path.join(self.overlay_dir, f) for f in os.listdir(self.overlay_dir)
						if f.lower().endswith(('.png'))]

		for i in range(self.num_images):
			# Randomly select one normal image and one overlay image
			normal_path = random.choice(normal_images)
			overlay_path = random.choice(overlay_images)
			normal_img = cv2.imread(normal_path, cv2.IMREAD_COLOR)
			overlay_img = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)
			if overlay_img is None or overlay_img.shape[-1] != 4:
				print(f"Skipping {overlay_img}: Invalid overlay image")
				continue

			# Rotate overlay image randomly within 360 degrees and save temporarily
			angle = random.uniform(0, 360)
			overlay_img = self.rotate_overlay(overlay_img, angle)
			temp_path = os.path.join(self.output_dir, f"overlay{i}.png")
			cv2.imwrite(temp_path, overlay_img)

			# Select random positions for overlay placement and augment over original image
			x_pos = random.uniform(0.0, 0.4)
			y_pos = random.uniform(0.0, 0.2)
			out_path = os.path.join(self.output_dir, f"image_aug_{i:05d}.jpg")
			iaug.overlay_image(normal_path, temp_path, out_path, x_pos=x_pos, y_pos=y_pos)
			print(f"Saved augmented image: {out_path}")

			# Remove temporary path
			os.remove(temp_path)

if __name__=="__main__":
	# Define directories for normal, overlays and results
	normal_image_dir = "../images/normal/"
	overlay_image_dir= "../overlays/"
	augmented_image_dir = "../results"
	os.makedirs(augmented_image_dir, exist_ok=True)

	# Augment images with ROI
	batch_augmentor = BatchAugmentor(normal_image_dir, overlay_image_dir, augmented_image_dir, num_images=200)
	batch_augmentor.augment()