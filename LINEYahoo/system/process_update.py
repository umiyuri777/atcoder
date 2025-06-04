from calculate_fee import calculate_fees
from system.storage import Storage # 型ヒント用

def process_update(target_storage: Storage, filename: str, new_filesize: int, is_paid_plan: bool, all_storages: dict[str, Storage]) -> bool:
    """UPDATEコマンドの処理を行う関数"""
    
    # 無料プランでタイプBストレージを使用しようとした場合
    if not is_paid_plan and target_storage.get_type() == "B":
        print("UPDATE: this storage location is not available on the free plan")
        return is_paid_plan
        
    # ファイルが存在しない場合
    if not target_storage.has_file(filename):
        print("UPDATE: file does not exist")
        return is_paid_plan
    
    # 操作前の状態を保存
    old_filesize = target_storage.get_file_size(filename)
    prev_current_usage = target_storage.current_usage
    prev_max_usage = target_storage.max_usage
    prev_update_amount = target_storage.update_amount
    
    # ファイルを更新
    target_storage.files[filename] = new_filesize
    target_storage.current_usage = target_storage.current_usage - old_filesize + new_filesize
    target_storage.max_usage = max(target_storage.max_usage, target_storage.current_usage)
    target_storage.update_amount += old_filesize + new_filesize
    
    # 料金計算
    storage_fee, update_fee, usage_fee = calculate_fees(all_storages)
    
    # 無料プランで、操作後の利用料金が0円を超える場合
    if not is_paid_plan and usage_fee > 0:
        # ロールバック
        target_storage.files[filename] = old_filesize
        target_storage.current_usage = prev_current_usage
        target_storage.max_usage = prev_max_usage
        target_storage.update_amount = prev_update_amount
        print("UPDATE: free plan fee limit exceeded")
    else:
        print(f"UPDATE: {storage_fee} {update_fee} {usage_fee}")
    
    return is_paid_plan