from xmlrpc.server import SimpleXMLRPCServer

# Database stok sederhana
stok_db = {"P001": 20, "P002": 50, "P999": 20}

def cek_stok(produk_id):
    return stok_db.get(produk_id, 0)

def kurangi_stok(produk_id, jumlah):
    if stok_db.get(produk_id, 0) >= jumlah:
        stok_db[produk_id] -= jumlah
        return True, f"Stok {produk_id} berhasil dikurangi. Sisa: {stok_db[produk_id]}"
    return False, "Stok tidak mencukupi!"

server = SimpleXMLRPCServer(("127.0.0.1", 9000))
print("Layanan Stok (RPC Server) berjalan di port 9000...")
server.register_function(cek_stok, "cek_stok")
server.register_function(kurangi_stok, "kurangi_stok")
server.serve_forever()