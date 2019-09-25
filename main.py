# -*- coding:utf-8 -*-

# 导入包
import LogCenter
import MySpider

# 主程序
def main():
    first_url=r'https://www.1905.com/mdb/film/list/enindex-A/'
    root_url=r'https://www.1905.com'
    MySpider.InitBaseConfig(root_url)
    MySpider.GetFilmsOnPage(first_url)

    LogCenter.logger.info('ALL DONE')

# 执行程序
if __name__ == "__main__":
    main()