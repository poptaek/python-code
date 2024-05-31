import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# 엑셀 파일에서 명함 정보를 읽어오는 함수
def read_from_excel(filename="business_cards.xlsx"):
    df = pd.read_excel(filename)
    cards = df.to_dict(orient='records')
    return cards

# 명함 정보를 엑셀로 저장하는 함수
def save_to_excel(cards, filename="business_cards.xlsx"):
    df = pd.DataFrame(cards)
    df.to_excel(filename, index=False)
    print(f"명함 정보가 '{filename}' 파일로 저장되었습니다.")

# 명함을 이미지로 생성하는 함수
def create_business_card_image(info, logo_path=None):
    card_width, card_height = 600, 350
    background_color = (255, 255, 255)
    font_color = (0, 0, 0)
    
    image = Image.new('RGB', (card_width, card_height), background_color)
    draw = ImageDraw.Draw(image)
    
    # 윈도우 기본 폰트 경로 설정
    font_path = "C:/Windows/Fonts/arial.ttf"
    font = ImageFont.truetype(font_path, 24)
    small_font = ImageFont.truetype(font_path, 18)
    
    draw.text((20, 50), f"Name: {info['Name']}", font=font, fill=font_color)
    draw.text((20, 100), f"Title: {info['Title']}", font=small_font, fill=font_color)
    draw.text((20, 150), f"Company: {info['Company']}", font=small_font, fill=font_color)
    draw.text((20, 200), f"Email: {info['Email']}", font=small_font, fill=font_color)
    draw.text((20, 250), f"Phone: {info['Phone']}", font=small_font, fill=font_color)
    
    # 로고 추가
    if logo_path:
        logo = Image.open(logo_path).convert("RGBA")  # 로고 이미지를 RGBA 형식으로 변환
        logo = logo.resize((100, 100))  # 로고 크기 조절
        image.paste(logo, (450, 20), logo)  # 투명도 유지하며 이미지에 로고 추가
    
    filename = f"{info['Name'].replace(' ', '_')}_business_card.png"
    image.save(filename)
    print(f"명함 이미지가 '{filename}' 파일로 저장되었습니다.")

# 엑셀 파일에서 명함 정보를 읽어옴
cards = read_from_excel("business_cards.xlsx")

# 명함 정보를 엑셀로 저장 (필요 시 사용)
# save_to_excel(cards)

# 예시 명함 하나를 이미지로 생성
if cards:
    for card in cards:
        create_business_card_image(card, logo_path="logo.png")  # 로고 파일 경로 지정
else:
    print("엑셀 파일에 명함 정보가 없습니다.")
