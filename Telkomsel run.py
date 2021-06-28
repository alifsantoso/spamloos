# Dibuat Oleh alif
# Mau ngapain tod? Kode ulang? Alat spam ajh di recode. Tinggal di pakek apa susahnya :v
# =,=

impor os, waktu, json, acak, string

r = "\033[1;91m"
g = "\033[1;32m"
w = "\033[1;97m"
y = "\033[1;93m"
d = "\x1b[41;37;1m"
cl = "\x1b[0;0m"


mencoba:
  dari permintaan impor *
  dari bs4 impor BeautifulSoup sebagai bs
kecuali:
  print(f"{w}[{g}•{w}] Instal Modul...")
  os.system("permintaan pemasangan pip")
  os.system("pip install bs4")
  

def telkomsel(nomor):
  xnxx = {"username":nomor,"action":"","iswebview":"true","fromaccount":"false"}
  kz = bs(post("https://nsp.telkomsel.com/account/process/processlupapassword", data=xnxx).text, 'html.parser').find('div', {'content container-fluid bg-3 kecil'}).findAll('div')[2]['class'][1]
  if kz == "peringatan-peringatan":
    pis = string.ascii_huruf kecil
    coz = random.randint(6,20)
    mail = ''.join(random.choice(pis) untuk p dalam range(coz))
    echa = {"iswebview":"false","email":"{mail}{airpatira}@gmail.com","nohp":nomor,"namapengguna":{airpatira},"password":"kontol.com123 "}
    rakz = post("https://nsp.telkomsel.com/account/process/processdaftar", data=echa).text
    print(f"{w}[{g}{i+1}{w}] {g}Daftar{w} - Spam Berhasil Dikirim!")
    
  lain:
    print(f"{w}[{g}{i+1}{w}] {g}Lupakan{w} - Spam Berhasil Dikirim!")



sementara Benar:
  os.system("hapus")
  airpatira = random.randint(10000.9999)
  cetak(f"""{r}╔═╗{w}┏━┓┏━┓┏┓┏┓┏┓┏┓┏━┏━┓
{r}╚═╗{w}┣━┛┣━┫┃┗┛┃┃┗┛┃┣━┣┳┛
{r}╚═╝{w}┻
{d} Dikodekan Oleh alif {cl}""")
  nomor = input(f"\n{w}[{g}•{w}] Nomor Target : ")
  jumlah = input(f"{w}[{g}•{w}] Jumlah : ")
  mencetak("")
  untuk i dalam rentang(int(jumlah)):
  	telkomsel(nomor)
  
  waktu.tidur(2)
  tanya = input(f"\n{w}[{g}?{w}] Ingin Coba Lagi y/n? ")
  jika tanya == "y" atau tanya == "Y":
    terus
  
  elif tanya == "n" or tanya == "N":
    istirahat
  
  lain:
    print(f"\n{w}[{r}!{w}] Buta Ya Tod? ")
    waktu.tidur(2.5)
    terus