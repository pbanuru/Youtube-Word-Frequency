from youtube_transcript_api import YouTubeTranscriptApi
from collections import Counter


def run():
    '''Recieves Input, Makes API Call, and Outputs Results'''
    video_link = input('Enter the video link: ')

    if video_link.startswith('https://www.youtube.com/watch?v='):

        n_most_common = input('I want the to see the n most common words: ')
        video_id = video_link.split('=')[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        counter = parse(transcript)
        print("------------------------------------------------")
        output(counter, int(n_most_common))

    else:
        # Using ansi escape codes to output color. https://www.youtube.com/watch?v=W0mlGkew6K4
        print(
            'Invalid link, must be in format \033[31mhttps://www.youtube.com/watch?v=\033[0m\033[95mvideo_id\033[0m')


def parse(transcript: list[dict['text': str, 'start': float, 'end': float]]):
    '''Parse into a counter object, counting the frequency of each word'''
    counter = Counter()
    for dictionary in transcript:
        word_list = dictionary['text'].split()

        # Remove Punctuation from each word, to avoid "infrastructure" and "infrastructure," from being counted as seperate words
        word_list = [word.strip(',.?!') for word in word_list]
        counter.update(word_list)

    return counter


def output(counter: Counter, n_most_common: int):
    '''
    Descending output in format:
    1. | the | 288
    2. | to  | 255
    3. | of  | 198
    4. | is  | 161
    '''
    most_common_n = counter.most_common(n_most_common)
    longest_word_length = max(len(word) for word, _ in most_common_n)

    num_len = len(str(n_most_common))
    for i, (word, frequency) in enumerate(most_common_n):
        print("{num:<{num_len}} | {word:^{padding}} | {frequency:>2}".format(
            num=str(i+1)+'.', word=word, frequency=frequency, padding=longest_word_length, num_len=num_len))
