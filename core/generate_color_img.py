import random

from PIL import Image, ImageDraw, ImageFont

from utils.color_converter import ColorConverter


class GenerateColorImg:
    def __init__(self):
        self.color_img = None
        self.width = 1200
        self.height = 1200

    def generate_img(self, color=None, add_text=True, save_img=False):
        """
        生成純色圖片
        :param color: 指定顏色，需為元組形式，預設為None，生成隨機顏色
        :param add_text: 是否在底部添加說明文字，預設為True
        :param save_img: 是否儲存圖片，預設為False
        :return:
        """
        if not color:
            self.rgb_color = self.get_random_color()  # (r, g, b) 隨機顏色
        else:
            self.rgb_color = color  # 指定顏色
        self.color_img = Image.new("RGB", (self.width, self.height), self.rgb_color)  # 建立純色圖片
        self.cmyk_color, self.hsv_color, self.hsl_color, self.hex_color = self.get_color_convert_result(self.rgb_color)
        print(f"RGB: {self.rgb_color}")
        print(f"CMYK: {self.cmyk_color}")
        print(f"HSV: {self.hsv_color}")
        print(f"HSL: {self.hsl_color}")
        print(f"HEX: {self.hex_color}")
        if add_text:
            self.add_text()
        if save_img:
            self.save_color_img()
        return self.color_img

    def get_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    def get_color_convert_result(self, rgb_color):
        cmyk_color = ColorConverter.rgb_to_cmyk(rgb_color)
        hsv_color = ColorConverter.rgb_to_hsv(rgb_color)
        hsl_color = ColorConverter.rgb_to_hsl(rgb_color)
        hex_color = ColorConverter.rgb_to_hex(rgb_color)
        return cmyk_color, hsv_color, hsl_color, hex_color

    def add_text(self):
        # 基本設定
        draw = ImageDraw.Draw(self.color_img)
        font = ImageFont.truetype("arialbd.ttf", 40, encoding='utf-8')  # 設定字型
        font_color = (0, 0, 0)  # 黑色
        # 添加底部空白說明欄
        left_top = (0, 1000)
        right_bottom = (1200, 1200)
        fill_color = (255, 255, 255)  # 白色
        draw.rectangle((left_top, right_bottom), fill=fill_color)
        # 添加文字
        r, g, b = self.rgb_color
        text = f"RGB: ({r}, {g}, {b})"
        position = (20, 1020)
        draw.text(position, text, fill=font_color, font=font)

        c, m, y, k = self.cmyk_color
        text = f"CMYK: ({c}%, {m}%, {y}%, {k}%)"
        position = (600, 1020)
        draw.text(position, text, fill=font_color, font=font)

        h, s, v = self.hsv_color
        text = f"HSV: ({h}°, {s}%, {v}%)"
        position = (20, 1080)
        draw.text(position, text, fill=font_color, font=font)

        h, s, l = self.hsl_color
        text = f"HSL: ({h}°, {s}%, {l}%)"
        position = (600, 1080)
        draw.text(position, text, fill=font_color, font=font)

        text = f"HEX: {self.hex_color}"
        position = (20, 1140)
        draw.text(position, text, fill=font_color, font=font)

    def save_color_img(self):
        self.color_img.save("random_image.png")


if __name__ == "__main__":
    color_img = GenerateColorImg().generate_img(save_img=False)
    color_img.show()
