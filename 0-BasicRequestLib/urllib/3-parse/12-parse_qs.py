from urllib.parse import parse_qs

"""
GET 请求参数 通过 parse_qs() 它转回字典，
"""
query = 'name=mtianyan&age=21'
print(parse_qs(query))
