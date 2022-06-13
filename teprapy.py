# tepraPy

import os, sys
from dotenv import load_dotenv


def msg(msg, msgType = ''):

    if msgType == 'c': print('*** {}'.format(msg))      # クリティカル
    elif msgType == 'w': print('<!> {}'.format(msg))    # 警告
    elif msgType == 'q': print('<?> {}'.format(msg))    # 質問
    elif msgType == 'a': return input('{} -> '.format(msg))     # 入力
    else: print(msg)
    

def print(spcPath, lblPath, csvPath, numCopy):

    def check(spcPath, lblPath, csvPath, numCopy):
        
        # ソフトウェアの存在確認
        if os.path.exists(spcPath) == False:
            msg('ソフトウェア(SPC10.exe)が存在しません。', 'c')
            return False
        
        # ラベルファイルの存在確認
        if os.path.exists(lblPath) == False:
            msg('ラベルファイルが存在しません。', 'c')
            return False

        # CSVファイルの存在確認
        if os.path.exists(csvPath) == False:
            msg('CSVファイルが存在しません。', 'c')
            return False

        # 部数の確認
        if type(numCopy) != int:
            msg('印刷部数の指定が不正です。', 'c')
            return False

        return True


    if not check(spcPath, lblPath, csvPath, numCopy):
        msg('印刷処理を中止します。', 'w')
        return False
    
    cmd = 'cmd /C ("{}" /pt "{}, {}, {}")'.format(spcPath, lblPath, csvPath, numCopy)
    try:
        os.system(cmd)
    except:
        msg('印刷コマンドの実行に失敗しました。\n{}'.format(cmd), 'c')
        return False

    return True


def main():  

    load_dotenv()
    spcPath = os.environ['TPRPY_SPCPATH']
    lblPath = os.environ['TPRPY_LBLPATH']
    csvPath = os.environ['TPRPY_CSVPATH']
    numCopy = 1 

    if not print(spcPath, lblPath, csvPath, numCopy): return False
 
    return True

if __name__ == "__main__":
    main()
