#! /usr/bin/env python
import argparse
import asyncio

from httpapi import WebApp
from cli import CLI


parser = argparse.ArgumentParser(description='Pocket OCR')
parser.add_argument('--http', dest='api', type=bool)
parser.add_argument('--file', dest='local_file', type=str)

args = parser.parse_args()

if args.api:
    WebApp().run_app()
elif args.local_file:
    asyncio.run(CLI().print_local_file(args.local_file))
