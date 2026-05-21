import streamlit as st
from Backend import WarehouseStack

# Konfigurasi Halaman (Harus diletakkan paling atas)
st.set_page_config(
    page_title="Sistem Gudang LIFO", 
    page_icon="📦", 
    layout="wide"
)

# Inisialisasi session_state agar data stack tidak hilang saat auto-rerun Streamlit
if 'warehouse' not in st.session_state:
    st.session_state.warehouse = WarehouseStack()

# Bagian Header
st.title("📦 Sistem Manajemen Gudang (Stack)")
st.markdown("Simulasi penyimpanan barang dengan metode **LIFO (Last In, First Out)**.")
st.markdown("---")

# Membagi layar menjadi dua kolom
col1, col2 = st.columns([1, 2])

# KOLOM KIRI: Kontrol Barang (Input & Eksekusi)
with col1:
    st.header("⚙️ Kontrol Operasi")
    
    # Form untuk Push (Tambah Barang)
    with st.form("push_form", clear_on_submit=True):
        st.subheader("Penerimaan Barang")
        new_item = st.text_input("Nama Barang Baru:", placeholder="Misal: Monitor ASUS 24 Inch")
        submit_push = st.form_submit_button("➕ Masukkan ke Gudang")

        if submit_push:
            if new_item.strip():
                st.session_state.warehouse.push(new_item.strip())
                st.success(f"Berhasil menyimpan '{new_item}'!")
                st.rerun() # Refresh tampilan
            else:
                st.warning("Nama barang tidak boleh kosong!")

    st.markdown("<br>", unsafe_allow_html=True)

    # Tombol untuk Pop (Ambil Barang)
    st.subheader("Pengeluaran Barang")
    st.info("Barang yang keluar adalah barang yang paling terakhir masuk.")
    if st.button("➖ Ambil Barang", use_container_width=True, type="primary"):
        popped_item = st.session_state.warehouse.pop()
        if popped_item:
            st.success(f"Berhasil mengambil '{popped_item}' dari gudang!")
            st.rerun()
        else:
            st.error("Gudang kosong! Tidak ada barang yang bisa diambil.")


# KOLOM KANAN: Visualisasi dan Status Gudang
with col2:
    st.header("📊 Status Gudang Saat Ini")

    # Mengambil data dari backend
    total_items = st.session_state.warehouse.size()
    top_item = st.session_state.warehouse.peek() or "Tidak ada"
    all_items = st.session_state.warehouse.get_all()

    # Menampilkan Metrik/Statistik
    m1, m2 = st.columns(2)
    m1.metric("Total Barang di Gudang", f"{total_items} Unit")
    m2.metric("Barang Teratas (Siap Diambil)", top_item)

    st.markdown("### 🗄️ Visualisasi Tumpukan (Stack)")
    
    # Menampilkan isi stack dengan gaya yang menarik
    if not all_items:
        st.info("Gudang saat ini kosong. Silakan masukkan barang dari panel kontrol di sebelah kiri.")
    else:
        # Container untuk memberikan efek box
        with st.container(border=True):
            for i, item in enumerate(all_items):
                if i == 0:
                    # Tampilan untuk barang paling atas (Top)
                    st.markdown(f"### 🟢 **{item}** *(Top - Keluar Pertama)*")
                else:
                    # Tampilan untuk barang di bawahnya
                    st.markdown(f"##### 📦 {item}")
                
                # Menambahkan garis pemisah antar barang kecuali barang paling bawah
                if i < len(all_items) - 1:
                    st.divider()