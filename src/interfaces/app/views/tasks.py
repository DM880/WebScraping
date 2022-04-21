import pandas as pd
from openpyxl import Workbook


def data_download(datas):

    datas.to_excel("url_scraped.xlsx", sheet_name="url_scraped")