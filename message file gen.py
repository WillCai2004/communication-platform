from torrentool.api import Torrent

def create_placeholder_file(file_name, file_size):
    """创建一个占位文件，指定大小。"""
    with open(file_name, "wb") as f:
        f.write(b"\x00" * file_size)
    print(f"占位文件已创建: {file_name}")

def create_torrent(file_name, torrent_name, trackers):
    """为指定文件创建 .torrent 文件。"""
    torrent = Torrent.create_from(file_name)
    torrent.announce_urls = trackers
    torrent.to_file(torrent_name)
    print(f"种子文件已创建: {torrent_name}")

def write_message_to_block(file_name, message, block_index, block_size=16 * 1024):
    """将消息写入占位文件的指定块中。"""
    offset = block_index * block_size  # 计算块的偏移量

    if len(message) > block_size:
        raise ValueError("消息长度超过块大小！")

    with open(file_name, "r+b") as f:
        f.seek(offset)  # 移动到块的起始位置
        f.write(message.encode("utf-8").ljust(block_size, b"\x00"))  # 写入消息并填充空字节

    print(f"消息已写入块 {block_index}: {message}")

def read_message_from_block(file_name, block_index, block_size=16 * 1024):
    """从占位文件的指定块中读取消息。"""
    offset = block_index * block_size  # 计算块的偏移量

    with open(file_name, "rb") as f:
        f.seek(offset)  # 移动到块的起始位置
        block_data = f.read(block_size)  # 读取块数据

    message = block_data.rstrip(b"\x00").decode("utf-8")  # 去除填充的空字节并解码
    return message

if __name__ == "__main__":
    # 第一步：创建一个占位文件
    placeholder_file = "chat_placeholder.dat"  # 占位文件名
    file_size = 100 * 1024 * 1024  # 文件大小为 100MB
    create_placeholder_file(placeholder_file, file_size)

    # 第二步：创建种子文件
    torrent_file = "chat.torrent"  # 种子文件名
    trackers = ['udp://tracker.openbittorrent.com:80']  # 使用的 Tracker
    create_torrent(placeholder_file, torrent_file, trackers)

    # 第三步：将消息写入一个块
    message = "Hello, this is a test message!"  # 要写入的消息
    block_index = 0  # 写入的块索引
    write_message_to_block(placeholder_file, message, block_index)

    # 第四步：从块中读取消息
    retrieved_message = read_message_from_block(placeholder_file, block_index)  # 读取块中的消息
    print(f"读取到的消息: {retrieved_message}")
