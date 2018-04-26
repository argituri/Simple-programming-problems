# encoding: utf-8
# Challenge: Given two strings, write a program that efficiently finds the longest common subsequence.
# Haaste: Kahden merkkijonon pisin yhteinen 'alimerkkijono' esim. sanoille "esimerkki" & "välimerkki" olisi "imerkki"


# Tulosta mallintava luokka jolla on attribuutit merkkijono ja sen pituus.
# Class that represents the result (longest substring) with two attributes: a string and the length

class tulos:
	def __init__(self,merkkijono,pituus):
		self.merkkijono = merkkijono
		self.pituus = pituus

# Metodi joka tulostaa objektin (käytännössä luokan tulos instanssin) merkkijonon ja pituuden. Tämän pitäisi varmaan olla luokassa tulos
# Method that prints out the attributes merkkijono and pituus of object objekti.

def tulostaMerkkijono(objekti):
	print "Longest subsequence: " + objekti.merkkijono
	print "Length of the subsequence: " + str(objekti.pituus)


# Vertaillaan merkkijonojen a,b kirjaimia. Löytyy samat --> katsotaan minkä pituinen 'alimerkkijono' siitä kohtaa lähtee.
# Mikäli suurempi kuin aiemmin löydetty, tallennetaan pituus ja alimerkkijono

# Takes two strings (a,b) and compares them letter by letter. When matching letters are found,

def samatKirjaimet(a, b):
	pituus = 0
	alimerkkijono = ""
	alimAlku = 0
	i = 0
	for i in range (len(a)):
		j = 0
		for j in range (len(b)):
			if (a[i] == b[j]):
				aliYrite = samatSanat(a[i:len(a)],b[j:j+len(a)])
				j += aliYrite.pituus  # Skip the letters in the substring so they are not checked many times unnecessarily
				if pituus<aliYrite.pituus:
					pituus = aliYrite.pituus
					vastaus = aliYrite


	return vastaus



# Otetaan merkkijonot c ja d ja katsotaan kuinka monta samaa kirjainta niissä on. 
# Samojen kirjainten lukumäärä = pituus
# Palauttaa tulos -objektin

# Takes two strings (c, d) and counts how long the matching sequence is. 
# Pituus = length of the similar substring =# of same consecutive letters
# This method returns an instance of the class tulos.

def samatSanat(c,d):
	pituus = 0
	try:
		while c[pituus] == d[pituus]:
			pituus += 1
	except IndexError:
			return tulos(c[0:pituus], pituus)
	return tulos(c[0:pituus], pituus)


# Määritellään testimerkkijonot str1, str2
# Define two strings (str1, str2) for testing

str1 = "esimerkki on hyvä olla"
str2 = "välimerkki on hyvä merkki"

print "Strings: " + "\n" + str1 + "\n" + str2 + "\n"
print(tulostaMerkkijono(samatKirjaimet(str1, str2)))