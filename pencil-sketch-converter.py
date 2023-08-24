import cv2

# مسیر عکس مورد نظر را وارد کنید
image_path = 'path_to_image.jpg'

# خواندن عکس
image = cv2.imread(image_path)

# تبدیل عکس به نقاشی
sketch_image, _ = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

# نمایش عکس اصلی و نقاشی‌شده
cv2.imshow("Original Image", image)
cv2.imshow("Sketch Image", sketch_image)

# منتظر کلیدی بماند تا پنجره‌ها بسته شوند
cv2.waitKey(0)

# بستن پنجره‌ها
cv2.destroyAllWindows()
