import sys

def compare_binary_files(file1_path, file2_path):
    try:
        with open(file1_path, 'rb') as file1:
            with open(file2_path, 'rb') as file2:
                # ファイルのバイナリデータを読み込む
                data1 = file1.read()
                data2 = file2.read()

                # バイナリデータの比較
                if data1 == data2:
                    print("ファイルは同じです。")
                else:
                    print("ファイルは異なります。")
    except FileNotFoundError:
        print("指定されたファイルが見つかりませんでした。")

if __name__ == "__main__":
    # 引数が正しく指定されているか確認
    if len(sys.argv) != 3:
        print("Usage: python compare_files.py file1 file2")
        sys.exit(1)

    file1_path = sys.argv[1]  # 比較するファイル1のパス
    file2_path = sys.argv[2]  # 比較するファイル2のパス

    compare_binary_files(file1_path, file2_path)
