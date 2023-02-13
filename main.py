from core.generate_color_img import GenerateColorImg


def main():
    color_img = GenerateColorImg().generate_img(add_text=True, save_img=False)
    color_img.show()


if __name__ == "__main__":
    main()
