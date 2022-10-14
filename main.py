from datetime import datetime as dt, timedelta as delta
import requests
import time
import os

m3u8_url = 'http://s6.playep.pro/vod/films/the.flash.2014.s08e15.720p.web.h264gossip_377851/hls/index.m3u8'
param = '-loglevel quiet'

parse = {
    'video_codecs': ['h264_qsv', 'h264'],
    'params2': ['-hwaccel dxva2', '-threads 4']
}
manifest = {
    1: {
        'name': 'The_Flash_s08ep15_h264_qsv_multithreading.mp4',
        'video_codec': 'h264',
        'params': '-threads 4'
    }
}


def main():
    timings = []
    print(f"{dt.now().strftime('%d-%m-%Y %H:%M:%S')} [INFO]: starting download!")
    start_time = dt.now().timestamp()
    for num, data in manifest.items():
        start_part_time = dt.now().timestamp()
        if data['video_codec'] == 'h264_qsv':
            command = f'ffmpeg {param} {data["params"]} -c:v {data["video_codec"]} -i {m3u8_url}' \
                      f' -c:a aac "{data["name"]}"'
        else:
            command = f'ffmpeg {param} {data["params"]} -i {m3u8_url} -c:v {data["video_codec"]}' \
                      f' -c:a aac "{data["name"]}"'
        os.system(command)
        end_part_time = dt.now().timestamp()
        duration_part = f'{int((end_part_time - start_part_time) // 60)}:{int((end_part_time - start_part_time) % 60)}'
        timings.append(f'{data["name"]} --- {duration_part}')
    end_time = dt.now().timestamp()
    duration_sec = end_time - start_time
    duration = f'{int(duration_sec // 60)}min {int(duration_sec % 60)}sec'
    print(f"{dt.now().strftime('%d-%m-%Y %H:%M:%S')} [INFO]: Done!")
    print(f'{dt.now().strftime("%d-%m-%Y %H:%M:%S")} [INFO]: Duration: {duration}')

    print('#' * 20)
    print('\n'.join(timings))
    print('#' * 20)


if __name__ == '__main__':
    main()
