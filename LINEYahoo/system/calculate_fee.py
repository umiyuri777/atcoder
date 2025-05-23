import math

def calculate_fees(storages):
    """料金を計算する関数"""
    storage_fee = 0
    update_fee = 0

    for s_data in storages.values():
        # 保存料金
        if s_data["max_usage"] > 0:
            # S_max MB（小数点以下切り上げ）
            s_max_mb_int = (s_data["max_usage"] + 999) // 1000
            
            # このストレージの今月の保存料金は S_max × μ_store 円（小数点以下切り上げ）
            raw_storage_fee_for_s = s_max_mb_int * s_data["storage_fee_coef"]
            storage_fee_increment = math.ceil(raw_storage_fee_for_s)
        else:
            storage_fee_increment = 0
        storage_fee += int(storage_fee_increment) # math.ceil は float を返すことがあるので int() で整数化

        # 更新料金
        if s_data["update_amount"] > 0:
            # U MB（小数点以下切り上げ）
            u_mb_int = (s_data["update_amount"] + 999) // 1000
            
            # このストレージの今月の更新料金は U × μ_update 円（小数点以下切り上げ）
            raw_update_fee_for_s = u_mb_int * s_data["update_fee_coef"]
            update_fee_increment = math.ceil(raw_update_fee_for_s)
        else:
            update_fee_increment = 0
        update_fee += int(update_fee_increment) # math.ceil は float を返すことがあるので int() で整数化
    
    usage_fee = max(0, storage_fee + update_fee - 1000)
    return storage_fee, update_fee, usage_fee