import sys
import hashlib

def calculate_hash(file_path, hash_algorithm="sha256"):
    """
    ファイルのハッシュ値を計算します。
    """
    hasher = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as f:
        # ファイルからデータを読み込んでハッシュを更新します
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def compare_hashes(file1_path, file2_path, hash_algorithm="sha256"):
    """
    2つのファイルのハッシュ値を比較します。
    """
    hash1 = calculate_hash(file1_path, hash_algorithm)
    hash2 = calculate_hash(file2_path, hash_algorithm)
    return hash1 == hash2

if __name__ == "__main__":
    # コマンドライン引数からファイルパスを取得します
    if len(sys.argv) != 3:
        print("Usage: python script.py <file1_path> <file2_path>")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    # ハッシュ値を比較します
    if compare_hashes(file1_path, file2_path):
        print("ファイルのハッシュ値は一致しています。")
    else:
        print("ファイルのハッシュ値は一致していません。")
