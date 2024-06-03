import streamlit as st 


st.title("Informasi Penyakit Gagal Jantung")


st.image('gagal jantung.webp', caption='Penyakit Gagal Jantung', use_column_width=True)


# Introduction
st.header("Apa itu Gagal Jantung?")
st.write("""
Gagal jantung adalah kondisi di mana jantung tidak dapat memompa darah sebagaimana mestinya. Hal ini dapat terjadi karena berbagai alasan, termasuk penyakit jantung koroner, tekanan darah tinggi, dan kondisi lainnya yang melemahkan jantung.
""")


# Bagian gejala
st.header("Gejala Gagal Jantung")
st.write("""
Gejala gagal jantung bisa bervariasi tergantung pada seberapa parah kondisinya, termasuk:
- Sesak napas saat beraktivitas atau saat berbaring
- Kelelahan dan kelemahan
- Pembengkakan pada kaki, pergelangan kaki, dan kaki
- Detak jantung cepat atau tidak teratur
- Batuk atau mengi yang terus-menerus
- Peningkatan kebutuhan untuk buang air kecil di malam hari
""")


# Bagian penyebab
st.header("Penyebab Gagal Jantung")
st.write("""
Penyebab umum gagal jantung meliputi:
- Penyakit jantung koroner
- Serangan jantung
- Tekanan darah tinggi
- Penyakit katup jantung
- Kerusakan otot jantung (kardiomiopati)
- Miokarditis
- Cacat jantung bawaan
- Gangguan irama jantung
""")


# Bagian Pencegahan
st.header("Pencegahan Gagal Jantung")
st.write("""
Beberapa langkah yang dapat membantu mencegah gagal jantung termasuk:
- Mengelola kondisi medis yang mendasarinya, seperti hipertensi, diabetes, dan penyakit jantung koroner
- Mengonsumsi makanan sehat dengan diet rendah garam dan lemak jenuh
- Berolahraga secara teratur
- Menghindari merokok dan mengurangi konsumsi alkohol
- Memantau dan mengelola tingkat stres
""")


#further information
st.write("Untuk informasi lebih lanjut, kunjungi situs web resmi [Kementerian Kesehatan Republik Indonesia](https://www.kemkes.go.id/).")


# Footer
st.write("**Sumber**: Informasi ini disusun berdasarkan data dari berbagai sumber medis dan kesehatan.")