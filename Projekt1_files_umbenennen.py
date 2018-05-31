# GeekGirlsCarrots Zürich: Informatiktage 2018
# Programmieren Lernen mit Python Kurs
#
#
# Programm, um mehrere Fotos gleichzeitig zu umbennenen. 
#
#
import os

# wechselt in den  Arbeitsverzeichnis, in dem wir arbeiten wollen. 
# Das ist für jeder anders!!
os.chdir('/home/username/photo_datei')


# initialisiere den Zähler. 
i = 1

# durchlaufe die Datei
for f in os.listdir():

	# splitext(): trennt die Dateierweiterung. Ich bekomme ein tuple mit 2 Elementen, und 
	# speichere die unter file_name (der Dateiname) und unter file_ext (die Dateierweiterung).
	file_name, file_ext = os.path.splitext(f)
		
	# ich nehme mir die Dateiname vor. Die Dateierweiterung interessiert mich jetzt nicht.
	# ich teile der Name in zwei Teilen: den Titel (file_titel), und die Zahl (file_num)
	# zur Erinnerung: die Dateinamen haben folgendes Format: IMG_8743
	file_titel, file_num = file_name.split('_')		
		
	# ersetze der alte Name (IMG) mit den neuen (in diesem Fall "Zürich in Mai")
	file_titel_neu = file_titel.replace('IMG', 'Zürich in Mai')
	
	# 
	file_num_neu = str(i)
	
	# gibt den neuen name aus. Format ist: zahl-fileName.dateierweiterung		
	new_name = '{}-{}{}'.format(file_num_neu,file_titel_neu,file_ext)

	# umbenenne und überschreibe die alten Dateinamen
	os.rename(f,new_name)
	i = i + 1
	# kürzer: i+=1
	