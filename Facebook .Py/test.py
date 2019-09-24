import facebook

def main():
    cfg = {
    "page_id": "103293627741324",
    "access_token": "EAAHEmqaETGcBANZCxyNYPCp2mOkeWMUYHmVEKhAQX1ODsNWedgsvhb7kG7yjNfTjNv1kmJaGUveDfvoxTVZAQdlEJB22ZCpPUHtnjHm8lqDdlintI4jPuHTolYJaPEWMuhZBOnIqSLKbJ4ilT9KTLOosvkOlv2cLiEHSQmLzJgH6TpnYB4SA6XZC48xjiJNtgMpncu48PbwZDZD"
    }
api = get_api(cfg)
msg = "Welcome to a TestPagePy"
status = api.put_wall_post(msg)

def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    resp= graph.get_objext('me/accounts')
    page_acces_token= None
    for page in resp['data']:
        if page['id']== cfg['page_id']:
            page_acces_token=page['acces_token']
            graph=facebook.GraphAPI(page_acces_token)
        return graph

if __name__=="_main_":
    main()

