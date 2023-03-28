import tracker
import read


if __name__ == "__main__":
    tracker.start(read.read_file_whole("src/env/token"))