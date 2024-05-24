from pytube import YouTube

def download_audio(video_url, output_path):
    try:
        # YouTube 객체 생성
        yt = YouTube(video_url)
        
        # 오디오 스트림 필터링
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # 다운로드
        audio_stream.download(output_path)
        
        print("음원 추출이 완료되었습니다.")
    except Exception as e:
        print("오류 발생:", str(e))

# 유튜브 비디오 URL
video_url = "https://youtu.be/F_k9tmvNp20?si=uJPkDXPTu6AiB54z"

# 음원을 저장할 경로
output_path = "추출된_음원.mp3"

# 함수 호출
download_audio(video_url, output_path)
