import unittest

from utils.color_converter import ColorConverter


class TestImgOperator(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestImgOperator, self).__init__(*args, **kwargs)
        # test_data_list = [(r,g,b), (c,m,y,k), (h,s,v), (h,s,l), #hex]
        self.test_data_01 = [(255, 0, 0), (0, 100, 100, 0), (0, 100, 100), (0, 100, 50), "#FF0000"]  # 紅色	Red
        self.test_data_02 = [(255, 255, 0), (0, 0, 100, 0), (60, 100, 100), (60, 100, 50), "#FFFF00"]  # 黃色	Yellow
        self.test_data_03 = [(0, 255, 0), (100, 0, 100, 0), (120, 100, 100), (120, 100, 50), "#00FF00"]  # 綠色	Green
        self.test_data_04 = [(0, 255, 255), (100, 0, 0, 0), (180, 100, 100), (180, 100, 50), "#00FFFF"]  # 青色	Aqua
        self.test_data_05 = [(0, 0, 255), (100, 100, 0, 0), (240, 100, 100), (240, 100, 50), "#0000FF"]  # 藍色	Blue
        self.test_data_06 = [(255, 0, 255), (0, 100, 0, 0), (300, 100, 100), (300, 100, 50), "#FF00FF"]  # 品紅色	Fuchsia
        self.test_data_07 = [(128, 0, 0), (0, 100, 100, 50), (0, 100, 50.2), (0, 100, 25.1), "#800000"]  # 栗色	Maroon
        self.test_data_08 = [(128, 128, 0), (0, 0, 100, 50), (60, 100, 50.2), (60, 100, 25.1), "#808000"]  # 橄欖綠	Olive
        self.test_data_09 = [(0, 128, 0), (100, 0, 100, 50), (120, 100, 50.2), (120, 100, 25.1), "#008000"]  # 綠色	Green
        self.test_data_10 = [(0, 128, 128), (100, 0, 0, 50), (180, 100, 50.2), (180, 100, 25.1), "#008080"]  # 藍綠色	Teal
        self.test_data_11 = [(0, 0, 128), (100, 100, 0, 50), (240, 100, 50.2), (240, 100, 25.1), "#000080"]  # 藏青色	Navy
        self.test_data_12 = [(128, 0, 128), (0, 100, 0, 50), (300, 100, 50.2), (300, 100, 25.1), "#800080"]  # 紫色	Purple
        self.test_data_13 = [(255, 255, 255), (0, 0, 0, 0), (0, 0, 100), (0, 0, 100), "#FFFFFF"]  # 白色	White
        self.test_data_14 = [(192, 192, 192), (0, 0, 0, 25), (0, 0, 75.3), (0, 0, 75.3), "#C0C0C0"]  # 銀色	Silver
        self.test_data_15 = [(128, 128, 128), (0, 0, 0, 50), (0, 0, 50.2), (0, 0, 50.2), "#808080"]  # 灰色	Gray
        self.test_data_16 = [(0, 0, 0), (0, 0, 0, 100), (0, 0, 0), (0, 0, 0), "#000000"]  # 黑色	Black

        self.test_data_set = []
        self.test_data_set.append(self.test_data_01)
        self.test_data_set.append(self.test_data_02)
        self.test_data_set.append(self.test_data_03)
        self.test_data_set.append(self.test_data_04)
        self.test_data_set.append(self.test_data_05)
        self.test_data_set.append(self.test_data_06)
        self.test_data_set.append(self.test_data_07)
        self.test_data_set.append(self.test_data_08)
        self.test_data_set.append(self.test_data_09)
        self.test_data_set.append(self.test_data_10)
        self.test_data_set.append(self.test_data_11)
        self.test_data_set.append(self.test_data_12)
        self.test_data_set.append(self.test_data_13)
        self.test_data_set.append(self.test_data_14)
        self.test_data_set.append(self.test_data_15)
        self.test_data_set.append(self.test_data_16)

    def test_rgb_to_cmyk(self):
        for test_data in self.test_data_set:
            cmyk_color = ColorConverter.rgb_to_cmyk(test_data[0])
            self.assertEqual(cmyk_color, test_data[1])

    def test_rgb_to_hsv(self):
        for test_data in self.test_data_set:
            hsv_color = ColorConverter.rgb_to_hsv(test_data[0])
            self.assertEqual(hsv_color, test_data[2])

    def test_rgb_to_hsl(self):
        for test_data in self.test_data_set:
            hsl_color = ColorConverter.rgb_to_hsl(test_data[0])
            self.assertEqual(hsl_color, test_data[3])

    def test_rgb_to_hex(self):
        for test_data in self.test_data_set:
            hex_color = ColorConverter.rgb_to_hex(test_data[0])
            self.assertEqual(hex_color, test_data[4])


if __name__ == '__main__':
    unittest.main()
