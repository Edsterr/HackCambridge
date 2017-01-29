from urllib.parse import urlparse
from urllib.request import urlopen
import lxml.html as LH


def categorizeWebsite(url):
    domain = urlparse(url).netloc
    categorization = urlopen("https://archive.lightspeedsystems.com/SubmitDomain.php?Domain=" + domain).read()
    root = LH.fromstring(categorization)
    for el in root.iter('span'):
        if 'onclick' in el.attrib and el.attrib['onclick'] == 'toggle()':
            return el.text


print(categorizeWebsite("http://www.gov.uk/some/fucking/apth/here.php"))


# http://community.lightspeedsystems.com/documentation/web-filter/administration-2/content-database/database-categories/
# Website categories listed at the URL above



