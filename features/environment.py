
from utilities.readfromglobalconf import readfromglobalconf
from utilities.resources import APIResources

#run before each feature - hook implimentation
def before_feature(context, feature):
    if 'Login' in feature.name:
        context.baseurl = readfromglobalconf('API', 'url')
        context.endpoint = APIResources.login
        context.full_url = context.baseurl + context.endpoint