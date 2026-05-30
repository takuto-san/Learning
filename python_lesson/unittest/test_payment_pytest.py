import pytest
from main import payment, PaymentError

@pytest.fixture
def wallet():
    return payment(1000)

def test_charge_success(wallet):
    new_balance = wallet.charge(500)
    assert new_balance == 1500 # chargeメソッドの返り値
    assert wallet.balance == 1500 # インスタンスが保持する値

def test_charge_failure(wallet):
    with pytest.raises(PaymentError):
        wallet.charge(0)
    with pytest.raises(PaymentError):
        wallet.charge(-100)

def test_pay_success(wallet):
    new_balance = wallet.pay(500)
    assert new_balance == 500
    assert wallet.balance == 500

def test_pay_failure(wallet):
    with pytest.raises(PaymentError):
        wallet.pay(0)
    with pytest.raises(PaymentError):
        wallet.pay(-100)
    with pytest.raises(PaymentError):
        wallet.pay(2000)