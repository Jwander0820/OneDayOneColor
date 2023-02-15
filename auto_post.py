from core.generate_color_img import GenerateColorImg
from utils.sqlite_operator import SQLiteOperator

if __name__ == "__main__":
    # 初始建立db，僅最開始需要使用
    # sqlite_op = SQLiteOperator()
    # sqlite_op.init_db()

    # 生成指定顏色圖片並更新DB資料
    # color = (0, 0, 0)
    # GenerateColorImg().generate_post_img(color=color, add_text=True, save_img=True)

    # 生成圖片資料至data中並更新DB資料
    GenerateColorImg().generate_post_img(add_text=True, save_img=True)
