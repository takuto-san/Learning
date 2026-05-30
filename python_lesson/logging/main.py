from payment import Payment, PaymentError

def main():
    wallet = Payment(1000)
    try:
        wallet.charge(500)
        wallet.pay(200)
        wallet.pay(2000)  # This should raise an error
    except PaymentError as e:
        print(f"Charge failed: {e}")

if __name__ == "__main__":
    main()