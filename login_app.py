import streamlit as st
import sqlite3

# Fungsi untuk membuat database dan tabel pengguna
def create_usertable():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, email TEXT, password TEXT)')
    conn.commit()
    conn.close()

# Fungsi untuk menambahkan pengguna baru ke database
def add_user(username, email, password):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('INSERT INTO userstable(username, email, password) VALUES (?,?,?)', (username, email, password))
    conn.commit()
    conn.close()
  
# Fungsi untuk memverifikasi login pengguna
def login_user(email, password):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE email =? AND password = ?', (email, password))
    data = c.fetchall()
    conn.close()
    return data

# Fungsi untuk memeriksa apakah email sudah terdaftar
def check_email_exists(email):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE email =?', (email,))
    data = c.fetchall()
    conn.close()
    return data

# Aplikasi Streamlit
def app():
    st.title('Selamat Datang')
    st.header('Tentukan cara yang lebih baik untuk memprediksi kesehatan jantung anda dengan jantung cerdas')

    # Membuat tabel pengguna jika belum ada
    create_usertable()

    choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])

    if choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if st.button('Login'):
            if login_user(email, password):
                st.success('Login successful!')
            else:
                st.error('Email atau password salah')
    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter your unique username')

        if st.button('Sign Up'):
            if check_email_exists(email):
                st.error('Email sudah terdaftar')
            else:
                add_user(username, email, password)
                st.success('Signup successful!')

if __name__ == '__main__':
    app()
