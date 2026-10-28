def count_text(file_path: str):
    """
    统计文本文件字符数、单词数
    :param file_path: 文本文件路径
    :return: dict，包含统计结果或者错误信息
    """
    if not isinstance(file_path, str):
        return {"error": "invalid path type"}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        char_count = len(content)
        word_list = content.split()
        word_count = len(word_list)
        return {
            "char_count": char_count,
            "word_count": word_count
        }
    except FileNotFoundError:
        return {"error": "file not found"}


if __name__ == "__main__":
    result = count_text("demo.txt")
    print("text stats result:", result)
