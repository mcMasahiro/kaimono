from enum import Enum
import sys

def main():
    salmon_price = None
    if len(sys.argv) > 1:
        salmon_price = int(sys.argv[1]) # 鮭の価格をコマンドライン引数から取得

    buyer = Buyer(salmon_price)
    buyer.buy_main()    #メイン食材購入
    buyer.buy_sub() # サブ食材購入
    buyer.buy_negi()    # ネギ購入
    buyer.print_bought_items() # 購入リスト出力
    
class Item(Enum):
    SALMON = "salmon"   # 鮭
    MEAT = "meat"   # ひき肉
    CHICKEN = "chicken" # 鳥もも
    NEGI = "negi"   # ネギ

class Buyer:
    def __init__(self, salmon_price: int | None = None) -> None:
        self._salmon_price = salmon_price
        self._bought_items: list[Item] = []

    def buy_main(self) -> None:
        """メイン食材購入
        description: 鮭を2つか、鳥ももを1つ購入する
        """
        if self._is_buy_salmon():
            self._buy_item(Item.SALMON, 2)
            return
        self._buy_item(Item.CHICKEN, 1)

    def buy_negi(self) -> None:
        """ネギ購入
        description: ネギを1つ購入する
        """
        self._buy_item(Item.NEGI, 1)

    def buy_sub(self) -> None:
        """サブ食材購入
        description: ひき肉を1つ購入する
        """
        self._buy_item(Item.MEAT, 1)
        print("サブ食材購入完了")

    def print_bought_items(self) -> None:
        """購入リストを出力する"""
        print(self._bought_items)
        print("完了")

    def _buy_item(self, item: Item, num: int) -> None:
        """指定アイテムを購入する
        Args:
            item (Item): 購入アイテム
            num (int): 購入数
        """        
        for _ in range(num):
            self._bought_items.append(item)
    
    def _is_buy_salmon(self) -> bool:
        """鮭を2つ買うか判定する"""
        if self._salmon_price is None:
            return False
        if self._salmon_price * 2 > 350:
            return False
        return True
    
if __name__ == "__main__":
    main()