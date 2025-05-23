from calculate_fee import calculate_fees

def process_update(storages, storage_name, filename, filesize, is_paid_plan):
    """UPDATEコマンドの処理を行う関数"""
    storage = storages[storage_name]
    
    # 無料プランでタイプBストレージを使用しようとした場合
    if not is_paid_plan and storage["type"] == "B":
        print("UPDATE: this storage location is not available on the free plan")
        return is_paid_plan
        
    # ファイルが存在しない場合
    if filename not in storage["files"]:
        print("UPDATE: file does not exist")
        return is_paid_plan
    
    # 操作前の状態を保存
    old_filesize = storage["files"][filename]
    prev_current_usage = storage["current_usage"]
    prev_max_usage = storage["max_usage"]
    prev_update_amount = storage["update_amount"]
    
    # ファイルを更新（一時的な処理）
    storage["files"][filename] = filesize
    storage["current_usage"] = storage["current_usage"] - old_filesize + filesize
    storage["max_usage"] = max(storage["max_usage"], storage["current_usage"])
    storage["update_amount"] += old_filesize + filesize
    
    # 料金計算
    storage_fee, update_fee, usage_fee = calculate_fees(storages)
    
    # 無料プランで、操作後の利用料金が0円を超える場合
    if not is_paid_plan and usage_fee > 0:
        # 状態を元に戻す
        storage["files"][filename] = old_filesize
        storage["current_usage"] = prev_current_usage
        storage["max_usage"] = prev_max_usage
        storage["update_amount"] = prev_update_amount
        print("UPDATE: free plan fee limit exceeded")
    else:
        print(f"UPDATE: {storage_fee} {update_fee} {usage_fee}")
    
    return is_paid_plan