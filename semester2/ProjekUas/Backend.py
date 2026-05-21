class WarehouseStack:
    def __init__(self):
        """Inisialisasi stack kosong untuk gudang."""
        self.items = []

    def is_empty(self):
        """Mengecek apakah gudang kosong."""
        return len(self.items) == 0

    def push(self, item):
        """Menambahkan barang baru ke tumpukan paling atas."""
        self.items.append(item)

    def pop(self):
        """Mengambil barang dari tumpukan paling atas."""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Melihat barang apa yang ada di tumpukan paling atas tanpa mengambilnya."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        """Menghitung total barang yang ada di gudang."""
        return len(self.items)

    def get_all(self):
        """
        Mengambil seluruh isi gudang.
        Dibalik (reverse) agar visualisasinya sesuai dengan konsep stack (yang terakhir masuk ada di atas).
        """
        return self.items[::-1]