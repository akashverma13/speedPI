#pip install speedtest-cli
import speedtest
#Codice necessario per il display LCD
import time
from RPLCD import CharLCD
import socket
import fcntl
import struct

#Funzione che mi ritorna l'indirizzo Ip
def ipAddress(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

#Funzione che esegue il speedtest
def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def main():
    lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
    #Scrivo ad un file CSV
    with open('file.csv', 'w') as f:
        f.write('download,upload,ping\n')
        for i in range(3):
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            f.write('{},{},{}\n'.format(d, u, p))
    #Formattazione del file CSV
    with open('file.txt', 'w') as f:
        for i in range(3):
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            f.write('Test #{}\n'.format(i+1))
            f.write('Download: {:.2f} Kb/s\n'.format(d / 1024))
            f.write('Upload: {:.2f} Kb/s\n'.format(u / 1024))
            f.write('Ping: {}\n'.format(p))
            lcd.write_string(u"Test della velocità in corso...")
            time.sleep(1)
            lcd.clear()
            time.sleep(1)

    #Stampo indirizzo ip sullo schermo
    lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
    lcd.write_string("IP address e velocità:")
    #Sposto il cursore
    lcd.cursor_pos = (1, 0)
    lcd.write_string(ipAddress('eth0'))

    #Stampo sulla console i risultati
    for i in range(3):
        d, u, p = test()
        print('Test #{}\n'.format(i+1))
        print('Download: {:.2f} Kb/s\n'.format(d / 1024))
        print('Upload: {:.2f} Kb/s\n'.format(u / 1024))
        print('Ping: {}\n'.format(p))
        media_download = media_download + d / 1024
        media_upload = media_upload + u / 1024
        media_ping = media_ping + p

    #Stampo download sullo schermo LCD
    lcd.cursor_pos = (2, 0)
    lcd.write_string('Download: {:.2f} Kb/s\n'.format(media_download / 3))
    #Stampo upload sullo schermo LCD
    lcd.cursor_pos = (3, 0)
    lcd.write_string('Upload: {:.2f} Kb/s\n'.format(media_upload / 3))
    #Stampo ping sullo schermo LCD
    lcd.cursor_pos = (4, 0)
    lcd.write_string('Ping: {}\n'.format(media_ping / 3))



if __name__ == '__main__':
    main()
