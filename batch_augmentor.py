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
		(h, w) = overlay.shape[:2]
		center = (w//2, h//2)
		M = cv2.getRotationMatrix2D(center, angle, 1.0)
		rotated = cv2.warpAffine(overlay, M, (w, h),
								 borderMode=cv2.BORDER_CONSTANT,
								 borderValue=(0, 0, 0, 0))
		return rotated

	def augment(self):
		normal_images = [os.path.join(self.normal_dir, f) for f in os.listdir(self.normal_dir)
						 if f.lower().endswith(('.jpg', '.png'))]
		overlay_images = [os.path.join(self.overlay_dir, f) for f in os.listdir(self.overlay_dir)
						if f.lower().endswith(('.png'))]

		for i in range(self.num_images):
			normal_path = random.choice(normal_images)
			overlay_path = random.choice(overlay_images)

			normal_img = cv2.imread(normal_path, cv2.IMREAD_COLOR)
			overlay_img = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)

			if overlay_img is None or overlay_img.shape[-1] != 4:
				print(f"Skipping {overlay_img}: Invalid overlay image")
				continue

			scale = random.uniform(0.1, 0.3)
			new_w = int(normal_img.shape[1] * scale)
			new_h = int(overlay_img.shape[0] * (new_w / overlay_img.shape[1]))
			overlay_img = cv2.resize(overlay_img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

			angle = random.uniform(0, 360)
			overlay_img = self.rotate_overlay(overlay_img, angle)

			x_pos = random.uniform(0.0, 0.4)
			y_pos = random.uniform(0.0, 0.3)

			temp_path = os.path.join(self.output_dir, f"overlay{i}.png")
			cv2.imwrite(temp_path, overlay_img)

			out_path = os.path.join(self.output_dir, f"image_aug_{158:05d}.jpg")
			iaug.overlay_image(normal_path, temp_path, out_path, x_pos=x_pos, y_pos=y_pos)
			print(f"Saved augmented image: {out_path}")

			os.remove(temp_path)

if __name__=="__main__":
	# Define directories
	normal_image_dir = "../images/normal/"
	overlay_image_dir= "../overlays/"
	augmented_image_dir = "../results"
	os.makedirs(augmented_image_dir, exist_ok=True)

	# Augment images with ROI
	batch_augmentor = BatchAugmentor(normal_image_dir, overlay_image_dir, augmented_image_dir, num_images=200)
	batch_augmentor.augment()