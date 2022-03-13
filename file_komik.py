class Komik(object):
  def __init__(self, judul, author, genre, viewers):
    self.judul = nama
    self.author = author
    self.genre = genre
    self.viewers = viewers

  def bacaan(self, durasi):
    for x in range(durasi):
      print("Ayo baca komik!")

  def info(self):
    print(f"judul: {self.judul}, author: {self.author}, genre: {self.genre}, viewers: {self.viewers}")


class Manhwa(Komik):
  def __init__(self, judul, author, genre, viewers, studio, kota):
    super().__init__(judul, author, genre, viewers)
    self.studio = studio
    self.kota = kota
  
  def asal(self):
    print("Komik ini berasal dari Korea")
          
  def info_manhwa(self):
    print(f"judul: {self.judul}, author: {self.author}, genre: {self.genre}, viewers: {self.viewers}, studio:{self.studio}, kota: {self.kota}")

class Manga(Komik):
  def __init__(self, judul, author, genre, viewers, berwarna):
    super().__init__(judul, author, genre, viewers)
    self.berwarna = berwarna
  
  def volume(self, jumlah):
    if jumlah >=2 :
      print("manga sangat populer")
    else:
      print("tidak populer")