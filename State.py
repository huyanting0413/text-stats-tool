def count_text(file_path):
    """统计文本文件字符数、单词数"""
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
    res = count_text("demo.txt")
    print(res)
