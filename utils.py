"""
Parse Arguments for bearer token, custom model-url, pre-defined model-url options
"""

import argparse

def parseArgs():
	argParser = argparse.ArgumentParser()
	argParser.add_argument('--compare', action=argparse.BooleanOptionalAction)
	argParser.add_argument("-qd", "--querydoc", help="Query from document (txt)")
	argParser.add_argument("-q",'--query', help="Raw string query")
	argParser.add_argument("-a",'--auth', help="Authorization Bearer Token")
	argParser.add_argument("-m", '--model', help="Model URL\nMust be provided as: 'profile_name/model_name'\nExample: 'stabilityai/stable-diffusion-2-1''")
	argParser.add_argument("-ex", "--export", help="Export URL if needed.")
	args = argParser.parse_args()
	return args