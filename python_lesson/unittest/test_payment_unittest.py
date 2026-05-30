import unittest
from main import payment, PaymentError

class TestPayment(unittest.TestCase):
    def setUp(self):
        self.payment = payment(1000)

    # assertEqual(a, b): aとbが等しいか
    # 2行のassertEqualは関数の返り値とインスタンスのbalanceが等しいかチェック
    def test_charge_success(self):
        new_balance = self.payment.charge(500)
        self.assertEqual(new_balance, 1500)
        self.assertEqual(self.payment.balance, 1500)

    def test_charge_failure(self):
        # assertRaises(ErrorType): 定義したErrorを返す
        # 0円チャージやマイナスチャージはエラー
        with self.assertRaises(PaymentError):
            self.payment.charge(0)
        with self.assertRaises(PaymentError):
            self.payment.charge(-100)
    
    def test_pay_success(self):
        new_balance = self.payment.pay(500)
        self.assertEqual(new_balance, 500)
        self.assertEqual(self.payment.balance, 500)

    def test_pay_failure(self):
        # 0円支払い、マイナス支払い、残高不足はエラー
        with self.assertRaises(PaymentError):
            self.payment.pay(0)
        with self.assertRaises(PaymentError):
            self.payment.pay(-100)
        with self.assertRaises(PaymentError):
            self.payment.pay(2000)

if __name__ == '__main__':
    unittest.main()