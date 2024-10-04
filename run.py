from subprocess import Popen, run


def run_api() -> None:
    Popen(['flask', 'run'], cwd='api')


def run_interface() -> None:
    run(['streamlit', 'run', 'app.py'], cwd='interface')


if __name__ == '__main__':
    run_api()
    run_interface()
