from subprocess import Popen, run
import sys


def run_api() -> None:
    Popen(['flask', 'run'], cwd='api')


def run_interface() -> None:
    run(['streamlit', 'run', 'app.py'], cwd='interface')


if __name__ == '__main__':
    try:
        run_api()
        run_interface()
    except KeyboardInterrupt:
        sys.exit(0)
