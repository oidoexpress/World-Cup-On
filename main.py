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
st.title("🇰🇷 Korea World Cup On")

st.image(
    "https://img.sbs.co.kr/newimg/news/20230518/201785626_500.jpg",
    use_container_width=True
)

st.subheader("2026 FIFA 북중미 월드컵 대한민국 응원 플랫폼")

col1, col2, col3 = st.columns(3)

col1.metric("최고 성적", "4강")
col2.metric("월드컵 진출", "11회 연속")
col3.metric("FIFA 랭킹", "조회중...")
elif menu == "🇰🇷 대한민국 대표팀":

    st.title("🇰🇷 대한민국 축구 국가대표")

    st.write("""
    감독 : 홍명보

    별명 : 태극전사

    협회 : 대한축구협회(KFA)

    최고 성적 : 2002 월드컵 4강
    """)

    st.image(
        "https://upload.wikimedia.org/wikipedia/en/0/09/Korea_Football_Association_logo.svg",
        width=200
    )
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
            "즈베즈다"
        ]
    })

    st.dataframe(
        players,
        use_container_width=True
    )
elif menu == "📊 FIFA 랭킹":

    ranking = pd.DataFrame({
        "순위":[1,2,3,4,5],
        "국가":[
            "아르헨티나",
            "프랑스",
            "스페인",
            "잉글랜드",
            "브라질"
        ]
    })

    st.dataframe(ranking)
if "Korea" in home or "Korea" in away:
    for match in matches:

    home = match.get("strHomeTeam","")
    away = match.get("strAwayTeam","")

    if "Korea" in home or "Korea" in away:

        st.success(
            f"{home} {home_score} : {away_score} {away}"
        )
