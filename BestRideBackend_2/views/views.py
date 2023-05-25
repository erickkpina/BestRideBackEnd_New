import requests, uuid, json
from rest_framework.reverse import reverse
from rest_framework.response import Response
from environs import Env
from django.http import JsonResponse
from rest_framework.decorators import api_view

env = Env()
env.read_env()

import os

"""class Images:
    @api_view(['POST'])
    def upload_file(request):
        
        #file_name: File to upload
        #bucket: Bucket to upload to
        #object_name: S3 object name. If not specified then file_name is used
        #return: True if file was uploaded, else False
        

        # If S3 object_name was not specified, use file_name
        object_name = os.path.basename(request.data['file_name'])

        # Upload the file
        #s3_client = boto3.client('s3')

        try:
            response = s3_client.upload_file(request.data['file_name'], "bestridebucket", object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True"""



class Translator():

    @api_view(['POST'])
    def translate(request):
        subscription_key = 'd282af8ef2784b829c28173a468cc593'
        endpoint = 'https://api.cognitive.microsofttranslator.com/'

        location = 'westeurope'

        constructed_url = endpoint + '/translate'

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-Type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }


        text = request.data['text']
        source_lang = request.data['sourceLang']
        target_lang = request.data['outputLang']

        params = {
            'api-version': '3.0',
            'to': target_lang,
            'from': source_lang
        }

        data = [{
            'text': text
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=data)
        response = request.json()

        response_data = {
            'translated_text': response[0]['translations'][0]['text']
        }

        return Response(response_data)

@api_view(['GET'])
def api_root(request, format=None):
    """
    API for Best Ride App
    """
    return Response({
        'Users': reverse('users', request=request, format=format),
    })
