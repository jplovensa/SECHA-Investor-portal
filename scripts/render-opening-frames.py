"""Render the original, deterministic SECHA+ interface motion study offline."""
import argparse
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from playwright.sync_api import sync_playwright
parser=argparse.ArgumentParser()
parser.add_argument('--output',required=True)
args=parser.parse_args()
output=Path(args.output);output.mkdir(parents=True,exist_ok=True)
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(Path(__file__).resolve().parent.parent)))
Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':960,'height':540},device_scale_factor=1)
    page.goto(f'http://127.0.0.1:{server.server_port}/scripts/opening-scene.html')
    page.evaluate('document.fonts.ready')
    for frame in range(216):
        page.evaluate('(t)=>window.render(t)',frame/24)
        page.locator('canvas').screenshot(path=str(output/f'{frame:04d}.png'))
    browser.close()
server.shutdown()
print('Rendered 216 original interface frames')
