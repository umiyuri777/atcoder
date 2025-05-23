from process_calc import process_calc
from process_delete import process_delete
from process_upload import process_upload
from process_upgrade import process_upgrade
from process_update import process_update
import sys
from io import StringIO


def main(lines):
    # ストレージ情報の初期化
    storages = {
        "storage_A1": {"type": "A", "storage_fee_coef": 0.01, "update_fee_coef": 0.0005, "files": {}, "current_usage": 0, "max_usage": 0, "update_amount": 0},
        "storage_A2": {"type": "A", "storage_fee_coef": 0.001, "update_fee_coef": 0.01, "files": {}, "current_usage": 0, "max_usage": 0, "update_amount": 0},
        "storage_B1": {"type": "B", "storage_fee_coef": 0.01, "update_fee_coef": 0.001, "files": {}, "current_usage": 0, "max_usage": 0, "update_amount": 0},
        "storage_B2": {"type": "B", "storage_fee_coef": 0.0001, "update_fee_coef": 0.5, "files": {}, "current_usage": 0, "max_usage": 0, "update_amount": 0}
    }
    
    is_paid_plan = False  # 最初は無料プラン
    
    try:
        for line in lines:
            parts = line.split()
            
            timestamp = parts[0]
            command = parts[1]
            
            if command == "CALC":
                process_calc(storages)
            elif command == "UPGRADE":
                is_paid_plan = process_upgrade()
            elif command == "UPLOAD":
                storage_name = parts[2]
                filename = parts[3]
                filesize = int(parts[4])
                is_paid_plan = process_upload(storages, storage_name, filename, filesize, is_paid_plan)
            elif command == "DELETE":
                storage_name = parts[2]
                filename = parts[3]
                is_paid_plan = process_delete(storages, storage_name, filename, is_paid_plan)
            elif command == "UPDATE":
                storage_name = parts[2]
                filename = parts[3]
                filesize = int(parts[4])
                is_paid_plan = process_update(storages, storage_name, filename, filesize, is_paid_plan)
            else:
                print(f"Unknown command: {command}")

    except EOFError:
        pass

if __name__ == "__main__":
    # 標準出力をキャプチャするためのバッファ
    output_buffer = StringIO()
    original_stdout = sys.stdout
    sys.stdout = output_buffer
    
    try:
        with open('/Users/yamaguchiyusei/programming/atcoder/LINEYahoo/system/input.txt', 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        
        main(lines)
    except FileNotFoundError:
        print("temp.txtファイルが見つかりません。ファイルパスを確認してください。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    
    # 標準出力を元に戻す
    sys.stdout = original_stdout
    
    # キャプチャした出力をtemp2.txtに書き込む
    with open('/Users/yamaguchiyusei/programming/atcoder/LINEYahoo/system/output.txt', 'w') as output_file:
        output_file.write(output_buffer.getvalue())
    
    print("処理が完了しました。結果はoutput.txtに保存されました。")