from process_calc import process_calc
from process_delete import process_delete
from process_upload import process_upload
from process_upgrade import process_upgrade
from process_update import process_update
import sys
from io import StringIO
from system.storage import Storage

def main(lines):
    # ストレージ情報の初期化 (Storageクラスを使用)
    storages: dict[str, Storage] = {
        "storage_A1": Storage(name="storage_A1", storage_type="A", storage_fee_coef=0.01, update_fee_coef=0.0005),
        "storage_A2": Storage(name="storage_A2", storage_type="A", storage_fee_coef=0.001, update_fee_coef=0.01),
        "storage_B1": Storage(name="storage_B1", storage_type="B", storage_fee_coef=0.01, update_fee_coef=0.001),
        "storage_B2": Storage(name="storage_B2", storage_type="B", storage_fee_coef=0.0001, update_fee_coef=0.5)
    }
    
    is_paid_plan = False  # 最初は無料プラン
    
    try:
        for line in lines:
            parts = line.split()
            
            timestamp = parts[0]
            command = parts[1]
            
            match command:
                case "CALC":
                    process_calc(storages)
                    
                case "UPGRADE":
                    is_paid_plan = process_upgrade() 
                    
                case "UPLOAD":
                    storage_name = parts[2]
                    filename = parts[3]
                    filesize = int(parts[4])
                    if storage_name in storages:
                        target_storage = storages[storage_name]
                        is_paid_plan = process_upload(target_storage, filename, filesize, is_paid_plan, storages)
                    else:
                        print(f"UPLOAD: invalid storage name {storage_name}")
                        
                case "DELETE":
                    storage_name = parts[2]
                    filename = parts[3]
                    if storage_name in storages:
                        target_storage = storages[storage_name]
                        is_paid_plan = process_delete(target_storage, filename, is_paid_plan, storages)
                    else:
                        print(f"DELETE: invalid storage name {storage_name}")
                        
                case "UPDATE":
                    storage_name = parts[2]
                    filename = parts[3]
                    filesize = int(parts[4])
                    if storage_name in storages:
                        target_storage = storages[storage_name]
                        is_paid_plan = process_update(target_storage, filename, filesize, is_paid_plan, storages)
                    else:
                        print(f"UPDATE: invalid storage name {storage_name}")
                case _:
                    print(f"Unknown command: {command}")

    except EOFError:
        print("EOFError: End of input reached unexpectedly.")
    except ValueError as ve:
        print(f"ValueError: Invalid data format in command - {ve}")
    except IndexError:
        print(f"IndexError: Invalid command format - insufficient arguments for {command if 'command' in locals() else 'unknown command'}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        pass 

if __name__ == "__main__":
    # 標準出力をキャプチャするためのバッファ
    output_buffer = StringIO()
    original_stdout = sys.stdout
    sys.stdout = output_buffer
    
    input_file_path = '/Users/yamaguchiyusei/programming/atcoder/LINEYahoo/system/input.txt'
    output_file_path = '/Users/yamaguchiyusei/programming/atcoder/LINEYahoo/system/output.txt'

    try:
        with open(input_file_path, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()] # 空行を無視
        
        if not lines:
            # 入力ファイルが空、または空行のみの場合の処理
            # print("Input file is empty or contains only empty lines.", file=original_stdout) # デバッグ用
            pass # 何もせず終了するか、特定のメッセージを出力
        else:
            main(lines)

    except FileNotFoundError:
        print(f"{input_file_path} not found. Please check the file path.", file=original_stdout)
    except Exception as e:
        print(f"An error occurred: {e}", file=original_stdout)
    
    # 標準出力を元に戻す
    sys.stdout = original_stdout
    
    # キャプチャした出力をoutput.txtに書き込む
    try:
        with open(output_file_path, 'w') as output_file:
            output_file.write(output_buffer.getvalue())
        print(f"Processing complete. Results saved to {output_file_path}")
    except Exception as e:
        print(f"Error writing to output file {output_file_path}: {e}")
    
    output_buffer.close()