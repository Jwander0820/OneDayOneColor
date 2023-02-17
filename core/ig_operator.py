class IGOperator:
    def post_text(self, color_data):
        text = f"Today's color is...\n" \
               f"RGB: {color_data['RGB']}\n" \
               f"CMYK: {color_data['CMYK']}\n" \
               f"HSV: {color_data['HSV']}\n" \
               f"HSL: {color_data['HSL']}\n" \
               f"HEX: {color_data['HEX']}\n" \
               f"Have a nice color!\n" \
               f"#onedayonecolor #color {(color_data['HEX']).lower()}"
        return text
