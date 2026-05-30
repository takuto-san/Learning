## Unittest Overview

### How to test?
Unittest/
├── main.py                  # テスト対象
└── test_payment_unittest.py  # ここにunittestを書く

```console
Run test:
$ cd Unittest
$　python -m unittest test_payment_unittest.py

Success:
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

Error:
Traceback (most recent call last):
  File "~/Develop/Udemy/Python_lesson/Unittest/test_payment_unittest.py", line 12, in test_charge_success
    self.assertEqual(new_balance, 1200)
AssertionError: 1500 != 1200
```

### coverage
```console
$ pip install coverage
$ cd Unittest
$ coverage run -m unittest test_payment_unittest.py
(.coverage file is made)
```
```console
$ coverage report

Output: 
Name                      Stmts   Miss  Cover
---------------------------------------------
main.py                      17      0   100%
test_payment_unittest.py      27      1    96%
---------------------------------------------
TOTAL                        44      1    98%
```

## pytest
pytestは、ファイルの中から名前がtest_で始まる関数を自動的に探して実行する。
そのため、test_payment_pytest.py内の関数名は「test_」で始まる必要がある。

@pytest fixtureをインスタンス生成部分で宣言しておくと、selfを書かないで済む。

```console
# 全ファイル対象
$ pytest
# 特定のファイル対象
$ pytest test_payment_pytest.py または python -m pytest test_payment_pytest.py
```

```console
Output: 
====================================== test session starts =======================================
platform darwin -- Python 3.10.16, pytest-8.3.5, pluggy-1.5.0
rootdir: /Users/OCUST013/Develop/Udemy/Python_lesson/Unittest
collected 4 items                                                                                

test_payment_pytest.py ....                                                                 [100%]

======================================= 4 passed in 0.01s ========================================
```