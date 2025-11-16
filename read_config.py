# coding=utf-8
import os
import yaml
from set_log import logger
import traceback
yaml.warnings({'YAMLLoadWarning': False})

# 读取config.yaml文件
def read_config_yaml() :
    try:
        logger.info('读取config.yaml - Start')
        with open('./config.yaml', mode = 'r', encoding = 'utf-8') as f :
            resp = yaml.safe_load(f)
            # print(resp)
        logger.info('读取config.yaml - success')
        return resp
    except Exception as e :
        logger.error('读取config.yaml - Failed')
        logger.error(f"{e}")
    finally:
        logger.info('读取config.yaml - End')

# if __name__ == '__main__':
#     res = read_config_yaml()
#     print(res)
