import base64


def zip_to_base64_txt(zip_path, txt_path):
    """将zip文件编码成base64格式并写入txt文件"""
    with open(zip_path, 'rb') as f_zip:
        zip_bytes = f_zip.read()
        b64_string = base64.b64encode(zip_bytes).decode('utf-8')
    with open(txt_path, 'w', encoding='utf-8') as f_txt:
        f_txt.write(b64_string)
    print(f"成功将 {zip_path} 编码为 Base64 并保存到 {txt_path}")


def base64_txt_to_zip(txt_path, zip_path):
    """将base64 txt文件解码还原为zip文件"""
    with open(txt_path, 'r', encoding='utf-8') as f_txt:
        b64_string = f_txt.read()
        zip_bytes = base64.b64decode(b64_string)
    with open(zip_path, 'wb') as f_zip:
        f_zip.write(zip_bytes)
    print(f"成功将 {txt_path} 解码还原为 {zip_path}")


if __name__ == "__main__":

    zip_to_base64_txt("edgedriver_win64.zip", "edgedriver_win64-win64.txt")
    #test
    # base64_txt_to_zip("PixPin_2.0.0.3.zip.txt", "restored.zip")
