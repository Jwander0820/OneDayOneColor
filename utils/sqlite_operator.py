import sqlite3
import time

from utils.logger import log_filter_error

DB_NAME = "odoc"
# DB_NAME = "data"  # test use db in ./utils


def get_local_time():
    """取得當前時間"""
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    return result


class SQLiteOperator:
    @log_filter_error
    def init_db(self):
        """資料庫初始建立"""
        # 建立資料庫連接，如果資料庫不存在就建立它
        conn = sqlite3.connect(f'{DB_NAME}.db')
        # 建立游標
        cursor = conn.cursor()
        # 建立資料表
        cursor.execute('''
        CREATE TABLE OneDayOneColor (
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            rgb TEXT NOT NULL,
            cmyk TEXT NOT NULL,
            hsv TEXT NOT NULL,
            hsl TEXT NOT NULL,
            hex TEXT NOT NULL
        )
        ''')
        # 提交事務並關閉資料庫連接
        conn.commit()
        conn.close()

    @log_filter_error
    def insert_data(self, color_data):
        """插入資料"""
        conn = sqlite3.connect(f'{DB_NAME}.db')
        cursor = conn.cursor()
        date = get_local_time()  # 取得當下時間
        # 操作插入資料
        rgb_color = str(color_data["RGB"])
        cmyk_color = str(color_data["CMYK"])
        hsv_color = str(color_data["HSV"])
        hsl_color = str(color_data["HSL"])
        hex_color = color_data["HEX"]
        cursor.execute("INSERT INTO OneDayOneColor (date, rgb, cmyk, hsv, hsl, hex) VALUES (?, ?, ?, ?, ?, ?)",
                       (date, rgb_color, cmyk_color, hsv_color, hsl_color, hex_color))

        conn.commit()
        conn.close()

    @log_filter_error
    def select_rgb_color(self):
        """用於確認RGB值是否重複，回傳DB現有顏色清單"""
        conn = sqlite3.connect(f'{DB_NAME}.db')
        cursor = conn.cursor()

        cursor.execute("SELECT rgb FROM OneDayOneColor")  # 選取表格中指定欄位值
        values = cursor.fetchall()  # 取值
        conn.close()
        return values


if __name__ == "__main__":
    sqlite_op = SQLiteOperator()
    # sqlite_op.init_db()  # 初始建立db
    sqlite_op.insert_data((189, 8, 32),
                          (0, 96, 83, 26),
                          (352, 95.8, 74.1),
                          (352, 91.9, 38.6),
                          "#BD0820")
