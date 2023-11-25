from django.shortcuts import render

class Errorhandler:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code != 200:
            return render(request, "index.html", status= response.status_code)
        return response
