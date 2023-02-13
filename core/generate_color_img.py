import random

from PIL import Image

from utils.color_converter import ColorConverter


class GenerateColorImg:
    def __init__(self):
        self.color_img = None
        self.width = 1200
        self.height = 1200

    def get_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    def get_color_convert_result(self, r, g, b):
        cmyk_color = ColorConverter.rgb_to_cmyk(r, g, b)
        hsv_color = ColorConverter.rgb_to_hsv(r, g, b)
        hsl_color = ColorConverter.rgb_to_hsl(r, g, b)
        hex_color = ColorConverter.rgb_to_hex(r, g, b)
        return cmyk_color, hsv_color, hsl_color, hex_color

    def generate_img(self):
        r, g, b = self.get_random_color()
        self.color_img = Image.new("RGB", (self.width, self.height), (r, g, b))
        cmyk_color, hsv_color, hsl_color, hex_color = self.get_color_convert_result(r, g, b)

        print(f"RGB: {(r, g, b)}")
        print(f"CMYK: {cmyk_color}")
        print(f"HSV: {hsv_color}")
        print(f"HSL: {hsl_color}")
        print(f"Hex: {hex_color}")

    def save_color_img(self):
        self.color_img.save("random_image.png")


if __name__ == "__main__":
    GenerateColorImg().generate_img()
