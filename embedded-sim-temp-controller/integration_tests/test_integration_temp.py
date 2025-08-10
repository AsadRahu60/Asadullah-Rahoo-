import subprocess
import pytest
from pathlib import Path

FIRMWARE_DIR = Path(__file__).resolve().parents[1] / "firmware"

def start_device():
    program = FIRMWARE_DIR / ".pio" / "build" / "native" / "program"
    assert program.exists(), "Build first: `cd firmware && pio run -e native`"
    proc = subprocess.Popen(
        [str(program)],
        cwd=str(FIRMWARE_DIR),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    # wait for READY
    line = proc.stdout.readline().strip()
    assert line == "READY"
    return proc

def send_cmd(proc, cmd):
    proc.stdin.write(cmd + "\n")
    proc.stdin.flush()
    return proc.stdout.readline().strip()

@pytest.mark.parametrize("temp,expected_mode", [
    (10.0, "HEATING"),
    (21.0, "IDLE"),
    (30.0, "COOLING"),
])
def test_device_modes(temp, expected_mode):
    proc = start_device()
    line = send_cmd(proc, f"READ {temp}")
    assert f"MODE {expected_mode}" in line
    status = send_cmd(proc, "STATUS")
    assert expected_mode in status
    send_cmd(proc, "EXIT")
    proc.terminate()
