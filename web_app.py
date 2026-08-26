import json
import streamlit as st


DATA_FILE = "prompts.json"


def load_prompts():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_prompts(prompts):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)


st.set_page_config(
    page_title="프롬프트 매니저",
    page_icon="📚",
    layout="wide"
)

st.title("📚 프롬프트 매니저")
st.caption("저장한 프롬프트를 검색하고 관리할 수 있습니다.")

prompts = load_prompts()


# -------------------------
# 사이드바
# -------------------------

st.sidebar.header("메뉴")

menu = st.sidebar.radio(
    "선택",
    [
        "프롬프트 검색",
        "전체 목록",
        "프롬프트 추가",
        "즐겨찾기"
    ]
)


# -------------------------
# 검색
# -------------------------

if menu == "프롬프트 검색":

    st.subheader("🔎 프롬프트 검색")

    keyword = st.text_input(
        "검색어",
        placeholder="예: 블로그, 집배원, 이미지"
    )

    if keyword:

        keyword = keyword.lower()

        results = []

        for prompt in prompts:

            title = prompt.get("title", "").lower()
            content = prompt.get("content", "").lower()
            category = prompt.get("category", "").lower()

            if (
                keyword in title
                or keyword in content
                or keyword in category
            ):
                results.append(prompt)

        st.write(f"검색 결과: {len(results)}개")

        for prompt in results:

            favorite = "⭐ " if prompt.get("favorite") else ""

            with st.expander(
                f'{favorite}[{prompt["category"]}] {prompt["title"]}'
            ):

                st.write(prompt["content"])

                st.code(
                    prompt["content"],
                    language=None
                )


# -------------------------
# 전체 목록
# -------------------------

elif menu == "전체 목록":

    st.subheader("📋 전체 프롬프트")

    st.write(f"총 {len(prompts)}개의 프롬프트")

    for number, prompt in enumerate(prompts, start=1):

        favorite = "⭐ " if prompt.get("favorite") else ""

        with st.expander(
            f'{number}. {favorite}[{prompt["category"]}] {prompt["title"]}'
        ):

            st.write(prompt["content"])


# -------------------------
# 프롬프트 추가
# -------------------------

elif menu == "프롬프트 추가":

    st.subheader("➕ 새 프롬프트 추가")

    title = st.text_input("제목")

    content = st.text_area(
        "프롬프트 내용",
        height=200
    )

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    category = st.selectbox(
        "카테고리",
        categories
    )

    if st.button("저장"):

        if title.strip() == "":

            st.warning("제목을 입력해주세요.")

        elif content.strip() == "":

            st.warning("프롬프트 내용을 입력해주세요.")

        else:

            new_prompt = {
                "title": title.strip(),
                "content": content.strip(),
                "category": category,
                "favorite": False
            }

            prompts.append(new_prompt)

            save_prompts(prompts)

            st.success("프롬프트가 저장되었습니다.")

            st.rerun()


# -------------------------
# 즐겨찾기
# -------------------------

elif menu == "즐겨찾기":

    st.subheader("⭐ 즐겨찾기")

    favorites = [
        prompt
        for prompt in prompts
        if prompt.get("favorite")
    ]

    if len(favorites) == 0:

        st.info("즐겨찾기된 프롬프트가 없습니다.")

    else:

        for prompt in favorites:

            with st.expander(
                f'[{prompt["category"]}] {prompt["title"]}'
            ):

                st.write(prompt["content"])