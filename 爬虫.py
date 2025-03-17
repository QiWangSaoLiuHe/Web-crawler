import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import easygui
import webbrowser

easygui.msgbox("使用前请阅读使用说明！使用说明同此程序一起上传到了github","告知")
a = easygui.buttonbox("是否阅读完使用说明？","说实话",["我确定","我还没下载呢！"])
if a == "我确定":
    # 目标 URL
    url = easygui.enterbox("请输入想要爬取的网页","爬虫")
    if url == None:
        easygui.msgbox("爬虫程序已经关闭","程序关闭")
    else:
        # 发送 HTTP 请求
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
        except requests.exceptions.RequestException as e:
            easygui.msgbox(f"请求失败: {e}","爬取失败")
            exit()

        # 解析 HTML 内容
        soup = BeautifulSoup(response.text, "html.parser")

        # 获取网页标题
        title = soup.title.string if soup.title else "无标题"
        print(f"网页标题: {title}")

        # 获取所有链接
        links = soup.find_all("a", href=True)
        print(f"\n找到 {len(links)} 个链接:")

        for link in links:
            # 获取链接文本和 URL
            link_text = link.text.strip()
            link_url = urljoin(url, link["href"])  # 处理相对路径
            print(f"{link_text} -> {link_url}")
        easygui.msgbox("结果已在控制台显示！","爬取成功")
elif a == "我还没下载呢！":
    b = easygui.buttonbox("是否前往下载？","下载",["是","否"])
    if b == "是":
        url_download = "https://github.com/QiWangSaoLiuHe/Web-crawler/blob/1c4ff77144eec71fdd45508de506e52e2522fa3e/%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B.txt"
        webbrowser.open(url_download)