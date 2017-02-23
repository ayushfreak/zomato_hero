try:
    from urllib.request import Request, urlopen  # Python 3
    import json
except:
    from urllib2 import Request, urlopen  # Python 2



def city(city_name):
    q = Request('https://developers.zomato.com/api/v2.1/cities?q='+city_name)#or can write q=%s'%(city_name))
    #q.add_header("User-agent", "curl/7.43.0")
    #q.add_header("Accept","application/json")
    q.add_header('X-Zomato-API-Key', 'd6f866f6464607e8452cb8c8452704ac')
    a = urlopen(q).read().decode('UTF-8')
    data=json.loads(a)
    if(len(data['location_suggestions']) is not 0):
        return (data['location_suggestions'][0]['id'])
    else:
        return None

def cuisines(city_id):
    q = Request('https://developers.zomato.com/api/v2.1/cuisines?city_id='+str(city_id))
    #q.add_header("User-agent", "curl/7.43.0")
    #q.add_header("Accept","application/json")
    q.add_header('X-Zomato-API-Key', 'd6f866f6464607e8452cb8c8452704ac')
    a = urlopen(q).read().decode('UTF-8')
    dat=json.loads(a)
    data=dat['cuisines']
    return data


def result(cuisine_id,city_id):
    q = Request('https://developers.zomato.com/api/v2.1/search?entity_id='+str(city_id)+'&entity_type=city&count=10&cuisines='+str(cuisine_id))
    #q.add_header("User-agent", "curl/7.43.0")
    #q.add_header("Accept","application/json")
    q.add_header('X-Zomato-API-Key', 'd6f866f6464607e8452cb8c8452704ac')
    a = urlopen(q).read().decode('UTF-8')
    dat=json.loads(a)
    return(dat['restaurants'])
