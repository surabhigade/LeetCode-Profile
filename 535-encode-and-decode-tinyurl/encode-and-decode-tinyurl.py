class Codec:
    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        self.base = "http://tinyurl.com/"
        self.counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.url2code:
            return self.base + self.url2code[longUrl]
        else:
            # create a unique code
            code = str(self.counter)
            self.url2code[longUrl] = code
            self.code2url[code] = longUrl
            self.counter += 1
            return self.base + code
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        
        :type shortUrl: str
        :rtype: str
        """
        # get the code part
        code = shortUrl.replace(self.base, "")
        return self.code2url.get(code, "")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))