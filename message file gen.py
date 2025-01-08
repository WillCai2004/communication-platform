from torrentool.api import Torrent

def create_placeholder_file(file_name, file_size):
    """Create a placeholder file with the specified size."""
    with open(file_name, "wb") as f:
        f.write(b"\x00" * file_size)
    print(f"Placeholder file created: {file_name}")

def create_torrent(file_name, torrent_name, trackers):
    """Create a .torrent file for the given file."""
    torrent = Torrent.create_from(file_name)
    torrent.announce_urls = trackers
    torrent.to_file(torrent_name)
    print(f"Torrent file created: {torrent_name}")

def write_message_to_block(file_name, message, block_index, block_size=16 * 1024):
    """Write a message to a specific block in the placeholder file."""
    offset = block_index * block_size

    if len(message) > block_size:
        raise ValueError("Message length exceeds block size!")

    with open(file_name, "r+b") as f:
        f.seek(offset)
        f.write(message.encode("utf-8").ljust(block_size, b"\x00"))

    print(f"Message written to block {block_index}: {message}")

def read_message_from_block(file_name, block_index, block_size=16 * 1024):
    """Read a message from a specific block in the placeholder file."""
    offset = block_index * block_size

    with open(file_name, "rb") as f:
        f.seek(offset)
        block_data = f.read(block_size)

    message = block_data.rstrip(b"\x00").decode("utf-8")
    return message

if __name__ == "__main__":
    # Step 1: Create a placeholder file
    placeholder_file = "chat_placeholder.dat"
    file_size = 100 * 1024 * 1024  # 100MB
    create_placeholder_file(placeholder_file, file_size)

    # Step 2: Create a torrent file
    torrent_file = "chat.torrent"
    trackers = ['udp://tracker.openbittorrent.com:80']
    create_torrent(placeholder_file, torrent_file, trackers)

    # Step 3: Write a message to a block
    message = "Hello, this is a test message!"
    block_index = 0
    write_message_to_block(placeholder_file, message, block_index)

    # Step 4: Read the message from the block
    retrieved_message = read_message_from_block(placeholder_file, block_index)
    print(f"Retrieved message: {retrieved_message}")
