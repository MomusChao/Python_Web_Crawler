def implement(zz):
    import requests
    import pandas as pd 
    import pickle
    from dateutil.parser import parse
    
    # token on FB Graph API Exploer
    token = '' 

    # fanpages_id & fanpages_id_name
    fanpages = {'fanpages_id':'fanpages_id_name''} 
    information_list = []

    for fanpage_id in fanpages:
        res = requests.get('https://graph.facebook.com/v2.12/{}/posts?limit=100&access_token={}'.format(fanpage_id, token))
        pages = 1 

        while True: 
            print('Crawler {}: page{}'.format(fanpages[fanpage_id], pages))
            for information in res.json()['data']:
                if 'message' in information:
                    information_list.append([fanpages[fanpage_id], information['message'],information['id'],information['created_time'], parse(information['created_time']).date()])
                    
            if 'next' in res.json()['paging']:
                res = requests.get(res.json()['paging']['next'])
                pages += 1
            else:
                print('{} {} Done! \n'.format(fanpage_id, fanpages[fanpage_id]))
                break
    with open('Thepretty_FB_post_info_v2.pickle', 'wb') as handle:
        pickle.dump(information_list, handle)
    
    return information_list