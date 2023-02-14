from core.generate_color_img import GenerateColorImg

if __name__ == "__main__":
    # 初始建立db
    # sqlite_op = SQLiteOperator()
    # sqlite_op.init_db()

    # 生成圖片資料至data中並更新DB資料
    GenerateColorImg().generate_post_img(add_text=True, save_img=True)
