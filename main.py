import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="World Cup On",
    page_icon="🏆",
    layout="wide"
)

# -------------------
# 사이드바 메뉴
# -------------------

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
# -------------------
# 홈
# -------------------
elif menu == "🔴 실시간 경기":

    st.title("🔴 실시간 축구 경기")

    import requests

    url = "https://www.thesportsdb.com/api/v1/json/3/livescore.php?s=Soccer"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        matches = data.get("event")

        if matches:

            for match in matches[:20]:

                home = match.get("strHomeTeam", "Unknown")
                away = match.get("strAwayTeam", "Unknown")

                home_score = match.get("intHomeScore", "-")
                away_score = match.get("intAwayScore", "-")

                league = match.get("strLeague", "")

                st.info(
                    f"{league}\n\n⚽ {home} {home_score} : {away_score} {away}"
                )

        else:
            st.warning("현재 진행 중인 경기가 없습니다.")

    except Exception as e:
        st.error(f"API 오류: {e}")

# -------------------
# 경기 일정
# -------------------

elif menu == "⚽ 경기 일정":

    st.title("⚽ 주요 경기 일정")

    schedule = pd.DataFrame({
        "날짜": [
            "2026-06-11",
            "2026-06-12",
            "2026-06-13",
            "2026-06-14"
        ],
        "경기": [
            "개막전",
            "조별리그",
            "조별리그",
            "조별리그"
        ]
    })

    st.dataframe(
        schedule,
        use_container_width=True
    )

# -------------------
# 조별리그
# -------------------

elif menu == "📊 조별리그":

    st.title("📊 조별리그")

    group_a = pd.DataFrame({
        "국가": [
            "대한민국",
            "멕시코",
            "남아공",
            "체코"
        ]
    })

    st.subheader("Group A")

    st.dataframe(
        group_a,
        use_container_width=True
    )

# -------------------
# 개최국
# -------------------

elif menu == "🌎 개최국":

    st.title("🌎 개최국 소개")

    st.subheader("🇺🇸 미국")
    st.write("주요 개최 도시 다수")

    st.subheader("🇨🇦 캐나다")
    st.write("토론토, 밴쿠버")

    st.subheader("🇲🇽 멕시코")
    st.write("멕시코시티, 과달라하라")

# -------------------
# 대한민국
# -------------------

elif menu == "🇰🇷 대한민국":

    st.title("🇰🇷 대한민국 국가대표")

    st.subheader("주요 선수")

    players = pd.DataFrame({
        "선수": [
            "손흥민",
            "이강인",
            "김민재",
            "황희찬"
        ],
        "포지션": [
            "FW",
            "MF",
            "DF",
            "FW"
        ]
    })

    st.dataframe(
        players,
        use_container_width=True
    )

# -------------------
# 역대 우승국
# -------------------

elif menu == "📚 역대 우승국":

    st.title("📚 역대 월드컵 우승국")

    winners = pd.DataFrame({
        "연도": [
            2010,
            2014,
            2018,
            2022
        ],
        "우승국": [
            "스페인",
            "독일",
            "프랑스",
            "아르헨티나"
        ]
    })

    st.dataframe(
        winners,
        use_container_width=True
    )

# -------------------
# 푸터
# -------------------

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center;color:gray'>
    <b>World Cup On</b><br>
    2026 FIFA 북중미 월드컵 정보 플랫폼<br><br>
    © 2026 World Cup On. All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True
)
