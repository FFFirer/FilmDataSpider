# -*- coding:utf-8 -*-

import logging
import logging.handlers
# 格式化日志输出到文件中，限制日志文件个数和日期

logging.basicConfig()

# logger的初始化工作
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

# 写入文件，如果文件超过8Mb，仅保留10个文件
handler = logging.handlers.RotatingFileHandler('logs/Info.log', maxBytes=8000, backupCount=3)

# 格式化日志
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)-8s | %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
