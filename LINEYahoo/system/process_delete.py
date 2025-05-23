from calculate_fee import calculate_fees

def process_delete(storages, storage_name, filename, is_paid_plan):
    """DELETEコマンドの処理を行う関数"""
    storage = storages[storage_name]
    
    # 無料プランでタイプBストレージを使用しようとした場合
    if not is_paid_plan and storage["type"] == "B":
        print("DELETE: this storage location is not available on the free plan")
        return is_paid_plan
        
    # ファイルが存在しない場合
    if filename not in storage["files"]:
        print("DELETE: file does not exist")
        return is_paid_plan
    
    # 操作前の状態を保存
    filesize = storage["files"][filename]
    prev_current_usage = storage["current_usage"]
    # prev_max_usage はDELETEでは変更されないので、ロールバック時も元のままで良い
    prev_update_amount = storage["update_amount"]
    
    # ファイルを削除（一時的な処理）
    del storage["files"][filename]
    storage["current_usage"] -= filesize
    # storage["max_usage"] はこの操作では変更されない（減ることはない）
    storage["update_amount"] += filesize
    
    # 料金計算
    storage_fee, update_fee, usage_fee = calculate_fees(storages)
    
    # 無料プランで、操作後の利用料金が0円を超える場合
    if not is_paid_plan and usage_fee > 0:
        # 状態を元に戻す
        storage["files"][filename] = filesize # 削除したファイルを戻す
        storage["current_usage"] = prev_current_usage
        # storage["max_usage"] は変更していないので、そのままで良い
        storage["update_amount"] = prev_update_amount
        print("DELETE: free plan fee limit exceeded")
    else:
        print(f"DELETE: {storage_fee} {update_fee} {usage_fee}")
    
    return is_paid_plan