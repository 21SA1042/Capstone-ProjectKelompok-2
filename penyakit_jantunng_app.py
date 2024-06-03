import pickle
import numpy as np
import streamlit as st

# Load saved model and scaler
model = pickle.load(open('penyakit_jantung.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

# Streamlit app
st.title("Prediksi Resiko Penyakit Jantung")

# Judul web
usia = st.sidebar.slider("Usia", 20, 100, 50)

# Input fitur jenis kelamin
jenis_kelamin = st.sidebar.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Input fitur anemia
anemia = st.sidebar.selectbox("Anemia", ["Tidak", "Ya"])

# Input fitur creatinine_phosphokinase
creatinine_phosphokinase = st.sidebar.number_input("Creatinine Phosphokinase")

# Input fitur diabetes
diabetes = st.sidebar.selectbox("Diabetes", ["Tidak", "Ya"])

# Input fitur pecahan_injeksi
pecahan_injeksi = st.sidebar.number_input("Pecahan Injeksi")

# Input fitur tekanan_darah_tinggi
tekanan_darah_tinggi = st.sidebar.selectbox("Tekanan Darah Tinggi", ["Tidak", "Ya"])

# Input fitur trombosit
trombosit = st.sidebar.number_input("Trombosit")

# Input fitur kebiasaan_merokok
kebiasaan_merokok = st.sidebar.selectbox("Kebiasaan Merokok", ["Tidak", "Ya"])

# Input fitur waktu
waktu = st.sidebar.number_input("Waktu")

# Input fitur serum_natrium
serum_natrium = st.sidebar.number_input("Serum Natrium")

# Input fitur serum_kreatinin
serum_kreatinin = st.sidebar.number_input("Serum Kreatinin")

if st.sidebar.button("Prediksi"):
    # Membuat array 1D dari input
    input_data = np.array([
        usia,
        1 if anemia == "Ya" else 0,
        creatinine_phosphokinase,
        1 if diabetes == "Ya" else 0,
        pecahan_injeksi,
        1 if tekanan_darah_tinggi == "Ya" else 0,
        trombosit,
        serum_kreatinin,
        serum_natrium,
        1 if jenis_kelamin == "Laki-laki" else 0,
        1 if kebiasaan_merokok == "Ya" else 0,
        waktu
    ])

    # Mengubah array 1D menjadi 2D
    input_data_reshaped = input_data.reshape(1, -1)
    print("Before scaling:", input_data_reshaped)

    # Transform input data with scaler
    input_data_transformed = scaler.transform(input_data_reshaped)
    print("After scaling:", input_data_transformed)

    # Melakukan prediksi dengan model
    hasil_prediksi = model.predict(input_data_transformed)

    # Menampilkan nilai-nilai input
    st.write("Detail Nilai Input:")
    st.write(f"Usia: {usia}")
    st.write(f"Jenis Kelamin: {jenis_kelamin}")
    st.write(f"Anemia: {anemia}")
    st.write(f"Creatinine Phosphokinase: {creatinine_phosphokinase}")
    st.write(f"Diabetes: {diabetes}")
    st.write(f"Pecahan Injeksi: {pecahan_injeksi}")
    st.write(f"Tekanan Darah Tinggi: {tekanan_darah_tinggi}")
    st.write(f"Trombosit: {trombosit}")
    st.write(f"Kebiasaan Merokok: {kebiasaan_merokok}")
    st.write(f"Waktu: {waktu}")
    st.write(f"Serum Natrium: {serum_natrium}")
    st.write(f"Serum Kreatinin: {serum_kreatinin}")

    # Menampilkan hasil prediksi kepada pengguna
    if hasil_prediksi[0] == 1:
        st.write("Hasil Prediksi: Pasien berisiko terkena penyakit jantung.")
    else:
        st.write("Hasil Prediksi: Pasien tidak berisiko terkena penyakit jantung.")
