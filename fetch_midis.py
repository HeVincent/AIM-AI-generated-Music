from musdl import OnlineScore
import sys
import os


def fetch_midis(listfile):
    path = os.getenv('path_to_folder')
    with open(listfile) as f:
        uns = f.read().splitlines()
    f.close()
    urls = [un.split(', ')[0] for un in uns]
    names = [un.split(', ')[1] for un in uns]
    for i in range(len(urls)):
        midi = f'{path}{names[i]}.mid'
        print(f"Processing file {names[i]}...")
        score = OnlineScore(urls[i])
        score.export('mid', midi)
        print("Done!")
        i += 1


if __name__ == '__main__':
    try:
        fetch_midis(sys.argv[1])

    except IndexError:
        print('Usage: fetch_midis.py <path to txt file>\n')
        print('Formatting in text file:\n<url1>, <name1>\n<url2>, <name2>...\n')
        print('Example: fetch_midis.py "D:\\list.txt"\n\nlist.txt:\n'
              'https://musescore.com/user/101036/scores/5928621, Les Toreadors - Bizet\n'
              'https://musescore.com/user/24069/scores/2437586, Pastoral 5th movement - Beethoven\n')
        print(f"Error: Specify the text file to parse info from.")
    except FileNotFoundError:
        print('Text file doesn\'t exist.')
