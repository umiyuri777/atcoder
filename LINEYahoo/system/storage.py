class Storage:
    def __init__(self, name: str, storage_type: str, storage_fee_coef: float, update_fee_coef: float):
        self.name: str = name
        self.type: str = storage_type  # "A" or "B"
        self.storage_fee_coef: float = storage_fee_coef # 保存料金係数
        self.update_fee_coef: float = update_fee_coef # 更新料金係数
        self.files: dict[str, int] = {}  # filename: filesize (KB)
        self.current_usage: int = 0  # KB
        self.max_usage: int = 0      # KB (今月の最大)
        self.update_amount: int = 0  # KB (今月の更新量合計)

    def get_type(self) -> str:
        """ストレージのタイプを取得する"""
        return self.type

    def has_file(self, filename: str) -> bool:
        """指定されたファイルが存在するかどうかを確認する"""
        return filename in self.files

    def get_file_size(self, filename: str) -> int | None:
        """指定されたファイルのサイズを取得する"""
        return self.files.get(filename)

    def reset_monthly_stats(self):
        """CALCコマンド後に月間統計をリセットする"""
        self.max_usage = self.current_usage 
        self.update_amount = 0
