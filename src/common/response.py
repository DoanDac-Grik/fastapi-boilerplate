from typing import Union

class ResponseData:
    def __init__(self, data: Union[dict, list]):
        self.data = data

class PaginationResponseData(ResponseData):
    def __init__(self, data: Union[dict, list], limit: int, page: int, total_pages: int):
        self.data = data
        self.limit = limit
        self.page = page
        self.total_pages = total_pages
