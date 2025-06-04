from calculate_fee import calculate_fees
from system.storage import Storage # 型ヒント用

def process_upload(target_storage: Storage, filename: str, filesize: int, is_paid_plan: bool, all_storages: dict[str, Storage]) -> bool:
    """ファイルのアップロードを行う関数"""
    
    # 無料プランでタイプBストレージを使用しようとした場合
    if not is_paid_plan and target_storage.get_type() == "B":
        print("UPLOAD: this storage location is not available on the free plan")
        return is_paid_plan
        
    # 同名のファイルが既に存在する場合
    if target_storage.has_file(filename):
        print("UPLOAD: file already exists")
        return is_paid_plan
    
    # 操作前の状態を保存
    prev_current_usage = target_storage.current_usage
    prev_max_usage = target_storage.max_usage
    prev_update_amount = target_storage.update_amount
    
    # ファイルをアップロード
    target_storage.files[filename] = filesize
    target_storage.current_usage += filesize
    target_storage.max_usage = max(target_storage.max_usage, target_storage.current_usage)
    target_storage.update_amount += filesize
    
    # 料金計算
    storage_fee, update_fee, usage_fee = calculate_fees(all_storages)
    
    # 無料プランで、操作後の利用料金が0円を超える場合
    if not is_paid_plan and usage_fee > 0:
        # ロールバック
        del target_storage.files[filename]
        target_storage.current_usage = prev_current_usage
        target_storage.max_usage = prev_max_usage
        target_storage.update_amount = prev_update_amount
        print("UPLOAD: free plan fee limit exceeded")
    else:
        print(f"UPLOAD: {storage_fee} {update_fee} {usage_fee}")
    
    return is_paid_plan