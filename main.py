import streamlit as st

def main():
    # 🍦 페이지 설정: 기본 타이틀만 남겨봅니다! (지난번 성공한 설정!)
    st.set_page_config(
        page_title="💖 팅커벨의 달콤한 베스킨라빈스 키오스크 💖",
    )

    st.title("🍦 베스킨라빈스 키오스크에 오신 것을 환영해요! ✨", anchor=False)
    st.subheader("달콤한 아이스크림과 함께 행복을 채워보세요! 😊", anchor=False)

    st.markdown("---") # 깔끔한 구분선

    # 1️⃣ 매장/포장 선택: 어떤 방법으로 즐길까요?
    st.header("1. 매장에서 드실래요, 가져가실래요? 🏡📦", anchor=False)
    order_type = st.radio(
        "어떻게 이용하시겠어요?",
        ("매장", "포장"),
        index=0, # 기본값은 '매장'으로!
        horizontal=True, # 나란히 정렬!
        help="아이스크림을 드실 장소를 선택해주세요."
    )
    st.info(f"선택: **{order_type}** 님의 주문을 준비할게요! 🥳")

    st.markdown("---")

    # 2️⃣ 용기 선택: 어떤 사이즈로 가득 채울까요?
    st.header("2. 어떤 용기에 담아드릴까요? 🎁", anchor=False)
    # 용기 정보 딕셔너리: 이름, 최대 맛 개수, 가격
    containers_info = {
        "파인트 🍨 (최대 3가지 맛)": {"max_flavors": 3, "price": 8900},
        "쿼터 🍦🍦 (최대 4가지 맛)": {"max_flavors": 4, "price": 17000},
        "패밀리 👨‍👩‍👧‍👦 (최대 5가지 맛)": {"max_flavors": 5, "price": 24000},
        "하프갤런 🥳 (최대 6가지 맛)": {"max_flavors": 6, "price": 29000},
    }

    container_options = list(containers_info.keys())
    selected_container_name = st.selectbox(
        "가장 끌리는 용기를 선택해주세요! 🤩",
        container_options,
        index=0, # 기본값은 '파인트'
        help="사이즈에 따라 담을 수 있는 맛의 개수가 달라져요!"
    )

    selected_container_data = containers_info[selected_container_name]
    max_flavors_allowed = selected_container_data["max_flavors"]
    container_price = selected_container_data["price"]

    st.success(f"✨ **{selected_container_name}**을(를) 선택하셨어요! 최대 **{max_flavors_allowed}가지** 맛을 고를 수 있고, 가격은 **{container_price:,.0f}원**입니다. 😋")

    st.markdown("---")

    # 3️⃣ 아이스크림 맛 선택: 상상만 해도 달콤! 🍭
    st.header(f"3. 아이스크림 맛을 골라주세요! 🌈 (최대 {max_flavors_allowed}가지)", anchor=False)

    available_flavors = [
        "엄마는 외계인 👽", "아몬드 봉봉 🍫", "베리베리 스트로베리 🍓", "민트 초콜릿 칩 🌿🍫",
        "슈팅스타 ✨", "바람과 함께 사라지다 🌬️", "사랑에 빠진 딸기 💖🍓", "이상한 나라의 솜사탕 ☁️",
        "레인보우 샤베트 🌈", "체리쥬빌레 🍒", "피스타치오 아몬드 💚", "뉴욕 치즈케이크 🍰",
        "초콜릿 무스 🍫", "월넛 🌰", "바닐라 🌼", "초콜릿 🍫"
    ]

    selected_flavors = st.multiselect(
        f"마음껏 골라봐요! 최대 {max_flavors_allowed}가지! 🥳",
        available_flavors,
        default=[],
        max_selections=max_flavors_allowed, # 여기에 '이하값으로'를 적용!
        placeholder=f"최대 {max_flavors_allowed}가지 맛을 선택해주세요! 🥳",
        help="선택한 용기에 맞는 최대 개수만큼 맛을 고를 수 있어요. 그보다 적게 골라도 괜찮아요!"
    )

    # 맛 개수 유효성 검사 (최소 1개는 골라야겠죠? 😊)
    can_proceed = False
    if not selected_flavors:
        st.warning("⚠️ 어서 빨리 첫 번째 맛을 골라보세요! 🤤 (최소 1가지 맛은 선택해주세요.)")
    elif len(selected_flavors) > max_flavors_allowed:
        st.error(f"❌ 아앗! 너무 많이 고르셨어요! 최대 **{max_flavors_allowed}가지** 맛만 선택해주세요! 😥")
    else:
        st.info(f"👍 선택하신 맛은 총 **{len(selected_flavors)}가지** 입니다: **{', '.join(selected_flavors)}**")
        can_proceed = True # 결제로 넘어갈 수 있게!

    st.markdown("---")

    # 4️⃣ 최종 가격 확인 및 결제 방법 선택: 이제 결제할 시간! 💳
    st.header("4. 주문을 확인하고 결제해주세요! 💰", anchor=False)

    # 총 가격은 용기 가격과 동일 (아이스크림 개수를 덜 선택해도 가격은 같아요!)
    total_price = container_price

    st.markdown(f"### 현재 총 결제 금액은... 🤩 **{total_price:,.0f}원** 입니다! ")
    
    st.subheader("어떤 방법으로 결제하시겠어요? 💳", anchor=False)
    payment_method = st.radio(
        "원하시는 결제 방법을 선택해주세요.",
        ("카드결제 💳", "현금결제 💰", "기프티콘 결제 🎁"),
        index=0, # 기본값은 '카드결제'
        horizontal=True,
        help="편하신 방법으로 결제하시면 됩니다."
    )
    st.caption(f"선택하신 결제 방법: **{payment_method}**")

    st.markdown("---")

    # 🎉 최종 주문 버튼!
    if st.button("🎉 주문 완료 및 결제하기 🎉", disabled=not can_proceed):
        st.success("✅ 주문이 성공적으로 접수되었습니다! 잠시만 기다려주세요! 😊")
        st.balloons() # 축하 풍선!

        # 😻 귀여운 아기고양이 이미지 추가!
        # 여기에 단님이 찾으신 아기고양이 이미지 URL을 붙여넣으세요!
        st.image(
            "https://i.imgur.com/7d7Cg1G.jpg", # ✨ 이 URL을 단님이 찾으신 이미지 URL로 바꿔주세요!
            caption="귀여운 아기고양이가 주문 완료를 축하해요! 😻",
            width=300 # 이미지의 너비를 조절할 수 있어요. (원치 않으면 이 줄은 지워도 됩니다)
        )
        
        st.markdown("### 📝 단 님의 주문 내역")
        st.write(f"- **이용 방법**: {order_type} 🥳")
        st.write(f"- **선택 용기**: {selected_container_name}")
        if selected_flavors:
            st.write(f"- **선택 맛 ({len(selected_flavors)}가지)**: {', '.join(selected_flavors)} 💖")
        else:
            st.write("- **선택된 맛이 없습니다. (그래도 용기 가격은 동일해요! 😊)**")
        st.write(f"- **결제 방법**: {payment_method}")
        st.markdown(f"## 💰 최종 결제 금액: <span style='color:green;'>**{total_price:,.0f}원**</span> 입니다! 다시 한번 감사드려요! 💖", unsafe_allow_html=True)

        st.info("💡 맛있게 드시고 행복한 하루 되세요! 이 화면은 잠시 후 초기화됩니다. (실제 앱에서는 페이지 새로고침이나 세션 초기화 로직을 추가할 수 있어요!)")
        # st.experimental_rerun() # 여기서는 예시를 위해 주석 처리합니다.

    else:
        if not can_proceed and st.session_state.get('last_button_click_attempted', False):
            st.error("⚠️ 주문을 완료하려면 아이스크림 맛을 최소 1가지 이상, 그리고 최대 허용 개수 이하로 선택해주세요! 🧐")
        elif not can_proceed:
            st.warning("위의 단계를 모두 완료하시면 주문 버튼이 활성화됩니다! 😊")

# Streamlit 앱 실행
if __name__ == "__main__":
    if 'last_button_click_attempted' not in st.session_state:
        st.session_state['last_button_click_attempted'] = False
    
    main()
