import os

def get_env():
	return os.get_env('ENV', 'development')