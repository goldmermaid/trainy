import os
import ray
import subprocess
import threading
import time
from click.testing import CliRunner
from udjat import connect_ray
from udjat.cli import trace
from udjat.httpd import start_server

def test_client():
    server_thread = threading.Thread(target=start_server)
    server_thread.setDaemon(True)
    server_thread.start()

    runner = CliRunner()
    result = runner.invoke(trace, [])
    assert result.exit_code == 0