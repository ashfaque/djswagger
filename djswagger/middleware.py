
# ! - 6
from django.conf import settings
from django.http import HttpResponseForbidden

forbidden_html = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>403 Forbidden</title>
    <style>
        @import url("https://fonts.googleapis.com/css?family=Press+Start+2P");

        html,
        body {
            width: 100%;
            height: 100%;
            margin: 0;
        }

        * {
            font-family: 'Press Start 2P', cursive;
            box-sizing: border-box;
        }

        #app {
            padding: 1rem;
            background: black;
            display: flex;
            height: 100%;
            justify-content: center;
            align-items: center;
            color: #54FE55;
            text-shadow: 0px 0px 10px;
            font-size: 6rem;
            flex-direction: column;
        }

        #app .txt {
            font-size: 1.8rem;
        }

        @keyframes blink {
            0% {
                opacity: 0;
            }

            49% {
                opacity: 0;
            }

            50% {
                opacity: 1;
            }

            100% {
                opacity: 1;
            }
        }

        .blink {
            animation-name: blink;
            animation-duration: 1s;
            animation-iteration-count: infinite;
        }
    </style>
</head>

<body>
    <div id="app">
        <div>403</div>
        <div class="txt"> Forbidden<span class="blink">_</span> </div>
    </div>
</body>

</html>'''

class RestrictSwaggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not settings.DEBUG and 'swagger' in request.path_info:
            return HttpResponseForbidden(forbidden_html)
            # return HttpResponseForbidden('Swagger UI is not available on production.')
        return self.get_response(request)
