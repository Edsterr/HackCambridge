"""from urllib.parse import urlparse
from urllib.request import urlopen
import lxml.html as LH


def categorizeWebsite(url):
    domain = urlparse(url).netloc
    categorization = urlopen("https://archive.lightspeedsystems.com/SubmitDomain.php?Domain=" + domain).read()
    root = LH.fromstring(categorization)
    for el in root.iter('span'):
        if 'onclick' in el.attrib and el.attrib['onclick'] == 'toggle()':
            return el.text
"""
def approx_compare(str_a, str_b):
    return "".join(str_a.split()).lower() in "".join(str_b.split()).lower()



def is_productive(title):
    whitelist = ["stackoverflow", "google", "github", "superuser", "python","reddit","django","java","html","js","javascript","linux","server","css","flask","git","database","intellij","pycharm","idea","urxvt","xterm","vim","emacs","nano","~","ngrok","py","class","sh","api"]
    for x in whitelist:
        if approx_compare(x, title):
            return True
    return False
             
        



# http://community.lightspeedsystems.com/documentation/web-filter/administration-2/content-database/database-categories/
# Website categories listed at the URL above



