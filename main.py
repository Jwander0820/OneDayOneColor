from core.generate_color_img import GenerateColorImg


def main():
    color_img, rgb_color = GenerateColorImg().generate_img(add_text=True, save_img=False)
    color_img.show()
    GenerateColorImg().get_post_text(rgb_color)


if __name__ == "__main__":
    main()
