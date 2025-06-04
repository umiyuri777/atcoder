import math
from system.storage import Storage # 型ヒント用

def calculate_fees(storages: dict[str, Storage]) -> tuple[int, int, int]:
    """料金を計算する関数"""
    total_storage_fee = 0
    total_update_fee = 0

    for storage_obj in storages.values():
        # 保存料金
        current_storage_fee = 0
        if storage_obj.max_usage > 0:
            # S_max MB（小数点以下切り上げ）
            s_max_mb = math.ceil(storage_obj.max_usage / 1000.0)
            
            # 保存料金計算
            storage_fee = s_max_mb * storage_obj.storage_fee_coef
            current_storage_fee = math.ceil(storage_fee)
        total_storage_fee += int(current_storage_fee)

        # 更新料金
        current_update_fee = 0
        if storage_obj.update_amount > 0:
            # U MB（小数点以下切り上げ）
            u_mb = math.ceil(storage_obj.update_amount / 1000.0)
            
            # 更新料金計算
            update_fee = u_mb * storage_obj.update_fee_coef
            current_update_fee = math.ceil(update_fee)
        total_update_fee += int(current_update_fee)
    
    usage_fee = max(0, total_storage_fee + total_update_fee - 1000)
    return total_storage_fee, total_update_fee, usage_fee