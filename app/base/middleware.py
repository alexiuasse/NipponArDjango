#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/07/2020 08:59.

# base/middleware.py
import threading

local = threading.local()

class BaseMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        local.user = request.user
        response = self.get_response(request)
        return response
