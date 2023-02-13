import colorsys


class ColorConverter:
    @staticmethod
    def rgb_to_hsv_by_colorsys(rgb_color):
        r, g, b = rgb_color
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        h = round(h * 360)
        s = round(s * 100)
        v = round(v * 100)
        return h, s, v

    @staticmethod
    def rgb_to_hsl_by_colorsys(rgb_color):
        r, g, b = rgb_color
        h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
        h = round(h * 360)
        l = round(l * 100)
        s = round(s * 100)
        return h, s, l

    @staticmethod
    def rgb_to_hex(rgb_color):
        r, g, b = rgb_color
        hex_color = f"#{r:02X}{g:02X}{b:02X}"  # 轉換成十六進制
        return hex_color

    @staticmethod
    def rgb_to_cmyk(rgb_color, round_setting=2, common_patterns=True):
        r, g, b = rgb_color
        if r == 0 and g == 0 and b == 0:
            if common_patterns:
                return 0, 0, 0, 100
            return 0, 0, 0, 1

        r, g, b = r / 255.0, g / 255.0, b / 255.0
        k = 1 - max(r, g, b)
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)

        c = round(c, round_setting)
        m = round(m, round_setting)
        y = round(y, round_setting)
        k = round(k, round_setting)
        if common_patterns:
            c = round(c * 100)
            m = round(m * 100)
            y = round(y * 100)
            k = round(k * 100)
            return c, m, y, k
        return c, m, y, k

    @staticmethod
    def rgb_to_hsv(rgb_color, round_setting=2, common_patterns=True):
        r, g, b = rgb_color
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        max_value = max(r, g, b)
        min_value = min(r, g, b)
        diff = max_value - min_value

        if max_value == min_value:
            h = 0
        elif max_value == r:
            h = (60 * ((g - b) / diff) + 360) % 360
        elif max_value == g:
            h = (60 * ((b - r) / diff) + 120) % 360
        else:
            h = (60 * ((r - g) / diff) + 240) % 360

        if max_value == 0:
            s = 0
        else:
            s = (diff / max_value) * 100

        v = max_value * 100

        h = round(h, round_setting)
        s = round(s, round_setting)
        v = round(v, round_setting)

        if common_patterns:
            h = round(h)
            s = round(s, 1)
            v = round(v, 1)
            return h, s, v
        return h, s, v

    @staticmethod
    def rgb_to_hsl(rgb_color, round_setting=2, common_patterns=True):
        r, g, b = rgb_color
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        max_value = max(r, g, b)
        min_value = min(r, g, b)
        diff = max_value - min_value

        if max_value == min_value:
            h = 0
        elif max_value == r:
            h = (60 * ((g - b) / diff) + 360) % 360
        elif max_value == g:
            h = (60 * ((b - r) / diff) + 120) % 360
        else:
            h = (60 * ((r - g) / diff) + 240) % 360

        l = (max_value + min_value) / 2

        if max_value == min_value:
            s = 0
        elif l <= 0.5:
            s = diff / (max_value + min_value)
        else:
            s = diff / (2 - max_value - min_value)

        s *= 100
        l *= 100

        h = round(h, round_setting)
        s = round(s, round_setting)
        l = round(l, round_setting)

        if common_patterns:
            h = round(h)
            s = round(s, 1)
            l = round(l, 1)
            return h, s, l
        return h, s, l


if __name__ == "__main__":
    # test color
    _rgb_color = (71, 21, 150)  # r, g, b

    # convert
    c, m, y, k = ColorConverter.rgb_to_cmyk(_rgb_color)
    hsv_h, hsv_s, hsv_v = ColorConverter.rgb_to_hsv(_rgb_color)
    hsl_h, hsl_s, hsl_l = ColorConverter.rgb_to_hsl(_rgb_color)
    hex_color = ColorConverter.rgb_to_hex(_rgb_color)

    # result
    print("RGB:", _rgb_color)
    print(f"CMYK: {c}%, {m}%, {y}%, {k}%")
    print(f"HSV: {hsv_h}°, {hsv_s}%, {hsv_v}%")
    print(f"HSL: {hsl_h}°, {hsl_s}%, {hsl_l}%")
    print(f"HEX: {hex_color}")
