import streamlit as st
import pandas as pd

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

if menu == "🏠 홈":

    st.image(
        "https://img.sbs.co.kr/newimg/news/20230518/201785626_500.jpg",
        use_container_width=True
    )

    st.title("🏆 World Cup On")

    st.subheader("2026 FIFA 북중미 월드컵")

    col1, col2, col3 = st.columns(3)

    col1.metric("참가국", "48개국")
    col2.metric("경기 수", "104경기")
    col3.metric("개최국", "3개국")

    st.markdown("---")

    st.markdown("""
    ### 🌎 개최국

    🇺🇸 미국

    🇨🇦 캐나다

    🇲🇽 멕시코

    역사상 최대 규모의 FIFA 월드컵이 개최됩니다.
    """)

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
