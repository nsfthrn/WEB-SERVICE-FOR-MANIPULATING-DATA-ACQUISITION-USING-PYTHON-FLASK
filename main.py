# import modul dari flask dan pandas
from flask import Flask, request, jsonify
import pandas as pd

# import fungsi yang digunakan di dalam file ini 
from load_data import load_data
from get_all_data import get_all_data
from get_column import get_column
from get_top_five import get_top_five
from sorting import sorting
from convert_json import convert_json
from delete_column import delete_column
from delete_all_data import delete_all_data
from insert_data import insert_data
from get_info import get_info
from get_row import get_row
from get_row_field import get_row_field
from update_data import update_data
from delete_data import delete_data
from get_row_json import get_row_json
from get_all_data_json import get_all_data_json
from jumlah_data import jumlah_data

app = Flask(__name__)

# deklarasi nama file csv
# sumber pengambilan data csv
# untuk dataframe kita dapat membaca sebuah file dan menjadikannya table 
# dataframe mendefinisikan fungsi load_data ( MEMBACA FILE CSV DARI PANDAS ) kemudian mengembalikan parameter filename yang isinya SUMBER FILE CSV
# dataframe.index kurang lebih 1 maksudnya ialah, filenya akan lebih dari 1.
filename = 'Book1.csv'
dataframe = load_data(filename)
dataframe.index += 1


# mengupdate data ketika ada perubahan
# didalam fungsi reload_data didefinisikan 2 parameter (fname dan dframe)
# parameter dframenya difungsikan kedalam file csv dimana parameter fname, dan dframe diganti dengan index=false dan separationnya : 
# kemudian variabel/fungsi dataframe didefinisikan dengan fungsi load_data ( membaca csv dengan parameter fname)
def reload_data(fname, dframe):
    global dataframe
    dframe.to_csv(fname, index=False, sep=':')
    dataframe = load_data(fname)



# endpoint localhost:5000/dataset
# istilah endpoint adalah pemanggilan URL API
# args adalah argument
# Fugsinya dengan nama dataset
# Metode yang digunakan ialah GET, POST DAN DELETE 
@app.route('/dataset', methods=['GET', 'POST', 'DELETE'])
def dataset():
    args = request.args
    response = dataframe
    # apabila diadakan pemanggilan terhadap request.methodnya GET maka akan dieksekusi perintah dibawah
    if request.method == 'GET':
        # Fungsi len() berfungsi untuk mengembalikan panjang (jumlah anggota) dari suatu objek.
        # maksud dari Len(args) yaitu mengembalikan panjang dari parameter arguments
        if not len(args) is 0: 
            # pemanggilan parameter field kemudian direspon dengan hasil dari fungsi get_cloumn
            # fungsi get_column itu untuk mengambil data dari column tertentu
            if 'field' in args:
                response = get_column(response, args['field'])
            # pemanggilan parameter toptive kemudian direspon dengan hasil dari fungsi get_top_five
            # fungsi topfive itu untuk mengambil 5 data urutan pertama atau terakhir
            if 'topfive' in args:
                response = get_top_five(response, args['topfive'])
            # pemanggilan parameter sort kemudian direspon dengan hasil dari fungsi sorting
            # fungsi topfive itu untuk mengurutkan data dari atas ke bawah atau sebaliknya
            # yang bisa dieksekusi itu ASCENDING ( awal ke akhir / kecil ke besar ) DAN DESCENDING ( sebaliknya )
            if 'sort' in args:
                response = sorting(response, args['sort'])
            # pemanggilan parameter format kemudian direspon dengan hasil dari fungsi jsonify(get_all_data_json)
            # fungsi get_all_data_json adalah untuk mengambil semua data dari csv dan mengubah ke format json
            # namun bisa juga diubah menjadi format RAW
            if 'format' in args:
                if args['format'] == 'json':
                    response = jsonify(get_all_data_json(response))
            else:
                response = str(response)
        else:
            response = str(response)
        return response

    # kemudian request selanjutnya apabila menggunakan method POST
    elif request.method == 'POST':
        # argumentnya didefinisikan dengan request untuk fungsi get_json
        argsp = request.get_json()
        # datanya didefinisikan dengan 3 argument yaitu raw_value, data dan sign
        data = [argsp['raw_value'], argsp['data'], argsp['sign']]
        # menerapkan fungsi insert data 
        # fungsi insert data untuk menambahkan data
        # dalam fungsi insert_data diterapkan juga fungsi get_row_count yang akan dieksekusi juga
        insert_data(response, data)
        # dijalankan juga fungsi untuk menampilkan semua data apabila telah ditambahkan
        reload_data(filename, response)
        # apabila fungsi insert berhasil dilakukan, maka akan muncil respon berupa " created "
        return 'created',201
    # kemudian request selanjutnya apabila menggunakan method DELETE
    elif request.method == 'DELETE':
        if not len(args) is 0:
            # pemanggilan parameter field kemudian direspon dengan hasil dari fungsi get_cloumn
            # fungsi get_column itu untuk mengambil data dari column tertentu
            if 'field' in args:
                # fungsi yang akan dieksekusi pada variabel response ialah delete_column apabila dibarengi dengan parameter field
                # pada fungsi delete column ditujukan untuk menghapus column tertentu
                response = delete_column(response, args['field'])
        else:
            # dan apabila fungsi dieksekusi dengan Method DELETE tanpa dibarengi dengan parameter FIELD maka yang akan dihapus adalah semuanya
            # untuk fungsi get_all_data itu ditujukan untuk menghapus semua data yang dituju ( semua data di CSV )
            response = delete_all_data(response)
        # kemudian setelah mendapatkan respon tersebut maka fungsi reload_data akan berfungsi lagi yaitu memperbarui data csv ( menamppilkan 
        # perubahan data )
        reload_data(filename, response)
        return str(response)

# endpoint localhost:5000/jumlah
# istilah endpoint adalah pemanggilan URL API
# args adalah argument
# Fugsinya dengan nama jumlah
# Metode yang digunakan ialah GET
@app.route('/dataset/jumlah', methods=['GET'])
def jumlah():
    args = request.args
    res = None
    if not len(args) is 0:
        # apabila parameter from difungsikan maka akan terjadi pengeksekusian fungsi jumlah_data 
        if 'from' in args:
            # pada fungsi umlah_data diberikan 2 pilihan . bisa menampilkan jumlah untuk ROW ataupun COLUMN
            res = jumlah_data(dataframe, args['from'])
    else:
        # nah untuk pemanggilan row dan column itu apabila tidak dipanggil dengan parameternya " field " maka akan muncul ALL
        res = jumlah_data(dataframe, 'all')
    return str(res)

# endpoint localhost:5000/dataset/id id berupa angka
# istilah endpoint adalah pemanggilan URL API
# args adalah argument
# Fugsinya dengan nama detail
# Metode yang digunakan ialah GET, POST DAN DELETE
@app.route('/dataset/<int:id>', methods=['GET', 'POST', 'DELETE'])
def detail(id):
    args = request.args
    # fungsi yang digunakan ialah get_row 
    # fungsi get row ialah untuk mengambil semua data dari index id
    # kemudian akan dimunculkan seluruh datanya beserta dengan id tersebut
    detailframe = get_row(get_all_data(dataframe), id)
    # menampilkan fungsi dengan metode GET
    if request.method == 'GET':
        if not len(args) is 0:
            # pemanggilan parameter field kemudian direspon dengan hasil dari fungsi get_row_field
            # fungsi get_row_field itu untuk mengambil satu data dari column tertentu
            # tentunya dibarengi dengan parameter field
            if 'field' in args:
                #detailframe didefinisikan dengan fungsi get_row_field 
                # fungsi get_row_field untuk mengambil satu data dari column tertentu
                detailframe = get_row_field(detailframe, args['field'])
            if 'format' in args:
                # jika argument di definisikan dengan format 
                # kemudian tuliskan parameter yang ingin dieksekusi dari field ke json, maka hasilnya akan berbentuk json
                if args['format'] == 'json' and 'field' not in args:
                    # fungsi yang dieksekusi ialah jsnofy(get_roe_json) dimana untuk merubah data ke format json
                    detailframe = jsonify(get_row_json(detailframe))
                else:
                    return jsonify(detailframe)
            else:
                detailframe = str(detailframe)
        else:
            detailframe = str(detailframe)
        return detailframe

    # kemudian request selanjutnya apabila menggunakan method POST
    elif request.method == 'POST':
        argsp = request.get_json()
        # data yang ditampilkan dan dieksekusi ialah dari argument raw_value, data dan sign
        data = [argsp['raw_value'], argsp['data'], argsp['sign']]
        # diantara dari argument diatas, apabila dilakukan perubahan maka akan difungsikan fungsi update_data
        # fungsi update_data yaitu untuk mengupdate data dari index id kemudian nanti akan ada fungsi get_all_data lagi
        # akan difungsikan untuk mengambil semua data csv dari id 
        updated = update_data(get_all_data(dataframe), id, data)
        # menampilkan perubahan data setelah diubah
        reload_data(filename, updated)
        # apabila data berhasil diubah maka akan muncul tulisan / return dari "updated"
        return 'updated',201
    # kemudian request selanjutnya apabila menggunakan method DELETE
    elif request.method == 'DELETE':
        # untuk variabel delete difungsikan fungsi delete_data
        # fungsi delete_data untuk menghapus satu data dari index id
        # nanti akan ada fungsi get_all_data lagi, akan difungsikan untuk mengambil semua data csv dari id
        deleted = delete_data(get_all_data(dataframe), id)
        # menampilkan perubahan data setelah diubah
        reload_data(filename, deleted)
        # apabila penghapusan data berhasil maka akan muncul return dari " deleted "
        return 'deleted',201

# endpoint localhost:5000/info
# istilah endpoint adalah pemanggilan URL API
# args adalah argument
# Fugsinya dengan nama info
# Metode yang digunakan ialah GET
@app.route('/info', methods=['GET'])
def info():
    # fungsi get_info yaotu untuk mengambil info dari data csv (fitur bawaan dari library pandas)
    # kemudian akan difungsikan lagi get_all_data untuk menampilkan data csv
    return str(get_info(get_all_data(dataframe)))

if __name__ == "__main__":
    app.run(debug=True)