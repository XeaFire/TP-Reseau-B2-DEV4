import socket
import sys
import utils.logs

# On définit la destination de la connexion
host = '5.5.5.11'  # IP du serveur
port = 13337               # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur



try :
    s.connect((host, port))
except socket.error as msg:
    utils.logs.log("Impossible de se connecter au serveur <IP_SERVER> sur le port <PORT>.", "ERROR", True, "/var/log/bs_client/bs_client.log")
    
    sys.exit(1)

# note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()
utils.logs.log(f"Connecté avec succès au serveur {host} sur le port {port}", "INFO", False, "/var/log/bs_client/bs_client.log")
clientmessage =input("Que veux-tu envoyer au serveur : ")
# Envoi de data bidon
s.sendall(clientmessage.encode(encoding="utf-8"))
utils.logs.log(f"Message envoyé au serveur {host} : {clientmessage}.", "INFO", False, "/var/log/bs_client/bs_client.log")


# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)
if not data :
    sys.exit(1)
utils.logs.log(f"Réponse reçue du serveur {host} : {data}", "INFO", False, "/var/log/bs_client/bs_client.log")
# On libère le socket TCP
s.close()

# Affichage de la réponse reçue du serveur
print(int.from_bytes(data, byteorder='big'))

sys.exit(0)


