def check_balance(account):
    """Mengembalikan saldo terkini dari akun."""
    return account.get("balance", 0)


def deposit(account, amount):
    """Menambahkan saldo ke akun (Setor Tunai)."""
    if amount <= 0:
        return False, "Nominal setor harus lebih dari 0!"
    
    account["balance"] += amount
    return True, f"Berhasil menyetor Rp {amount:,}. Saldo baru: Rp {account['balance']:,}"


def withdraw(account, amount):
    """Mengurangi saldo dari akun dengan validasi kecukupan saldo (Tarik Tunai)."""
    if amount <= 0:
        return False, "Nominal tarik harus lebih dari 0!"
    
    if amount > account["balance"]:
        return False, "Saldo tidak mencukupi untuk melakukan penarikan!"
    
    account["balance"] -= amount
    return True, f"Berhasil menarik Rp {amount:,}. Saldo tersisa: Rp {account['balance']:,}"