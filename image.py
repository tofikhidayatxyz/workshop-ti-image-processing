import cv2
import numpy as np

def split_image(image, num_sections):
    height, width, _ = image.shape
    section_width = width // num_sections
    sections = [image[:, i*section_width:(i+1)*section_width, :] for i in range(num_sections)]
    return sections

def split_image(image, num_sections):
    height, width, _ = image.shape
    section_width = width // num_sections
    sections = [image[:, i*section_width:(i+1)*section_width, :] for i in range(num_sections)]
    return sections

def merge_sections(sections):
    return np.concatenate(sections, axis=1)

def overlay_color(image, color, opacity):
    overlay = image.copy()
    cv2.rectangle(overlay, (0, 0), (image.shape[1], image.shape[0]), color, -1)
    cv2.addWeighted(overlay, opacity, image, 1 - opacity, 0, image)
    return image


image_path = './sources/master.jpg'
original_image = cv2.imread(image_path)


num_sections = 5
image_sections = split_image(original_image, num_sections)


colors = [
    (128, 98, 214, 0.3),
    (255, 225, 123, 0.4), 
    (241, 26, 123, 0.6), 
    (13, 18, 130, 0.22),
    (151, 254, 237, 0.7)
]

for i in range(num_sections):
    image_sections[i] = overlay_color(image_sections[i], colors[i], opacity=colors[i][3])

modified_image = merge_sections(image_sections)
cv2.waitKey(0)

watermark_text = "TOFIK HIDAYAT"
font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 2.0
font_thickness = 4
text_color = (0, 0, 0) 
text_position = (200, 300)

watermarked_image = np.copy(modified_image)
cv2.putText(watermarked_image, watermark_text, text_position, font, font_scale, text_color, font_thickness, cv2.LINE_AA)
alpha = 0.7
watermarked_image = cv2.addWeighted(modified_image, 1 - alpha, watermarked_image, alpha, 0)


cv2.imwrite('./results/final.png',watermarked_image)