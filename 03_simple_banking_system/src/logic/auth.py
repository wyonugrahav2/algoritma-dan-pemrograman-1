def verify_pin(input_pin, account):
    """Memverifikasi apakah PIN yang dimasukkan cocok dengan data akun."""
    return str(account.get("pin")) == str(input_pin)