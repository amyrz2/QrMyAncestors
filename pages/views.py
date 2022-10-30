# Create your views here.

from django.http import HttpResponse

def indexPageView(request) :
    sOutput = '<html>'\
                '<head><title>Home</title></head>'\
                '<body>'\
                    '<p style="font-size:50px; background-color:#779ecb; text-align:center; color:white;">Welcome to QRMyAncestors (pun intended)!</p>'\
                    '<p style="background-color:#779ecb; color:white; text-align:center; font-size:25px;">'\
                        '<b>The brand new way to share the stories of those you love and admire</b></p>'\
                    '<ul style = "color:white; font-size:20px; background-color:#779ecb;">'\
                        '<li>Joy</li>'\
                        '<li>Happiness</li>'\
                        '<li>Love</li>'\
                    '</ul>'\
                '</body>'\
            '</html>'
    return HttpResponse(sOutput)   

def aboutPageView(request) :
    sOutput = '<html><head><title>About</title></head><body><p style="font-size:50px; color:white; background-color:#779ecb; text-align:center;">About QRMyAncestors:</p><p style="font-size:30px; color:white; background-color:#779ecb; text-align:center;">Started in 2022, QRMyAncestors is beginning to revolutionize the way we share stories and remember those who have passed away. Stay connected with us :)</p></body><ul style="font-size:20px; color:white; background-color:#779ecb;"><li>email: QRMyAncestors@QRMyAncestors.com</li><li>instagram: QRMyAncestors</li><li>LinkedIn: QRMyAncestors</li></ul></body></html>'
    return HttpResponse(sOutput)

def profilePageView(request, person_name) :
    sOutput = '<html><head><title>Contact</title></head><body><p style="font-size:50px; color:white; background-color:#779ecb; text-align:center;">About ' + person_name + '\'s story</p></body></html>'
    return HttpResponse(sOutput)
