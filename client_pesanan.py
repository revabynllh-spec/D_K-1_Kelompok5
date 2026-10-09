import xmlrpc.client

stok_service = xmlrpc.client.ServerProxy("http://127.0.0.1:9000/")

produk = "P001"
jumlah_beli = 2

print(f"Cek stok awal {produk}: {stok_service.cek_stok(produk)}")

# Melakukan pemesanan
status, pesan = stok_service.kurangi_stok(produk, jumlah_beli)
print(f"Status Pesanan: {pesan}")
print(f"Cek stok akhir {produk}: {stok_service.cek_stok(produk)}")