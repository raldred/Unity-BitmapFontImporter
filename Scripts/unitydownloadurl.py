#!/bin/python
# coding=utf-8


from optparse import OptionParser
import urllib
import re

def getUrls():
    f = urllib.urlopen("https://unity3d.com/get-unity/download/archive")
    # f = urllib.urlopen("https://google.com")
    data = f.read()
    # <a href="http://download.unity3d.com/download_unity/0b02744d4013/MacEditorInstaller/Unity-5.0.2f1.pkg">Unity Editor</a>
    urls = re.findall(r'<a href="(https?://.*?MacEditorInstaller/Unity-(5\..*?)\.(pkg|exe))">Unity Editor</a>', data)
    return urls

def filterUrls(urls, os, version):
    if len(urls) == 0 :
        return urls

    # if os == "mac":
    #     os = "osx"

    if version is None:
        return urls

    if version == "last":
        return [urls[0]]

    newurls =filter(lambda item:item[1].startswith(version), urls)
    return newurls

# l = len(urls)
# for i in xrange(1,l):
#     if urls[i][1].startswith("5"):
#         print urls[i][0]
#         break
#     # print urls[i][1] + "@" + urls[i][0]


# -------------- main --------------
if __name__ == '__main__':
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option(
        '-v', '--version', dest='version',
        help='filter unity version, last 5 5.3 5.3.5')
    parser.add_option(
        '-o', '--os', dest='os',
        help='filter unity os, win or osx or mac')
    (opts, args) = parser.parse_args()

    urls = getUrls()
    urls = filterUrls(urls, opts.os, opts.version)
    if len(urls) > 0:
        print urls[0][0]
