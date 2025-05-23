from calculate_fee import calculate_fees

def process_calc(storages):
    """CALCコマンドの処理を行う関数"""
    storage_usages = []
    for storage in storages.values():
        storage_usages.append(storage["current_usage"])
    
    storage_fee, update_fee, usage_fee = calculate_fees(storages)
    
    # 月間統計のリセット
    for storage in storages.values():
        storage["max_usage"] = storage["current_usage"]
        storage["update_amount"] = 0
    
    print(f"CALC: [{' '.join(map(str, storage_usages))}] {storage_fee} {update_fee} {usage_fee}")