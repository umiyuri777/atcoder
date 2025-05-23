from calculate_fee import calculate_fees

def process_upload(storages, storage_name, filename, filesize, is_paid_plan):
    """UPLOADコマンドの処理を行う関数"""
    storage = storages[storage_name]
    prev_max_usage = storage["max_usage"]
    
    # 無料プランでタイプBストレージを使用しようとした場合
    if not is_paid_plan and storage["type"] == "B":
        print("UPLOAD: this storage location is not available on the free plan")
        return is_paid_plan
        
    # 同名のファイルが既に存在する場合
    if filename in storage["files"]:
        print("UPLOAD: file already exists")
        return is_paid_plan
    
    # ファイルをアップロード（一時的な処理）
    storage["files"][filename] = filesize
    storage["current_usage"] += filesize
    storage["max_usage"] = max(storage["max_usage"], storage["current_usage"])
    storage["update_amount"] += filesize
    
    # 料金計算
    storage_fee, update_fee, usage_fee = calculate_fees(storages)
    
    # 無料プランで、操作後の利用料金が0円を超える場合
    if not is_paid_plan and usage_fee > 0:
        # 状態を元に戻す
        del storage["files"][filename]
        storage["current_usage"] -= filesize
        storage["max_usage"] = prev_max_usage
        storage["update_amount"] -= filesize
        print("UPLOAD: free plan fee limit exceeded")
    else:
        print(f"UPLOAD: {storage_fee} {update_fee} {usage_fee}")
    
    return is_paid_plan