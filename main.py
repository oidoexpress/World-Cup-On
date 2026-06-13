import streamlit as st
import pandas as pd
import requests
st.set_page_config(
    page_title="World Cup On",
    page_icon="🏆",
    layout="wide"
)
menu = st.sidebar.radio(
    "메뉴",
    [
        "🏠 홈",
        "🇰🇷 대한민국 대표팀",
        "👥 선수단",
        "⚽ 경기 일정",
        "📊 FIFA 랭킹",
        "🏆 월드컵 역사",
        "🔴 실시간 축구"
    ]
)

# 홈
if menu == "🏠 홈":

    st.title("🇰🇷 Korea World Cup On")

    st.image(
        "https://img.sbs.co.kr/newimg/news/20230518/201785626_500.jpg",
        use_container_width=True
    )

    st.subheader("2026 FIFA 북중미 월드컵 대한민국 응원 플랫폼")

    col1, col2, col3 = st.columns(3)

    col1.metric("최고 성적", "4강")
    col2.metric("월드컵 진출", "11회 연속")
    col3.metric("FIFA 랭킹", "23위")

# 대한민국 대표팀
elif menu == "🇰🇷 대한민국 대표팀":

    st.title("🇰🇷 대한민국 축구 국가대표")

    st.write("""
감독 : 홍명보

별명 : 태극전사

협회 : 대한축구협회(KFA)

최고 성적 : 2002 FIFA 월드컵 4강
""")

    st.image(
        "https://wimg.sedaily.com/news/legacy/2023/03/03/29MVTGNQTB_1.jpg",
        width=200
    )

# 선수단
elif menu == "👥 선수단":

    players = pd.DataFrame({
        "선수": [
            "손흥민",
            "이강인",
            "김민재",
            "황희찬",
            "조현우",
            "설영우"
        ],
        "포지션": [
            "FW",
            "MF",
            "DF",
            "FW",
            "GK",
            "DF"
        ],
        "소속팀": [
            "토트넘",
            "PSG",
            "바이에른 뮌헨",
            "울버햄튼",
            "울산 HD",
            "츠르베나 즈베즈다"
        ]
    })

    st.dataframe(players, use_container_width=True)

# FIFA 랭킹
elif menu == "📊 FIFA 랭킹":

    ranking = pd.DataFrame({
        "순위": [1, 2, 3, 4, 5],
        "국가": [
            "아르헨티나",
            "프랑스",
            "스페인",
            "잉글랜드",
            "브라질"
        ]
    })

    st.dataframe(ranking, use_container_width=True)

# 월드컵 역사
elif menu == "🏆 월드컵 역사":

    st.title("🏆 대한민국 월드컵 역사")

    history = pd.DataFrame({
        "연도": [2002, 2010, 2022],
        "성적": ["4강", "16강", "16강"]
    })

    st.dataframe(history, use_container_width=True)

# 실시간 축구
elif menu == "🔴 실시간 축구":

    st.title("🔴 대한민국 관련 실시간 경기")

    url = "https://www.thesportsdb.com/api/v1/json/3/livescore.php?s=Soccer"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        matches = data.get("event")

        if matches:

            korea_match_found = False

            for match in matches:

                home = match.get("strHomeTeam", "")
                away = match.get("strAwayTeam", "")

                if "Korea" in home or "Korea" in away:

                    korea_match_found = True

                    home_score = match.get("intHomeScore", "-")
                    away_score = match.get("intAwayScore", "-")
                    league = match.get("strLeague", "")
                    status = match.get("strStatus", "LIVE")

                    st.success(
                        f"""
🏆 {league}

⚽ {home} {home_score} : {away_score} {away}

🔴 상태 : {status}
"""
                    )

            if not korea_match_found:
                st.warning("현재 대한민국 관련 실시간 경기가 없습니다.")

        else:
            st.warning("현재 진행 중인 경기가 없습니다.")

    except Exception as e:
        st.error(f"API 오류: {e}")
