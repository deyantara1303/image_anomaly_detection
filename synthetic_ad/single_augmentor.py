from augly import image as i

class SingleAugmentor:
	def __init__(self, original_image, overlay_image, result_image, x_position, y_position):
		self.org= original_image
		self.overlay = overlay_image
		self.result = result_image
		self.x_pos = x_position
		self.y_pos = y_position

	def augly_augment(self):
		i.overlay_image(self.org, self.overlay, self.result, y_pos=self.y_pos, x_pos=self.x_pos)

if __name__=="__main__":
	""" Set normal image in normal_image_path.
	Set overlay_image_path.
	Set x and y position for the overlay object.
	Store final augmented image in augmented_image_path."""

	normal_image_path = "../images/normal/normal_xxx.png"
	overlay_image_path = "../overlays/mask_xxx.png"
	x_position = 0.36
	y_position = 0.0
	augmented_image_path = "../results/image_xxx.jpg"

	# Augment images with ROI
	augmentor = SingleAugmentor(normal_image_path, overlay_image_path, augmented_image_path, x_position, y_position)
	augmentor.augly_augment()