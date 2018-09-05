import base64

def base64_url_encode(input_bytes):
	base64_url_bytes = base64.urlsafe_b64encode(input_bytes)
	return base64_url_bytes.decode().rstrip('=')

def base64_url_decode(string):
	padding = 4 - (len(string) % 4)
	string = string + ('=' * padding)
	return base64.urlsafe_b64decode(string)
