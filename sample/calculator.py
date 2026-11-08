"""シンプルな電卓モジュール（Confluence 自動ドキュメント生成のサンプル）。"""

from __future__ import annotations


class Calculator:
    """四則演算と計算履歴を持つ電卓。"""

    def __init__(self) -> None:
        self.history: list[str] = []

    def add(self, a: float, b: float) -> float:
        """a + b を返す。"""
        return self._record("+", a, b, a + b)

    def subtract(self, a: float, b: float) -> float:
        """a - b を返す。"""
        return self._record("-", a, b, a - b)

    def multiply(self, a: float, b: float) -> float:
        """a * b を返す。"""
        return self._record("*", a, b, a * b)

    def divide(self, a: float, b: float) -> float:
        """a / b を返す。b が 0 の場合は ZeroDivisionError を送出する。"""
        if b == 0:
            raise ZeroDivisionError("0 で割ることはできません")
        return self._record("/", a, b, a / b)

    def clear_history(self) -> None:
        """計算履歴を消去する。"""
        self.history.clear()

    def _record(self, op: str, a: float, b: float, result: float) -> float:
        self.history.append(f"{a} {op} {b} = {result}")
        return result


def main() -> None:
    calc = Calculator()
    calc.add(1, 2)
    calc.multiply(3, 4)
    calc.divide(10, 4)
    for line in calc.history:
        print(line)


if __name__ == "__main__":
    main()
