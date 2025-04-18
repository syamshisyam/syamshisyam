
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Konstanta
P = 5e15  # total proyek
biaya_kuliah = 1e8  # Rp 100 juta per mahasiswa
penduduk_jakarta_usia_kuliah = 1_320_000

# Slider input
st.title("🎓 Simulasi Interaktif Dana Korupsi & Pendidikan")

st.sidebar.header("🔧 Parameter Korupsi")
x = st.sidebar.slider("Markup Harga (x)", 0.0, 1.0, 0.2, 0.01)
y = st.sidebar.slider("Penggelapan Dana (y)", 0.0, 1.0, 0.2, 0.01)
z = st.sidebar.slider("Pengadaan Fiktif (z)", 0.0, 1.0, 0.2, 0.01)

# Fungsi gabungan
def dana_korupsi(x, y, z):
    return P * (0.4 * x**2 + 0.35 * y + 0.25 * np.log(1 + z))

dana = dana_korupsi(x, y, z)
jumlah_mahasiswa = dana // biaya_kuliah
persen_tercover_jakarta = min(100, (jumlah_mahasiswa / penduduk_jakarta_usia_kuliah) * 100)

# Output
st.subheader("📊 Hasil Simulasi")

st.metric("Dana yang Dikumpulkan dari Korupsi", f"Rp {dana:,.0f}")
st.metric("Mahasiswa yang Bisa Dibiayai", f"{int(jumlah_mahasiswa):,} orang")
st.metric("Persentase Penduduk Jakarta Usia Kuliah yang Tercover", f"{persen_tercover_jakarta:.2f}%")

# Pie chart visual
labels = ['Biaya Kuliah Jakarta', 'Sisa untuk Provinsi Lain']
sizes = [min(jumlah_mahasiswa, penduduk_jakarta_usia_kuliah),
         max(jumlah_mahasiswa - penduduk_jakarta_usia_kuliah, 0)]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)
