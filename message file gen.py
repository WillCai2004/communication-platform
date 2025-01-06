from torrentool.api import Torrent

#创建内容文件
file_name = "message.txt"
content = "这是需要通过 BitTorrent 传输的文本内容。"

#将文本写入文件
with open(file_name, "w", encoding="utf-8") as f:
    f.write(content)

print(f"内容已保存为文件: {file_name}")

#创建文件
torrent = Torrent.create_from(file_name)

#添加Tracker
torrent.announce_urls = ['udp://tracker.openbittorrent.com:80']

#保存文件
torrent_file = "message.torrent"
torrent.to_file(torrent_file)

print(f"Torrent 文件已生成: {torrent_file}")

#打印种子信息
print(f"种子信息:\n{torrent}")
