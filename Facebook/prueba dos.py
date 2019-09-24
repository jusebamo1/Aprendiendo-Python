import facebook
from Config import config as c


page_access_token = c.tokenLargo
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = c.idPagina
graph.put_object(facebook_page_id, "feed", message='test Python')

