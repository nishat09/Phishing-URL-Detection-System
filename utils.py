import re
from urllib.parse import urlparse

def extract_features(url):
    # Remove the protocol (http, https, ftp)
    url = re.sub(r"https?://", "", url)
    
    # Extract URL components
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname or ""
    path = parsed_url.path or ""
    
    features = {
        "url_length": len(url),
        "num_dots": hostname.count("."),
        "num_digits": sum(c.isdigit() for c in url),
        "num_special_chars": sum(c in ["@", "-", "_", "/", "?", "=", "&"] for c in url),
        "is_https": url.startswith("https"),
        "path_length": len(path),
        "num_subdomains": hostname.count("."),
        "has_ip_address": bool(re.match(r"(\d{1,3}\.){3}\d{1,3}", hostname))
    }
    
    return features

# Test it
if __name__ == "__main__":
    url = "https://example.com/login.php?user=admin&pass=1234"
    print(extract_features(url))
