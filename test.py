# test.py
import argparse

def main():  
    
    prsDiscription = '''
    TEPRAPY
    Printing TEPRA labels using the TEPRA app's API
    '''
    prsArgsDiscription = '''
    Ex: python teprapy.py 2
    '''
    parser = argparse.ArgumentParser(description = prsDiscription)
    parser.add_argument('description', help = prsArgsDiscription)
    parser.add_argument('-c', '--cpy', action = 'store_true', help = 'Number of copies')
    parser.add_argument('-a', '--app', action = 'store_true', help = 'TEPRA App path (spc10.exe)',)
    parser.add_argument('-l', '--lbl', action = 'store_true', help = 'TEPRA Label file path')
    parser.add_argument('-i', '--ipt', action = 'store_true', help = 'Import csv file path')

    args = parser.parse_args()

    print(str(args.cpy))
    print(args.app)

if __name__ == "__main__":
    main()
