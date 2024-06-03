import streamlit as st
import random

# Definisikan dictionary untuk respons
responses = {
    "halo": ["Halo! Ada yang bisa saya bantu?", "Hai! Bagaimana kabarmu hari ini?", "Selamat datang! Ada pertanyaan?"],
    "saran untuk pencegahan gagal jantung": ["Untuk pencegahan gagal jantung, sebaiknya Anda menjaga pola makan sehat, rutin berolahraga, dan menghindari merokok.", "Pastikan Anda memantau tekanan darah dan kadar kolesterol secara teratur, serta berkonsultasi dengan dokter Anda secara rutin.", "Menghindari konsumsi alkohol berlebihan dan mengelola stres juga penting dalam pencegahan gagal jantung."],
    "bantu saya": ["Tolong berikan rekomendasi vitamin yang bagus.", "Berikan saya rekomendasi vitamin."],
    "saran untuk rekomendasi vitamin": ["Vitamin C baik untuk sistem kekebalan tubuh.", "Vitamin D penting untuk kesehatan tulang.", "Vitamin B kompleks membantu fungsi otak dan energi."],
    "saran untuk rekomendasi obat": ["Konsultasikan dengan dokter untuk obat yang tepat sesuai dengan kondisi Anda.", "Pastikan untuk mengikuti dosis yang dianjurkan oleh dokter.", "Selalu baca informasi pada kemasan obat dan tanyakan apoteker jika ada yang tidak jelas."],
    "terima kasih": ["Sama-sama!", "Senang bisa membantu!", "Terima kasih kembali!"],
    "selamat tinggal": ["Sampai jumpa!", "Selamat tinggal! Semoga hari Anda menyenangkan!", "Sampai bertemu lagi!"]
}

# Buat judul aplikasi
st.title("Chatbot")

# Simpan riwayat percakapan
if 'history' not in st.session_state:
    st.session_state.history = []

# Input dari pengguna
user_input = st.text_input("Masukkan pesan Anda:")

# Tampilkan respons berdasarkan input pengguna
if user_input:
    user_input = user_input.lower()
    st.session_state.history.append(f"Anda: {user_input}")
    
    if user_input in responses:
        response = random.choice(responses[user_input])
    else:
        response = "Maaf, saya tidak mengerti pertanyaan Anda."
    
    st.session_state.history.append(f"Bot: {response}")

# Tampilkan riwayat percakapan
if st.session_state.history:
    for line in st.session_state.history:
        st.write(line)


