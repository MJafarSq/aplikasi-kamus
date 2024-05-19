meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SHEESH" : "sedikit ketidaksetujuan",
            "CREEPY" : "menakutkan, tidak menyenangkan"
            }

word =  input('masukan kata kata:')
word = word.upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('gk ada di dict!')














