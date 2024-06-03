import streamlit as st

st.title("Rekomendasi Pola Hidup Sehat Untuk Penderita Gagal Jantung")

st.write("Gagal jantung adalah kondisi di mana jantung tidak dapat memompa darah sebagaimana mestinya. Berikut adalah beberapa rekomendasi pola hidup sehat yang dapat membantu penderita gagal jantung")

def show_recommendations():
    st.header("Rekomendasi Pola Hidup Sehat")

    st.subheader("1. Pola Makan Sehat")
    st.image('Makanan Sehat.jpg', caption='Makanan sehat', use_column_width=True)
    st.write("""
    - Kurangi asupan garam
    - Konsumsi makanan rendah lemak jenuh
    - Perbanyak buah dan sayuran
    - Pilih protein tanpa lemak seperti ikan dan kacang-kacangan
    """)



    st.subheader("2. Aktivitas Fisik")
    st.image('olahraga.jpg', caption='Olahgara', use_column_width=True)
    st.write("""
    - Lakukan olahraga ringan seperti berjalan kaki, bersepeda, atau berenang
    - Konsultasikan dengan dokter sebelum memulai program olahraga
    """)



    st.subheader("3. Pengelolaan Berat Badan")
    st.image('pencegahan obesitas.png', caption='pencegahan obesitas', use_column_width=True)
    st.write("""
    - Pertahankan berat badan ideal
    - Hindari obesitas dengan pola makan sehat dan olahraga teratur
    """)



    st.subheader("4. Penghentian Kebiasaan Buruk")
    st.image('berhenti merokok.webp', caption='No Smoking', use_column_width=True)
    st.write("""
    - Berhenti merokok
    - Batasi konsumsi alkohol
    """)



    st.subheader("5. Pengobatan dan Pemantauan Kesehatan")
    st.image('periksa ke dokter spealis jantung.jpg', caption='rutin kontrol ke dokter spealis ', use_column_width=True)
    st.write("""
    - Minum obat sesuai anjuran dokter
    - Rutin kontrol ke dokter untuk memantau kondisi jantung
    - Monitor tekanan darah dan kadar kolesterol
    """)



def get_feedback():
    st.header("Berikan Umpan Balik Anda")
    feedback = st.text_area("Apakah rekomendasi ini membantu Anda? Berikan saran atau komentar Anda.")
    if st.button("Kirim"):
        st.write("Terima kasih atas umpan balik Anda!")


show_recommendations()
get_feedback()









    
