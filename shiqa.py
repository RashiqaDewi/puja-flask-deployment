from flask import Flask, request, render_template
import random
import logging

app = Flask(__name__)


pesan_default = [
    "Makan patty itu",
    "Berdansalah",
    "Buang selada itu",
    "Jaga kasir",
    "Saatnya shif mu jaga kasir",
    "Temui aku di rumah Sandy",
    "Jangan ambil resep krabby patty",
    "Hindari ajakan Plankton",
    "Pesan 12 krabby patty", 
    "Ganggu Squidward",
]

@app.route('/puja-kerang-ajaib', methods=['GET', 'POST'])
def kerang():
    if request.method == 'GET':
        nama = request.args.get('nama')
        if nama:
            pesan = f"{nama}, {random.choice(pesan_default)}"
        else:
            pesan = random.choice(pesan_default)

        return render_template('input.html', pesan=pesan)

@app.route('/puja',methods = ['GET', 'POST'] )
def puja() :
    if request.method == 'POST':
        nama_post = request.form.get('nama')
        print(f"DEBUG: Nama dari formulir :{nama_post}")
        if nama_post:
            pesan1 = f"Selamat datang, {nama_post}. Anda berhasil masuk ke Puja Kerang Ajaib"

        else:
            pesan1 = "Selamat datang. Anda berhasil masuk ke Puja Kerang Ajaib"
        pesan2 = f"{nama_post}, {random.choice(pesan_default)}"

        return render_template('hasil.html', nama=nama_post, pesan=pesan1 , pesan2 = pesan2)

if app.config.get('LOG_WITH_GUNICORN'):
    gunicorn_error_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers.extend(gunicorn_error_logger.handlers)
    app.logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    app.run(debug=True)

