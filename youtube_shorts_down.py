from pytube import YouTube

def download_youtube_shorts(url, save_path='.'):
    try:
        # 유튜브 객체 생성
        yt = YouTube(url)
        
        # 스트림 선택 (최고 화질의 비디오 스트림)
        stream = yt.streams.filter(file_extension='mp4', only_video=True).order_by('resolution').desc().first()

        # 비디오 다운로드
        if stream:
            print(f'Downloading: {yt.title}')
            stream.download(output_path=save_path)
            print(f'Download complete: {save_path}/{yt.title}.mp4')
        else:
            print('No suitable stream found.')

    except Exception as e:
        print(f'An error occurred: {e}')

# 사용 예시
url = 'https://youtube.com/shorts/bCaL74mgRcY?si=-xxFQKkqgpIdh8HY'
download_youtube_shorts(url)
