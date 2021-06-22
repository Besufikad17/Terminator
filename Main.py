import os
from pyfiglet import Figlet
from halo import Halo


figlet = Figlet(font='larry3d')


def scan(path):
    ab = []
    for roots, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('Unhide Files') and file.endswith('.bat'):
                ab.append(os.path.join(roots, file))
        for dir in dirs:
            dirname = dir
            for r, d, f in os.walk(os.path.join(roots,dir)):
                for file in f:
                    if file.startswith(dirname) and file.endswith('.exe'):
                        tempdir = os.path.join(dir,file)
                        ab.append(os.path.join(roots,tempdir))
    return ab


def delete(ab):
    for path in ab:
        try:
            os.remove(path)
        except FileNotFoundError:
            return 'woops file not found'


def main():
    print(figlet.renderText('Terminator'))
    dir = input('Enter directory or drive: ')
    spinner = Halo(text='Scanning', spinner='dots')
    spinner.start()
    scanresult = scan(dir)
    spinner.stop()
    print('scan result: ')
    for dir in scanresult:
        print(dir)
    print(str(len(scanresult)) + ' unwanted files found')
    choice = input('Do u wanna remove those :')
    if choice == 'yes' or choice == 'yea' or choice == 'hell ya':
        delete(scanresult)
    print('Done :)')


if __name__ == '__main__':
    main()

