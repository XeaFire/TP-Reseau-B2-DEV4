import socket
import sys

# On définit la destination de la connexion
host = '5.5.5.11'  # IP du serveur
port = 13337               # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur

try :
    s.connect((host, port))
except socket.error as msg:
    print(f"Erreur de connexion avec le serveur :")
    sys.exit(1)

# note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()

# Envoi de data bidon
s.sendall(b'Meowwwww')



# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)
if not data :
    sys.exit(1)
# On libère le socket TCP
s.close()

# Affichage de la réponse reçue du serveur
print(data)

sys.exit(0)


