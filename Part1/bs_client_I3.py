import socket
import sys

# On définit la destination de la connexion
host = '5.5.5.11'  # IP du serveur
port = 13337               # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur



while True:
    clientmessage =input("Que veux-tu envoyer au serveur : ")
    if type(clientmessage) is not str:
        print("Votre réponse n'est pas valide")
    else:
        break

if "meo" not in clientmessage or "waf" not in clientmessage:
    raise TypeError("Il n'y a pas meo ou waf dans la phrase sad :/")


try :
    s.connect((host, port))
except socket.error as msg:
    print(f"Erreur de connexion avec le serveur : {msg}")
    sys.exit(1)



# note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()

print(f"Connecté avec succès au serveur {host} sur le port {port}")
# Envoi de data bidon
s.sendall(clientmessage.encode(encoding="utf-8"))



# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)
if not data :
    sys.exit(1)
# On libère le socket TCP
s.close()

# Affichage de la réponse reçue du serveur
print(data)

sys.exit(0)


