from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from bs4.element import Comment
from bs4 import BeautifulSoup
import validators
import requests

class ScrapperAPIView(APIView):
    

    def tag_visible(self, element):
        """
        Method to filter just visible text
        """
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def get(self, request, format=None):
        """
        Return an object with page info
        """
        url = self.request.query_params.get("url")
        if not url:
            return Response("url must be provide in url query parameters",status=status.HTTP_400_BAD_REQUEST)
        url = url if url.startswith('http') else ('http://' + url)
        if not validators.url(url):
            return Response("Invalid URL", status=status.HTTP_400_BAD_REQUEST)
        page = requests.get(url)
        content = BeautifulSoup(page.text, 'html.parser')
        result = {
            "title": None,
            "description": None,
            "image":None,
            "url":None,
            "texts":None,
            "links":[]
        }
        for tag in content.find_all("meta"):
            if tag.get("property") == "og:title":
                result["title"] = tag.get("content", None) # Added title if it doesn't has content show None
            if tag.get("property") == "og:description":
                result["description"] = tag.get("content", None) # Added description if it doesn't has content show None
            if tag.get("property") == "og:image":
                result["image"] = tag.get("content", None) # Added image if it doesn't has content show None
            if tag.get("property") == "og:url":
                result["url"] = tag.get("content", None) # Added url if it doesn't has content show None
        texts = content.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)  
        result["texts"] = u" ".join(t.strip() for t in visible_texts) #Join all found text
        for link in content.find_all('a', href=True):
            if validators.url(link.get("href")):
                result["links"].append(link.get("href"))

        result["links"] = list(dict.fromkeys(result["links"])) # Remove duplicates

        return Response(result, status=status.HTTP_200_OK)


