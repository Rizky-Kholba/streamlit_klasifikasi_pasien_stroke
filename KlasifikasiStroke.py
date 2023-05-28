import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('KlasifikasiStroke.sav', 'rb'))

st.title('Klasifikasi Pasien Stroke')
col1, col2 = st.columns(2)


optPernikahan = ['Menikah', 'Belum Menikah']
optKelamin = ['Wanita', 'Pria']
optProfesi = ['Privasi', 'Wiraswasta', 'Anak-anak',
              'Pegawai Negeri Sipil', 'Tidak Bekerja']
optRumah = ['Perkotaan', 'Pedesaan']
optPerokok = ['Tidak Pernah Merokok',
              'Pernah Merokok', 'Merokok', 'Tidak Tahu']
Option = ['Iya', 'Tidak']


with col1:
    jnsKelamin = st.selectbox('Jenis Kelamin', optKelamin)
    if jnsKelamin == 'Wanita':
        jnsKelamin = 0
    else:
        jnsKelamin = 1

    Umur = st.number_input('Umur')

    Hipertensi = st.selectbox('Hipertensi', Option)
    if Hipertensi == 'Tidak':
        Hipertensi = 0
    else:
        Hipertensi = 1

    pyktJantung = st.selectbox('Penyakit jantung', Option)
    if pyktJantung == 'Tidak':
        pyktJantung = 0
    else:
        pyktJantung = 1

    stsPernikahan = st.selectbox('Status Pernikahan', optPernikahan)
    if stsPernikahan == 'Belum Menikah':
        stsPernikahan = 0
    else:
        stsPernikahan = 1

with col2:
    Profesi = st.selectbox('Profesi', optProfesi)
    if Profesi == 'Privasi':
        Profesi = 0
    elif Profesi == 'Wiraswasta':
        Profesi = 1
    elif Profesi == 'Anak-anak':
        Profesi = 2
    elif Profesi == 'Pegawai Negeri Sipil':
        Profesi = 3
    else:
        Profesi = 4

    tmpTinggal = st.selectbox('Tempat Tingaal', optRumah)
    if tmpTinggal == 'Perkotaan':
        tmpTinggal = 0
    else:
        tmpTinggal = 1

    GulaDarah = st.number_input('Kadar Glukosa/Gula Darah')

    BMI = st.number_input('Indeks Masa Tubuh/Berat Badan Ideal')

    stsPerokok = st.selectbox('Status Perokok', optPerokok)
    if stsPerokok == 'Tidak Pernah Merokok':
        stsPerokok = 0
    elif stsPerokok == 'Tidak Tahu':
        stsPerokok = 1
    elif stsPerokok == 'Pernah Merokok':
        stsPerokok = 2
    else:
        stsPerokok = 3


predict = ''
if st.button('Hasil Prediksi'):
    predict = model.predict([[
        jnsKelamin,
        Umur,
        Hipertensi,
        pyktJantung,
        stsPernikahan,
        Profesi,
        tmpTinggal,
        GulaDarah,
        BMI,
        stsPerokok
    ]])

    if (predict[0] == 0):
        predict = 'Pasien kemungkinan tidak terkena stroke'
    else:
        predict = 'Pasien kemungkinan terkena stroke'

st.success(predict)
