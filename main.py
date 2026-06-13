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
        "🔴 실시간 경기",
        "⚽ 경기 일정",
        "📊 조별리그",
        "🌎 개최국",
        "🇰🇷 대한민국",
        "📚 역대 우승국"
    ]
)

# 홈
if menu == "🏠 홈":

    st.title("🏆 World Cup On")

    st.image(
        "https://img.sbs.co.kr/newimg/news/20230518/201785626_500.jpg",
        use_container_width=True
    )

    st.subheader("2026 FIFA 북중미 월드컵")

    col1, col2, col3 = st.columns(3)

    col1.metric("참가국", "48개국")
    col2.metric("경기 수", "104경기")
    col3.metric("개최국", "3개국")

# 실시간 경기
elif menu == "🔴 실시간 경기":

    st.title("🔴 실시간 축구 경기")

    url = "https://www.thesportsdb.com/api/v1/json/3/livescore.php?s=Soccer"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        matches = data.get("event")

        if matches:

            st.success(f"현재 {len(matches)}개의 경기가 진행 중입니다.")

            for match in matches:

                league = match.get("strLeague", "리그 정보 없음")

                home = match.get("strHomeTeam", "Unknown")
                away = match.get("strAwayTeam", "Unknown")

                home_score = match.get("intHomeScore", "-")
                away_score = match.get("intAwayScore", "-")

                status = match.get("strStatus", "LIVE")
                minute = match.get("strProgress", "")

                venue = match.get("strVenue", "경기장 정보 없음")
                attendance = match.get("intSpectators", "-")

                with st.container():

                    st.markdown(f"## 🏆 {league}")

                    st.markdown(
                        f"""
### ⚽ {home} {home_score} : {away_score} {away}

🔴 상태 : {status}

⏱ 진행시간 : {minute}

🏟 경기장 : {venue}

👥 관중 : {attendance}
"""
                    )

                    st.divider()

        else:
            st.warning("현재 진행 중인 경기가 없습니다.")

    except Exception as e:
        st.error(f"API 오류: {e}")
