from calculate_fee import calculate_fees
from system.storage import Storage

def process_calc(storages: dict[str, Storage]) -> None:
    """CALCコマンドの処理を行う関数"""
    storage_usages_kb = []

    for storage_obj in storages.values():
        storage_usages_kb.append(storage_obj.current_usage)
    
    storage_fee, update_fee, usage_fee = calculate_fees(storages)
    
    print(f"CALC: [{' '.join(map(str, storage_usages_kb))}] {storage_fee} {update_fee} {usage_fee}")

    # 月間統計のリセット 
    for storage_obj in storages.values():
        storage_obj.reset_monthly_stats()