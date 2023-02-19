import os
import random

from PIL import Image, ImageDraw, ImageFont

from core.ig_operator import IGOperator
from utils.color_converter import ColorConverter
from utils.logger import create_logger, log_filter_error
from utils.sqlite_operator import SQLiteOperator


class GenerateColorImg:
    def __init__(self):
        self.rgb_color = None
        self.color_img = None
        self.color_data = None
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
        self.color_data = self.get_color_convert_result(self.rgb_color)
        self.ig_post_text = IGOperator().post_text(self.color_data)
        if add_text:
            self.add_text()
        if save_img:
            self.save_color_img()
        return self.color_img, self.rgb_color

    @log_filter_error
    def generate_post_img(self, color=None, add_text=True, save_img=False):
        """
        生成純色圖片，比對資料庫顏色，確保不會有重複顏色出現
        :param color: 指定顏色，需為元組形式，預設為None，生成隨機顏色
        :param add_text: 是否在底部添加說明文字，預設為True
        :param save_img: 是否儲存圖片，預設為False
        :return:
        """
        logger = create_logger()
        if not color:
            self.rgb_color = self.confirm_rgb_color()  # (r, g, b) 隨機顏色
        else:
            self.rgb_color = color  # 指定顏色
            rgb_list = SQLiteOperator().select_rgb_color()  # 從DB取得現有顏色清單
            if self._check_duplicate(self.rgb_color, rgb_list):  # 確認指定的顏色是否在DB中已存在
                logger.info(f"指定的顏色已存在，請重新選定顏色 RGB: {self.rgb_color}")
                return
        self.color_img = Image.new("RGB", (self.width, self.height), self.rgb_color)  # 建立純色圖片
        self.color_data = self.get_color_convert_result(self.rgb_color)  # 顏色轉換
        self.ig_post_text = IGOperator().post_text(self.color_data)  # 生成IG貼文內容
        # 更新DB資料
        SQLiteOperator().insert_data(self.color_data)
        logger.info(f"Today Color is RGB: {self.color_data['RGB']}, HEX:{self.color_data['HEX']}")
        if add_text:
            self.add_text()
        if save_img:
            self.save_color_img()
        return self.color_img, self.rgb_color

    def get_post_text(self, color=None):
        self.rgb_color = color
        self.color_data = self.get_color_convert_result(self.rgb_color)  # 顏色轉換
        self.ig_post_text = IGOperator().post_text(self.color_data)  # 生成IG貼文內容
        print(self.ig_post_text)

    def get_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    def _check_duplicate(self, rgb_color, rgb_list):
        """用於確認RGB值是否重複"""
        for db_rgb_value in rgb_list:
            if db_rgb_value[0] == str(rgb_color):
                # print("Data already exists")  # 有重複值
                return True
        return False

    def confirm_rgb_color(self):
        rgb_list = SQLiteOperator().select_rgb_color()  # 從DB取得現有顏色清單
        rgb_color = self.get_random_color()  # 取隨機顏色
        flags = True
        while flags:
            rgb_color = self.get_random_color()  # 取隨機顏色
            flags = self._check_duplicate(rgb_color, rgb_list)  # 確認顏色是否有重複
        return rgb_color

    def get_color_convert_result(self, rgb_color):
        """
        RGB顏色轉換成不同格式的色彩空間
        :param rgb_color: RGB色彩
        :return: {"RGB": rgb_color, "CMYK": cmyk_color, "HSV": hsv_color, "HSL": hsl_color, "HEX": hex_color}
        """
        cmyk_color = ColorConverter.rgb_to_cmyk(rgb_color)
        hsv_color = ColorConverter.rgb_to_hsv(rgb_color)
        hsl_color = ColorConverter.rgb_to_hsl(rgb_color)
        hex_color = ColorConverter.rgb_to_hex(rgb_color)
        # print(f"RGB: {rgb_color}")
        # print(f"CMYK: {cmyk_color}")
        # print(f"HSV: {hsv_color}")
        # print(f"HSL: {hsl_color}")
        # print(f"HEX: {hex_color}")
        color_data = {"RGB": rgb_color, "CMYK": cmyk_color, "HSV": hsv_color, "HSL": hsl_color, "HEX": hex_color}
        return color_data

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
        r, g, b = self.color_data["RGB"]
        text = f"RGB: ({r}, {g}, {b})"
        position = (20, 1020)
        draw.text(position, text, fill=font_color, font=font)

        c, m, y, k = self.color_data["CMYK"]
        text = f"CMYK: ({c}%, {m}%, {y}%, {k}%)"
        position = (600, 1020)
        draw.text(position, text, fill=font_color, font=font)

        h, s, v = self.color_data["HSV"]
        text = f"HSV: ({h}°, {s}%, {v}%)"
        position = (20, 1080)
        draw.text(position, text, fill=font_color, font=font)

        h, s, l = self.color_data["HSL"]
        text = f"HSL: ({h}°, {s}%, {l}%)"
        position = (600, 1080)
        draw.text(position, text, fill=font_color, font=font)

        text = f"HEX: {self.color_data['HEX']}"
        position = (20, 1140)
        draw.text(position, text, fill=font_color, font=font)

    def save_color_img(self, output_folder="./data"):
        if not os.path.exists(output_folder):  # 指定輸出資料夾，若資料夾不存在則建立
            os.makedirs(output_folder)

        file_name = f"RGB{self.color_data['RGB']}_" \
                    f"CMYK{self.color_data['CMYK']}_" \
                    f"HSV{self.color_data['HSV']}_" \
                    f"HSL{self.color_data['HSL']}_" \
                    f"HEX{self.color_data['HEX']}"
        self.color_img.save(f"{output_folder}/{file_name}.png")


if __name__ == "__main__":
    color_img, rgb_color = GenerateColorImg().generate_img(color=(0, 0, 0), save_img=False)
    color_img.show()
    GenerateColorImg().get_post_text(rgb_color)
