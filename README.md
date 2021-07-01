# TD Secrets - dein kleiner Passwortmanager
by Asphilia

## Letzte Änderungen:
* 01.07.2021: TD Secrets wurde erstellt. Die GUI funktioniert. Man kann Einloggen, neue Passwörter hinzufügen, und verschlüsselte Passwörter entschlüsseln.

## Was soll noch kommen?
* TD Secrets soll eine Liste aller Bezeichnungen ausgeben können. Das sollte die Passwortsuche erleichtern.
* Das Ändern von Einträgen soll in die GUI hinzugefügt werden.
* Code Dokumentation!!!

## Was kann TD Secrets?
TD Secrets speichert dir deine Passwörter oder andere Nachrichten in einer Tabelle. Die Passwörter werden mit 2 bis 3 stelligen Zahlen verschlüsselt.

## Wie wird verschlüsselt?
In der Klasse TDSecret im Modul tdsecrets gibt es ein '''dict''', in welchem alle Möglichen Buchstaben, Zahlen und Sonderzeichen als Listen enthalten sind. Dieses Alphabet wird mit 4 verschiedenen Seeds gemischt. Dann können Buchstaben zu Zahlen und Zahlen zu Buchstaben umgewandelt werden.

## Wie benutze ich TD Secrets?
TD Secrets funktioniert ganz einfach: du rufst im Terminal '''python tdsecretgui.py''' auf, und eine kleine Benutzeroberfläche erscheint. Nun klickst du auf LogIn, um eine neue Tabelle zu erstellen, oder eine bestehende Tabelle zu öffnen. Du wirst nach vier Seeds gefragt, dies sind die Passwörter für die Verschlüsselung. Wenn die Seeds nicht stimmen, werden deine Passwörter nicht korrekt ent- und verschlüsselt. Am besten schaust du nach dem Einloggen, ob ein schon bestehendes Passwort richtig entschlüsselt wird, bevor du ein neues hinzufügst.

## Wie sicher ist TD Secrets?
Da es sich bei TD Secrets um meine eigene kleine Applikation handelt, und ich kaum Ahnung von Verschlüsselungen habe, ist TD Secrets wahrscheinlich nicht sehr sicher, aber ich weiß es nicht.