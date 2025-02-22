import cv2
import numpy as np

class ForegroundExtractor:
	def __init__(self, image_path, result_path):
		self.points = []
		self.image_path = image_path
		self.result_path = result_path
		self.img = cv2.imread(self.image_path, 1)
		self.img= cv2.resize(self.img, (900, 900), interpolation=cv2.INTER_LINEAR)

	def display_image(self):
		cv2.imshow('image', self.img)

	def extract_roi_on_mouse_click(self):
		print("Click sequentially on the ROI to capture the borders")
		cv2.setMouseCallback('image', self.on_mouse_click)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def on_mouse_click(self, event, x, y, flags, param):
		# Click on left mouse button to select polygon points, exit on right mouse button
		if event == cv2.EVENT_LBUTTONDOWN:
			print(f"clicked coordinate: {x}, {y}")
			self.points.append((x, y))
			cv2.imshow('image', self.img)
		elif event == cv2.EVENT_RBUTTONDOWN:
			if len(self.points) > 2:
				self.extract_object()
			else:
				print("Select at least 3 points to define the shape")


	def extract_object(self):
		# Create all-zeros (black) mask of the image size
		mask = np.zeros(self.img.shape[:2], dtype=np.uint8)

		# Convert selected self.points into numpy array
		pts = np.array(self.points, np.int32)

		# Fill the ROI from mouse click with white on the mask
		cv2.fillPoly(mask, [pts], 255)

		# Keep only the ROI pixels in foreground and black background
		extracted = cv2.bitwise_and(self.img, self.img, mask=mask)

		# Decompose extracted image into RGB channels and merge with mask ROI
		r, g, b = cv2.split(extracted)
		result = cv2.merge([r, g, b, mask])

		cv2.imwrite(self.result_path, result)
		cv2.imshow("Cropped contour", extracted)
		print("Contour extracted. Press any key to save and exit")

		cv2.waitKey(0)

if __name__=="__main__":
	""" Set ROI image in roi_image_path.
	Set overlay_image_path.
	Store extracted overlay ROI in overlay_image_path."""

	roi_image_path = '../images/anomalies/string.jpeg'
	overlay_image_path = "../overlays/mask_string.png"

	# Extract ROI
	foreground_extractor = ForegroundExtractor(roi_image_path, overlay_image_path)
	foreground_extractor.display_image()
	foreground_extractor.extract_roi_on_mouse_click()