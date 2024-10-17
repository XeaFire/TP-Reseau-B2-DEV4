import socket
import sys
import argparse
import re
import utils
import utils.checkping
host = '5.5.5.11'  # IP du serveur
port = 13337       # Port choisir par le serveur


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", action="store" help="Choose wich port you want open")
parser.add_argument("-l", "--listen", action="store", help="Choose wich IP you want listen")

args = parser.parse_args()

ip_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

if int(args.port) < 0 or int(args.port) > 65535:
    print(f"ERROR -p argument invalide. Le port spécifié {args.port} n'est pas un port valide (de 0 à 65535).")
    sys.exit(1)
elif int(args.port) < 1024:
    print(f"ERROR -p argument invalide. Le port spécifié {args.port} est un port privilégié. Spécifiez un port au dessus de 1024.")
    sys.exit(2)
elif not re.match(ip_regex, args.listen):
    print(f"ERROR -l argument invalide. L'adresse {args.listen} n'est pas une adresse IP valide.")
    sys.exit(3)
elif not utils.checkping.check_ping(args.listen):
    print(f"ERROR -l argument invalide. L'adresse {args.listen} n'est pas l'une des adresses IP de cette machine.")

else:
    port = int(args.port)



# On définit la destination de la connexion


# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))  

# Place le programme en mode écoute derrière le port auquel il s'est bind
s.listen(1)
# On définit l'action à faire quand quelqu'un se connecte : on accepte
conn, addr = s.accept()
# Dès que quelqu'un se connecte, on affiche un message qui contient son adresse
print(f"Un client vient de se co et son IP c'est {addr}.") 
# Petite boucle infinie (bah oui c'est un serveur)
# A chaque itération la boucle reçoit des données et les traite
while True:

    try:
        # On reçoit 1024 bytes de données
        data = conn.recv(1024)
        
        # Si on a rien reçu, on continue
        if not data: break

        if "meo" in str(data):
            print("Meo à toi confrère.")
        elif "waf" in str(data):
            print("ptdr t ki")
        else:
            print("Mes respects humble humain.")
        conn.sendall(b'Hi mate !')

    except socket.error:
        print("Error Occured.")
        break

# On ferme proprement la connexion TCP
conn.close()

sys.exit(0)


